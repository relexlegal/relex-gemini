# Submission — Gemini CLI extension gallery

> Prepared 2026-10-28 on branch `directory-review-2026-10`. Nothing has been
> submitted, pushed or deployed. Before any submission: deploy the backend branch
> `directory-review-2026-10` (neutral server instructions, data-only responses),
> then merge and push this repo.

Hosted server: `https://relex.legal/api/mcp` (streamable HTTP, OAuth 2.1 with
PKCE and dynamic client registration). Twelve tools: `list_matters`,
`read_matter_context`, `diagnose_matter_sources`, `read_matter_source`,
`save_matter_work_product`, `correct_matter_ontology`, `conclude_matter_session`,
`find_legal_professionals`, `read_legal_professional`,
`prepare_professional_request`, `search`, `execute`.

The gallery (geminicli.com/extensions) is crawled daily from public GitHub repos
that carry the `gemini-cli-extension` topic and a root `gemini-extension.json`.
There is no form.

## Done in this branch
- [x] `gemini-extension.json` 0.1.8 with `description`, `mcpServers.relex.httpUrl`, OAuth enabled, `contextFileName: GEMINI.md`.
- [x] Skills mirrored to the extension root (`skills/`, `references/`) — Gemini CLI only discovers `<extension root>/skills/<name>/SKILL.md`. Source of truth stays `plugin/`; `python3 scripts/sync_gemini_extension.py` regenerates, `--check` verifies (run it in CI / before tagging).
- [x] GEMINI.md and SECURITY.md: twelve tools; reading default corrected.
- [ ] `plugin/agents/` is not mirrored (Gemini subagents are a preview feature).

## User must do
- [ ] Deploy backend, merge and push to `main` of github.com/relexlegal/relex-gemini (public).
- [ ] Add the repo topic `gemini-cli-extension` (repo currently has no topics).
- [ ] Tag and publish a GitHub release `v0.1.8`.
- [ ] Smoke test: `gemini extensions install https://github.com/relexlegal/relex-gemini --consent`, then authenticate the `relex` MCP server (`/mcp auth relex`) and check that the Relex skills and the twelve tools are listed (`/mcp`).
