# Security

Relex lets you use Gemini on legal matters **without exposing client PII**.

## Authentication

- MCP: `https://relex.legal/api/mcp`
- OAuth via Gemini CLI `/mcp auth` or Enterprise-configured OAuth
- API key fallback: Relex **Settings → API Keys**

## Client PII never reaches the model

- Parties sealed client-side; documents read and redacted by the Relex Private Model on Relex servers by default
- MCP `execute` blocks plaintext party/document endpoints

## Reporting

**security@relex.legal**
