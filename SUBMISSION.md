# Submission — Gemini CLI extension gallery

> Prepared 2026-10-28; updated the same day for MCP server version 1.1.0
> (branch `docs/read-api-1.1.0`). Nothing has been submitted. The backend with
> neutral server instructions, data-only responses and the `read_api` tool is
> on `master` (5a5d7b9) and deployed as revision `relex-backend-00192`.

Hosted server: `https://relex.legal/api/mcp` (streamable HTTP, OAuth 2.1 with
PKCE and dynamic client registration). Thirteen tools: `list_matters`,
`read_matter_context`, `diagnose_matter_sources`, `read_matter_source`,
`save_matter_work_product`, `correct_matter_ontology`, `conclude_matter_session`,
`find_legal_professionals`, `read_legal_professional`,
`prepare_professional_request`, `search`, `read_api`, `execute`.

Server version 1.1.0. `read_api` reads one GET endpoint (read-only; parameters
`path` and optional `query`). `execute` creates, updates or deletes through one
endpoint (POST/PUT/PATCH/DELETE); DELETE and other irreversible routes are not
applied by the tool and return a Relex deep link where the user confirms the
change.

The gallery (geminicli.com/extensions) is crawled daily from public GitHub repos
that carry the `gemini-cli-extension` topic and a root `gemini-extension.json`.
There is no form.

## Done in this branch
- [x] `gemini-extension.json` 0.1.9 with `description`, `mcpServers.relex.httpUrl`, OAuth enabled, `contextFileName: GEMINI.md`.
- [x] Skills mirrored to the extension root (`skills/`, `references/`) — Gemini CLI only discovers `<extension root>/skills/<name>/SKILL.md`. Source of truth stays `plugin/`; `python3 scripts/sync_gemini_extension.py` regenerates, `--check` verifies (run it in CI / before tagging).
- [x] GEMINI.md and SECURITY.md: thirteen tools; reading default corrected.
- [ ] `plugin/agents/` is not mirrored (Gemini subagents are a preview feature).

## User must do
- [ ] Make sure github.com/relexlegal/relex-gemini is public.
- [ ] Add the repo topic `gemini-cli-extension` (repo currently has no topics).
- [ ] Tag and publish a GitHub release `v0.1.9`.
- [ ] Smoke test: `gemini extensions install https://github.com/relexlegal/relex-gemini --consent`, then authenticate the `relex` MCP server (`/mcp auth relex`) and check that the Relex skills and the thirteen tools are listed (`/mcp`).
