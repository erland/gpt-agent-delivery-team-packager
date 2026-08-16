#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, shutil, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = [
    'agent-delivery-package-templates.md',
    'codex-agent-toml-templates.md',
    'script-templates.md',
    'validation-checklists.md',
    'gpt-setup-reference.md',
    'prompt-recipes.md',
]

def semver(value: str) -> str:
    value = value.strip()
    if value.startswith('v'):
        value = value[1:]
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?', value):
        raise SystemExit(f'Invalid version: {value!r}. Expected semantic version such as 1.0.0 or v1.0.0.')
    return value

def extract_instruction() -> str:
    return (ROOT/'gpt-configuration/instructions.txt').read_text(encoding='utf-8')

def extract_starters() -> str:
    return (ROOT/'gpt-configuration/conversation-starters.md').read_text(encoding='utf-8')

def sha256(path: Path) -> str:
    h=hashlib.sha256(); h.update(path.read_bytes()); return h.hexdigest()

def zip_tree(src: Path, target: Path):
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(x for x in src.rglob('*') if x.is_file()):
            info=zipfile.ZipInfo(p.relative_to(src).as_posix(), date_time=(1980,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o644<<16
            z.writestr(info,p.read_bytes())

def copy(src: str, dst: Path):
    s=ROOT/src; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(s,dst)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--version'); ap.add_argument('--output-dir',default='dist')
    a=ap.parse_args(); version=semver(a.version or (ROOT/'VERSION').read_text())
    out=(ROOT/a.output_dir).resolve(); shutil.rmtree(out,ignore_errors=True); out.mkdir(parents=True)
    work=out/'.build'; custom=work/'custom'; portable=work/'portable'
    custom.mkdir(parents=True); portable.mkdir(parents=True)
    instruction=extract_instruction(); starters=extract_starters()

    # Custom GPT setup package: canonical configuration + six uploaded knowledge files.
    for rel in ['README.md','docs/package-manifest.md']:
        copy(rel, custom/rel)
    copy('gpt-configuration/instructions.txt', custom/'gpt-configuration/instructions.txt')
    copy('gpt-configuration/conversation-starters.md', custom/'gpt-configuration/conversation-starters.md')
    for name in KNOWLEDGE: copy(f'knowledge/{name}', custom/'knowledge'/name)
    (custom/'VERSION').write_text(version+'\n',encoding='utf-8')

    # Portable chat package.
    copy('portable/START-HERE.md', portable/'START-HERE.md')
    (portable/'assistant').mkdir()
    (portable/'assistant/instructions.txt').write_text(instruction,encoding='utf-8')
    (portable/'assistant/conversation-starters.md').write_text(starters,encoding='utf-8')
    for name in KNOWLEDGE: copy(f'knowledge/{name}', portable/'knowledge'/name)
    (portable/'VERSION').write_text(version+'\n',encoding='utf-8')
    manifest={'package':'agent-delivery-team-packager','format':'portable-chat-assistant','version':version,'entrypoint':'START-HERE.md','instructions':'assistant/instructions.txt','conversation_starters':'assistant/conversation-starters.md','knowledge':[f'knowledge/{x}' for x in KNOWLEDGE]}
    files={}
    for p in sorted(x for x in portable.rglob('*') if x.is_file() and x.name!='MANIFEST.json'):
        files[p.relative_to(portable).as_posix()]=sha256(p)
    manifest['files']=files
    (portable/'MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

    cz=out/f'agent-delivery-team-packager-custom-gpt-v{version}.zip'; pz=out/f'agent-delivery-team-packager-chat-v{version}.zip'
    zip_tree(custom,cz); zip_tree(portable,pz); shutil.rmtree(work)
    print(cz); print(pz)
if __name__=='__main__': main()
