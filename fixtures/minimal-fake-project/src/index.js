function formatGreeting(name) {
  const trimmed = String(name || "").trim();
  return trimmed ? `Hello, ${trimmed}!` : "Hello!";
}

if (require.main === module) {
  console.log(formatGreeting("Agent Delivery Team"));
}

module.exports = { formatGreeting };
