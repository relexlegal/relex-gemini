# Relex Legal Workspace (Gemini)

Connect Gemini to the remote MCP server at `https://relex.legal/api/mcp`.

## What you get

Eleven tools over Streamable HTTP: matter list/context/diagnose, save work
product, ontology corrections, conclude session, professional discovery, plus
generic `search` / `execute` against the validated Relex API. Auth is browser
OAuth 2.1 + PKCE (no API-key paste required for interactive use).

## Install

```bash
gemini extensions install https://github.com/relexlegal/relex-gemini --consent
# or from a local checkout:
gemini extensions install . --consent
gemini mcp list
```

Or add the server directly:

```bash
gemini mcp add --transport http relex https://relex.legal/api/mcp
```

Then authorize when prompted. Use only synthetic / QA matters for testing.

## Host notes

- Gemini CLI uses a loopback redirect `http://localhost:<port>/oauth/callback`.
- Gemini app (Connected Apps → Custom) registers Google `oauth-redirect*.googleusercontent.com` relays; personal accounts, US/English only on Google’s side.
- Installing this extension does not grant access to private Relex data until the user completes OAuth consent.
