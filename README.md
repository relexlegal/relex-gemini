# Relex × Gemini

**Legal Workspace — One source of truth for any Agent — confidential by design**

Keep legal knowledge, matter context and saved progress in Relex, independently
of the assistant you use. Authorize another compatible agent to continue from
the same stored context, without rebuilding the background in another chat.

## Portable context, with your permission

1. Create or open the matter in Relex and add information through its protected
   intake and document workflows.
2. Connect a supported client to `https://relex.legal/api/mcp` and authorize
   your own Relex account. Installing a package does not authorize private data.
3. Ask the agent to read the permitted matter context before working and save
   its conclusions when finished. A second authorized client can then use that
   continuing record.

Portability covers information saved in Relex, not automatic import of private
chat histories or a model's internal memory. Client-side identity encryption,
de-identification and MCP access controls protect the supported workflows;
de-identified legal facts may still be sensitive. Review what you authorize.

## Workspace, SDK and Marketplace

Use **Legal Workspace** for persistent legal context; the **Legal SDK** for
building your firm's or legal department's own platform; and the
**Legal Marketplace** to discover published professional profiles or make an
AI-first law firm discoverable across specialties.

An agent may help find a professional and prepare a reference-only request.
The user must review and approve sharing in Relex. Discovery is not engagement,
a completed conflict check, payment or a guarantee of professional availability.

Client support depends on the host product, plan and administrator settings.
Gemini CLI support does not imply support in every Gemini web experience.
Harvey BYOMCP is a customer-admin connection path, not a claim of Harvey
Connector Library listing or approval. Check the current
[connector guides](https://relex.legal/docs/connectors) and
[portable-context guide](https://relex.legal/guides/portable-legal-context).
## Official Google / Gemini names

| Surface | Product calls it |
|---------|------------------|
| **Gemini CLI** | **MCP server** (`gemini mcp add`, `mcpServers` in settings) |
| **Gemini Enterprise** | **Custom MCP Server** (data store / connector) |
| Personal Gemini web chat | Usually **no** arbitrary custom MCP — use CLI or Enterprise |

Always name **`relex`**, URL `https://relex.legal/api/mcp` (Streamable HTTP).

## How it works

Gemini connects over **Streamable HTTP** MCP. Tools: `search`, `execute`.
Auth: **`/mcp auth relex`** (browser OAuth) on CLI, or **API key** / Enterprise
IdP wiring as configured by admin.

## Quick start — Gemini CLI

```bash
gemini mcp add --transport http relex https://relex.legal/api/mcp
```

List status:

```bash
gemini mcp list
```

Authenticate when prompted:

```text
/mcp auth relex
```

Then say:

> Set up my practice workflow with Relex

### settings.json equivalent

User config `~/.gemini/settings.json` or project `.gemini/settings.json`:

```json
{
  "mcpServers": {
    "relex": {
      "httpUrl": "https://relex.legal/api/mcp"
    }
  }
}
```

With API key:

```json
{
  "mcpServers": {
    "relex": {
      "httpUrl": "https://relex.legal/api/mcp",
      "headers": {
        "Authorization": "Bearer rlx_..."
      }
    }
  }
}
```

> Tip: avoid underscores in the server name (`relex` is good; `relex_legal` can
> break some Gemini policy FQN parsers).

## Personal vs Team / Enterprise

| Plan / product | Who installs | Who connects |
|----------------|--------------|--------------|
| **Gemini CLI (personal)** | You run `gemini mcp add` | You complete `/mcp auth` / OAuth |
| **Gemini Enterprise / Google Cloud** | **Admin** registers a Custom MCP Server / data store for the org application | Members use the app; OAuth or IdP as configured by admin |

### Gemini Enterprise (admin)

1. Deploy or point at the **hosted** Relex URL (no need to re-host unless
   required by network policy): `https://relex.legal/api/mcp`.
2. In Gemini Enterprise / Agent Builder, add a **Custom MCP Server** connector
   with that URL.
3. Configure OAuth / IdP per Google’s custom MCP docs.
4. Publish the application so members can use Relex tools.

Members typically **cannot** register arbitrary custom MCP servers themselves
in a managed Enterprise tenant — same pattern as Claude Team and ChatGPT
Enterprise.

Full guide: [`docs/install.md`](docs/install.md) ·
[`docs/connect-gemini-cli.md`](docs/connect-gemini-cli.md) ·
[`docs/connect-gemini-enterprise.md`](docs/connect-gemini-enterprise.md).

## Layout

```
relex-gemini/
├── plugin/
│   ├── .mcp.json
│   ├── plugin.json
│   ├── skills/
│   ├── agents/
│   ├── commands/
│   └── references/
├── docs/
│   ├── install.md
│   ├── connect-gemini-cli.md
│   ├── connect-gemini-enterprise.md
│   └── positioning.md
└── SECURITY.md
```

## Docs on relex.legal

- [Gemini connector](https://relex.legal/docs/connectors/gemini)
- [MCP Server](https://relex.legal/docs/mcp)
- [For AI Agents](https://relex.legal/for-agents)

## License

AGPL-3.0-or-later — see [LICENSE](LICENSE).
