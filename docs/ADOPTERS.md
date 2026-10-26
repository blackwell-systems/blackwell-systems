# Adopters

Third-party repositories that use Blackwell Systems projects, each verified by opening the file listed under Evidence. Last verified 2026-10-26.

**120 repositories across 59 organizations and developers**, plus 2 adopters without a public repository (Open Data Products SDK, SkyElite).

| Project | Repositories |
|---|---|
| [GCF](https://github.com/blackwell-systems/gcf) | 26 |
| [agent-lsp](https://github.com/blackwell-systems/agent-lsp) | 40 |
| [mcp-assert](https://github.com/blackwell-systems/mcp-assert) | 42 |
| [GCP emulators](https://github.com/blackwell-systems/gcp-emulator) | 11 |
| [claudewatch](https://github.com/blackwell-systems/claudewatch) | 2 |

Counted: direct use in code, dependency manifests, MCP and editor configs, CI, containers, packaging, and vendored skills. Not counted: our own repositories, forks, copies of an adopting project, packages that arrive only indirectly through another dependency (lockfile-only), catalogs and awesome lists, documentation-only mentions, and unrelated projects that share a name. The full method and scripts are in [`adoption/`](../adoption/).

## GCF

| Repository | Stars | How it is used | Evidence |
|---|---|---|---|
| [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | 81,414 | GCF encoder vendored into its compression engine | `open-sse/services/compression/engines/headroom/gcf/index.ts` |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 54,203 | Optional GCF output for MCP tool results | `package.json` |
| [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | 4,356 | Optional GCF output (gcf-python) | `pyproject.toml` |
| [automateyournetwork/netclaw](https://github.com/automateyournetwork/netclaw) | 685 | GCF for MCP responses (gcf-python) | `src/netclaw_tokens/requirements.txt` |
| [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | 638 | GCF context encoding | `package.json` |
| [stevesolun/ctx](https://github.com/stevesolun/ctx) | 589 | Optional GCF extra (gcf-python) | `pyproject.toml` |
| [erikdarlingdata/PerformanceMonitor](https://github.com/erikdarlingdata/PerformanceMonitor) | 524 | Opt-in GCF output for MCP tools (.NET SDK) | `Directory.Packages.props` |
| [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) | 314 | GCF responses (gcf-python) | `pyproject.toml` |
| [speakeasy-api/openapi](https://github.com/speakeasy-api/openapi) | 276 | GCF output in its oq CLI | `go.mod` |
| [gensecaihq/Wazuh-MCP-Server](https://github.com/gensecaihq/Wazuh-MCP-Server) | 258 | Opt-in GCF responses (gcf-python) | `pyproject.toml` |
| [erikdarlingdata/PerformanceStudio](https://github.com/erikdarlingdata/PerformanceStudio) | 245 | Opt-in GCF output for MCP tools (.NET SDK) | `Directory.Packages.props` |
| [daniel3303/Equibles](https://github.com/daniel3303/Equibles) | 240 | Opt-in GCF output for table tools (.NET SDK) | `Directory.Packages.props` |
| [gensecaihq/pfsense-mcp-server](https://github.com/gensecaihq/pfsense-mcp-server) | 112 | Opt-in GCF responses | `src/server.py` |
| [sieteunoseis/mcp-cisco-support](https://github.com/sieteunoseis/mcp-cisco-support) | 33 | GCF response format | `package.json` |
| [NETGVai/NeuroNest](https://github.com/NETGVai/NeuroNest) | 20 | GCF serializer | `package.json` |
| [operasoftware/opera-devtools-mcp](https://github.com/operasoftware/opera-devtools-mcp) | 15 | Optional GCF output for MCP tool results | `package.json` |
| [hewimetall/vmcp](https://github.com/hewimetall/vmcp) | 13 | GCF output from its MCP gateway | `crates/vmcp-server/src/gcf_out.rs` |
| [thawkins/ragent](https://github.com/thawkins/ragent) | 7 | GCF crate behind a config flag | `crates/ragent-config/src/gcf.rs` |
| [dmmdea/offload-harness](https://github.com/dmmdea/offload-harness) | 4 | GCF encoding in its harness | `internal/gcf/gcf.go` |
| [pcDamasceno/neterse](https://github.com/pcDamasceno/neterse) | 3 | Optional GCF extra (gcf-python) | `pyproject.toml` |
| [chaitanya-sharmaa/axon](https://github.com/chaitanya-sharmaa/axon) | 2 | GCF (gcf-python) | `pyproject.toml` |
| [payfacto/bb](https://github.com/payfacto/bb) | 1 | GCF output for agent consumption | `go.mod` |
| [ChetanKoneru/gcf-mode](https://github.com/ChetanKoneru/gcf-mode) | 0 | Emacs major mode for .gcf files | `gcf-mode.el` |
| [Starlit-Digital/bram](https://github.com/Starlit-Digital/bram) | 0 | GCF output format (gcf-go) | `go.mod` |
| [Starlit-Digital/clyde](https://github.com/Starlit-Digital/clyde) | 0 | GCF agent context (gcf-go) | `go.mod` |
| [Starlit-Digital/loom](https://github.com/Starlit-Digital/loom) | 0 | GCF snapshots (gcf-go) | `go.mod` |

## agent-lsp

| Repository | Stars | How it is used | Evidence |
|---|---|---|---|
| [liuyanghejerry/Clausura](https://github.com/liuyanghejerry/Clausura) | 204 | agent-lsp as a command backend for CI code review | `examples/mcp-lsp-review.yaml` |
| [nix-community/nur-combined](https://github.com/nix-community/nur-combined) | 204 | Packaged in the Nix User Repository | `NUR package` |
| [NVlabs/Skill2Env](https://github.com/NVlabs/Skill2Env) | 190 | Vendors agent-lsp skills | `lsp-safe-edit SKILL.md` |
| [sudosubin/agents.nix](https://github.com/sudosubin/agents.nix) | 18 | agent-lsp skills packaged for Nix | `skills` |
| [artemnoor/CodeSlicer](https://github.com/artemnoor/CodeSlicer) | 14 | CI tests against agent-lsp | `pyproject.toml` |
| [hewimetall/vmcp](https://github.com/hewimetall/vmcp) | 13 | agent-lsp as the LSP layer behind its gateway | `scripts/run-agent-lsp.sh` |
| [krabka-io/krabka-broker](https://github.com/krabka-io/krabka-broker) | 6 | agent-lsp in project MCP config | `.mcp.json` |
| [loic-roux-404/plateforme](https://github.com/loic-roux-404/plateforme) | 6 | agent-lsp in VS Code MCP config (Nix, Terraform, YAML) | `.vscode/mcp.json` |
| [AlexaDeWit/Ecluse](https://github.com/AlexaDeWit/Ecluse) | 5 | agent-lsp in project MCP config | `.mcp.json` |
| [berlinguyinca/autospec](https://github.com/berlinguyinca/autospec) | 3 | agent-lsp code-intelligence backend | `docs/code-intelligence.md` |
| [OKHP3/skillz](https://github.com/OKHP3/skillz) | 3 | Vendors agent-lsp skills | `lsp-safe-edit SKILL.md` |
| [Mission-Platform/composable-mission-ready-platform](https://github.com/Mission-Platform/composable-mission-ready-platform) | 2 | Vendors agent-lsp skills | `lsp-safe-edit SKILL.md` |
| [Hellblazer/qwen-coprocessor-stack](https://github.com/Hellblazer/qwen-coprocessor-stack) | 1 | agent-lsp MCP server for coprocessor agents | `config/coprocessor-pool-codeintel.example.json` |
| [krabka-io/krabka-io.github.io](https://github.com/krabka-io/krabka-io.github.io) | 1 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-schema-registry](https://github.com/krabka-io/krabka-schema-registry) | 1 | agent-lsp in project MCP config | `.mcp.json` |
| [OKHP3/askjamie-foundry](https://github.com/OKHP3/askjamie-foundry) | 1 | Vendors agent-lsp skills | `lsp-safe-edit SKILL.md` |
| [aashutosh396/mindpalace](https://github.com/aashutosh396/mindpalace) | 0 | Vendors the agent-lsp skill | `_skillforge/MANIFEST.json` |
| [bit0rez/gentoo_overlay](https://github.com/bit0rez/gentoo_overlay) | 0 | Gentoo ebuild for agent-lsp | `dev-misc/agent-lsp/agent-lsp-0.19.2.ebuild` |
| [Borgvall/Decanter](https://github.com/Borgvall/Decanter) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/gres](https://github.com/krabka-io/gres) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-cli](https://github.com/krabka-io/krabka-cli) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-client-rs](https://github.com/krabka-io/krabka-client-rs) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-connect](https://github.com/krabka-io/krabka-connect) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-gateway](https://github.com/krabka-io/krabka-gateway) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-o11y-demo](https://github.com/krabka-io/krabka-o11y-demo) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-operator](https://github.com/krabka-io/krabka-operator) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-protocol](https://github.com/krabka-io/krabka-protocol) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-rebalancer](https://github.com/krabka-io/krabka-rebalancer) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-streams-go](https://github.com/krabka-io/krabka-streams-go) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-streams-java](https://github.com/krabka-io/krabka-streams-java) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/krabka-streams-rs](https://github.com/krabka-io/krabka-streams-rs) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [krabka-io/tooling](https://github.com/krabka-io/tooling) | 0 | agent-lsp in project MCP config | `.mcp.json` |
| [leafclick/codex-universal](https://github.com/leafclick/codex-universal) | 0 | agent-lsp installed in its Codex image | `Dockerfile.generic` |
| [PCSchmidt/Syntaris](https://github.com/PCSchmidt/Syntaris) | 0 | Vendors agent-lsp skills | `lsp-safe-edit SKILL.md` |
| [selfagency/bifrost-docker](https://github.com/selfagency/bifrost-docker) | 0 | agent-lsp installed in its Docker image | `Dockerfile` |
| [TDQUOC/TDQ-Workflow](https://github.com/TDQUOC/TDQ-Workflow) | 0 | Setup script installs agent-lsp releases | `scripts/tdq_setup.py` |
| Individual developers (4) | | Personal setups: dotfiles, homelab and Nix configurations | |

## mcp-assert

| Repository | Stars | How it is used | Evidence |
|---|---|---|---|
| [WYRE-AI/autotask-mcp](https://github.com/WYRE-AI/autotask-mcp) | 58 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/connectwise-manage-mcp](https://github.com/WYRE-AI/connectwise-manage-mcp) | 28 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/ninjaone-mcp](https://github.com/WYRE-AI/ninjaone-mcp) | 26 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/itglue-mcp](https://github.com/WYRE-AI/itglue-mcp) | 17 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/cipp-mcp](https://github.com/WYRE-AI/cipp-mcp) | 11 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/proofpoint-mcp](https://github.com/WYRE-AI/proofpoint-mcp) | 5 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/datto-rmm-mcp](https://github.com/WYRE-AI/datto-rmm-mcp) | 4 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/syncro-mcp](https://github.com/WYRE-AI/syncro-mcp) | 4 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/action1-mcp](https://github.com/WYRE-AI/action1-mcp) | 3 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/halopsa-mcp](https://github.com/WYRE-AI/halopsa-mcp) | 3 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/hudu-mcp](https://github.com/WYRE-AI/hudu-mcp) | 3 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/superops-mcp](https://github.com/WYRE-AI/superops-mcp) | 3 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/qbo-mcp](https://github.com/WYRE-AI/qbo-mcp) | 2 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/auvik-mcp](https://github.com/WYRE-AI/auvik-mcp) | 1 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/avanan-mcp](https://github.com/WYRE-AI/avanan-mcp) | 1 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/connectwise-automate-mcp](https://github.com/WYRE-AI/connectwise-automate-mcp) | 1 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/huntress-mcp](https://github.com/WYRE-AI/huntress-mcp) | 1 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/inforcer-mcp](https://github.com/WYRE-AI/inforcer-mcp) | 1 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/kaseya-quote-manager-mcp](https://github.com/WYRE-AI/kaseya-quote-manager-mcp) | 1 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/mimecast-mcp](https://github.com/WYRE-AI/mimecast-mcp) | 1 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/xero-mcp](https://github.com/WYRE-AI/xero-mcp) | 1 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/abnormal-mcp](https://github.com/WYRE-AI/abnormal-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/atera-mcp](https://github.com/WYRE-AI/atera-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/connectwise-cpq-mcp](https://github.com/WYRE-AI/connectwise-cpq-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/crewhu-mcp](https://github.com/WYRE-AI/crewhu-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/domotz-mcp](https://github.com/WYRE-AI/domotz-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/freshdesk-mcp](https://github.com/WYRE-AI/freshdesk-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/ironscales-mcp](https://github.com/WYRE-AI/ironscales-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/knowbe4-mcp](https://github.com/WYRE-AI/knowbe4-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/liongard-mcp](https://github.com/WYRE-AI/liongard-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/mailprotector-mcp](https://github.com/WYRE-AI/mailprotector-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/mcp-eval-baseline](https://github.com/WYRE-AI/mcp-eval-baseline) | 0 | Composite action wrapping mcp-assert-action | `action.yml` |
| [WYRE-AI/reusable-workflows](https://github.com/WYRE-AI/reusable-workflows) | 0 | Release workflow runs mcp-assert | `.github/workflows/mcp-server-release.yml` |
| [WYRE-AI/rocketcyber-mcp](https://github.com/WYRE-AI/rocketcyber-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/rootly-mcp](https://github.com/WYRE-AI/rootly-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/saas-alerts-mcp](https://github.com/WYRE-AI/saas-alerts-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/salesbuildr-mcp](https://github.com/WYRE-AI/salesbuildr-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/scalepad-mcp](https://github.com/WYRE-AI/scalepad-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/sherweb-mcp](https://github.com/WYRE-AI/sherweb-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [WYRE-AI/spamtitan-mcp](https://github.com/WYRE-AI/spamtitan-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |
| [wyre-technology/.github](https://github.com/wyre-technology/.github) | 0 | Shared reusable mcp-assert workflow | `.github/workflows/mcp-assert.yml` |
| [wyre-technology/afkbot-mcp](https://github.com/wyre-technology/afkbot-mcp) | 0 | mcp-assert in CI via the shared workflow | `.github/workflows/mcp-assert.yml` |

## GCP emulators

| Repository | Stars | How it is used | Evidence |
|---|---|---|---|
| [apereo/cas](https://github.com/apereo/cas) | 11,390 | Secret Manager emulator in CI | `ci/tests/gcp/run-gcp-server.sh` |
| [flipt-io/flipt](https://github.com/flipt-io/flipt) | 4,928 | Secret Manager emulator in integration tests | `build/testing/integration.go` |
| [camunda/camunda](https://github.com/camunda/camunda) | 4,339 | Secret Manager emulator in end-to-end tests | `secret-store/.../SecretManagerEmulatorContainer.java` |
| [akash-network/console](https://github.com/akash-network/console) | 263 | KMS emulator in the dev stack | `packages/docker/docker-compose.dev.yml` |
| [qamarudeenm/minisky](https://github.com/qamarudeenm/minisky) | 58 | Secret Manager service in a local GCP emulator | `docker/secretmanager.Dockerfile` |
| [reagento/dature](https://github.com/reagento/dature) | 48 | Secret Manager and IAM emulators in integration tests | `tests/integration/sources/gcp_secret_manager/` |
| [adorsys/status-list-server](https://github.com/adorsys/status-list-server) | 26 | Secret Manager emulator in Rust integration tests | `tests/gcp_secrets_manager.rs` |
| [mpyw/suve](https://github.com/mpyw/suve) | 14 | Secret Manager emulator in test environments | `compose.yaml` |
| [mferretti/SeedStream](https://github.com/mferretti/SeedStream) | 4 | Secret Manager emulator in integration tests | `GoogleSecretManagerResolverIT.java` |
| [farmisen/zuul](https://github.com/farmisen/zuul) | 3 | Secret Manager emulator (built from a fork) in Docker Compose | `docker-compose.emulator.yml` |
| [lagdo/dbadmin-mono](https://github.com/lagdo/dbadmin-mono) | 2 | Secret Manager emulator in Docker Compose | `docker/compose-secrets/docker-compose.yml` |

## claudewatch

| Repository | Stars | How it is used | Evidence |
|---|---|---|---|
| Individual developers (2) | | Personal setups: dotfiles, homelab and Nix configurations | |

## Adopters without a public repository

| Project | Adopter | How it is used |
|---|---|---|
| GCF | [Open Data Products SDK](https://opendataproducts.org/sdk/) (Linux Foundation) | GCF sidecars for ODPC and ODPG workflows |
| GCF | SkyElite (SkyElite team) | GCF for cross-agent context in a LangGraph multi-agent travel planner |

Using one of these projects? Open an issue or pull request on the project's repository and it will be added here.
