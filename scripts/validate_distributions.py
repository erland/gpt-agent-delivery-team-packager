#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, tempfile, zipfile
from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('builder',ROOT/'scripts/build_distributions.py'); b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)

def sha(p):
 h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--version'); ap.add_argument('--dist-dir',default='dist'); a=ap.parse_args()
 v=b.semver(a.version or (ROOT/'VERSION').read_text()); d=(ROOT/a.dist_dir).resolve()
 custom=d/f'agent-delivery-team-packager-custom-gpt-v{v}.zip'; portable=d/f'agent-delivery-team-packager-chat-v{v}.zip'
 for z in [custom,portable]:
  if not z.is_file(): raise SystemExit(f'Missing {z}')
  with zipfile.ZipFile(z) as q:
   bad=q.testzip()
   if bad: raise SystemExit(f'Corrupt entry {bad} in {z}')
 with tempfile.TemporaryDirectory() as td:
  td=Path(td)
  with zipfile.ZipFile(custom) as q:q.extractall(td/'c')
  with zipfile.ZipFile(portable) as q:q.extractall(td/'p')
  instruction=b.extract_instruction().encode(); starters=b.extract_starters().encode()
  if (td/'c/gpt-configuration/instructions.txt').read_bytes()!=instruction: raise SystemExit('Custom instructions mismatch')
  if (td/'p/assistant/instructions.txt').read_bytes()!=instruction: raise SystemExit('Portable instructions mismatch')
  if (td/'c/gpt-configuration/conversation-starters.md').read_bytes()!=starters: raise SystemExit('Custom starters mismatch')
  if (td/'p/assistant/conversation-starters.md').read_bytes()!=starters: raise SystemExit('Portable starters mismatch')
  for n in b.KNOWLEDGE:
   src=(ROOT/'knowledge'/n).read_bytes()
   if (td/'c/knowledge'/n).read_bytes()!=src: raise SystemExit(f'Custom knowledge mismatch: {n}')
   if (td/'p/knowledge'/n).read_bytes()!=src: raise SystemExit(f'Portable knowledge mismatch: {n}')
  if (td/'c/VERSION').read_text().strip()!=v or (td/'p/VERSION').read_text().strip()!=v: raise SystemExit('VERSION mismatch')
  m=json.loads((td/'p/MANIFEST.json').read_text())
  if m['version']!=v: raise SystemExit('Manifest version mismatch')
  for rel,h in m['files'].items():
   if sha(td/'p'/rel)!=h: raise SystemExit(f'Manifest hash mismatch: {rel}')
 print(f'OK: validated custom GPT and portable Chat distributions for {v}.')
if __name__=='__main__':main()
