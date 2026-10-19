**English** · [简体中文](docs/i18n/README.zh-CN.md) · [Русский](docs/i18n/README.ru.md) · [हिन्दी](docs/i18n/README.hi.md) · [العربية](docs/i18n/README.ar.md)

[![Blackwell Systems™](https://raw.githubusercontent.com/blackwell-systems/blackwell-docs-theme/main/badge-trademark.svg)](https://github.com/blackwell-systems) [![Stars](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/blackwell-systems/blackwell-systems/main/stars-badge.json)](https://github.com/blackwell-systems)

## Blackwell Systems: building the agentic stack, publishing the proof

Founder: Dayna Blackwell. I build the open infrastructure the agentic AI stack runs on, and ship the evidence to back it: durable agents, wire formats, code intelligence, MCP tooling, and conformance testing, with the research underneath. Independent, evidence-first.

**My work is used by 120+ repositories across 60+ organizations, with nearly 1 million downloads**, including Google's Chrome DevTools MCP, Opera, Apereo CAS, Camunda and Flipt.

---

### New book: Building AI Agents in Go

<a href="https://golang-agents.com"><img src="https://golang-agents.com/og-v2.jpg" width="75%" alt="Building AI Agents in Go"></a>

Learn how AI agents work by building one in Go, from the first request to production, using the standard library. 17 chapters, 776 pages: the agent loop, tool calling, context, streaming, MCP, evals across models, sandboxing and prompt-injection defenses, and crash-safe runs that never repeat an action. Every example runs offline with no API key.

[Book](https://golang-agents.com) · [Free sample (27 pages)](https://golang-agents.com/sample/building-ai-agents-in-go-sample-light.pdf) · [Code](https://github.com/blackwell-systems/go-agents-book-code)

### GCF (Graph Compact Format)

<a href="https://github.com/blackwell-systems/gcf"><img src="https://raw.githubusercontent.com/blackwell-systems/gcf/main/assets/gcf-hero-wire-delta.png" width="75%" alt="GCF"></a>

The AI-native wire format for structured data. 100% comprehension on every frontier model. 50-92% fewer tokens than JSON. 2,500+ LLM evaluations across 11 models and 4 providers. 43B+ lossless round-trips across 5 formats. Used by 28 projects outside Blackwell Systems, with 580K+ downloads, including Chrome DevTools MCP, Opera and OmniRoute (77K stars), where GCF's encoder is vendored in, so the 10,000+ OmniRoute forks made since carry it too, plus 50+ standalone projects built from OmniRoute's code. Zero training required.

[![Spec](https://img.shields.io/badge/spec-gcformat.com-6fa2c9?style=for-the-badge)](https://gcformat.com)
[![Benchmarks](https://img.shields.io/badge/benchmarks-2%2C500%2B%20evals-22c55e?style=for-the-badge)](https://gcformat.com/guide/benchmarks.html)
[![Playground](https://img.shields.io/badge/playground-live-6fa2c9?style=for-the-badge)](https://gcformat.com/playground.html)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20579817-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20579817)

[Spec](https://github.com/blackwell-systems/gcf) ·
[Go](https://github.com/blackwell-systems/gcf-go) ·
[TypeScript](https://github.com/blackwell-systems/gcf-typescript) ·
[Python](https://github.com/blackwell-systems/gcf-python) ·
[Rust](https://github.com/blackwell-systems/gcf-rust) ·
[Swift](https://github.com/blackwell-systems/gcf-swift) ·
[Kotlin](https://github.com/blackwell-systems/gcf-kotlin) ·
[.NET](https://github.com/blackwell-systems/gcf-dotnet) ·
[Proxy](https://github.com/blackwell-systems/gcf-proxy) ·
[Tree-sitter](https://github.com/blackwell-systems/tree-sitter-gcf)

### bide

<a href="https://github.com/bide-ai/bide"><img src="https://raw.githubusercontent.com/bide-ai/bide/main/assets/bide-social.png" width="50%" alt="bide"></a>

A full framework for building AI agents in Go: models (OpenAI, Anthropic, Gemini), tools, typed multi-step flows, memory and RAG, MCP, multi-agent coordination, and typed human-in-the-loop, all on one durable, append-only journal. The journal is the difference: side effects fire at most once (a resumed run never re-charges a card or re-sends an email), thousands of concurrent runs survive crashes and node handoffs in a single process with no cluster, every run emits a cryptographically verifiable audit trail (RFC 6962 Merkle proofs, checkable without trusting the vendor), and shared governed state is provably convergent. Built for ambient agents that run unattended and act under audit.

[![CI](https://img.shields.io/github/actions/workflow/status/bide-ai/bide/ci.yml?style=for-the-badge&label=CI)](https://github.com/bide-ai/bide/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue?style=for-the-badge)](https://github.com/bide-ai/bide/blob/main/LICENSE)
[![Go](https://img.shields.io/badge/Go-1.27-00ADD8?style=for-the-badge&logo=go)](https://go.dev)
[![Status](https://img.shields.io/badge/status-working%20v0-22c55e?style=for-the-badge)](https://github.com/bide-ai/bide)

[Getting started](https://github.com/bide-ai/bide/blob/main/docs/getting-started.md) ·
[Concepts](https://github.com/bide-ai/bide/blob/main/docs/CONCEPTS.md) ·
[Flows](https://github.com/bide-ai/bide/blob/main/docs/guides/flows.md) ·
[Governance](https://github.com/bide-ai/bide/blob/main/docs/guides/governance.md) ·
[Audit](https://github.com/bide-ai/bide/blob/main/docs/guides/audit.md) ·
[Security model](https://github.com/bide-ai/bide/blob/main/docs/guides/security-model.md)

### agent-lsp

<a href="https://github.com/blackwell-systems/agent-lsp"><img src="https://raw.githubusercontent.com/blackwell-systems/agent-lsp/main/assets/social-preview.png" width="50%" alt="agent-lsp"></a>

Code intelligence infrastructure for AI agents. 65 tools, 30 CI-verified languages, 24 agent workflows. Single Go binary. Uses GCF as default output format. Used by 41 repositories across 25 organizations.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/agent-lsp?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/agent-lsp/blob/main/LICENSE)

### mcp-assert

<a href="https://github.com/blackwell-systems/mcp-assert"><img src="https://raw.githubusercontent.com/blackwell-systems/mcp-assert/main/assets/social-preview.png" width="50%" alt="mcp-assert"></a>

Conformance testing for MCP servers. 102 servers scanned, 34 bugs found, 12 upstream issues filed. Fuzz testing, schema linting, per-assertion Docker isolation. Runs in CI across 39 of WYRE's MCP server repos. 55K+ downloads.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/mcp-assert?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/mcp-assert/blob/main/LICENSE)

### knowing

<a href="https://github.com/blackwell-systems/knowing"><img src="https://raw.githubusercontent.com/blackwell-systems/knowing/main/assets/knowing-social-preview.jpg" width="50%" alt="knowing"></a>

Self-adapting code intelligence engine. The system GCF was extracted from. 28 MCP tools, graph-native analysis, session deduplication.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/knowing?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/knowing/blob/main/LICENSE)

### polywave

<a href="https://github.com/blackwell-systems/polywave"><img src="https://raw.githubusercontent.com/blackwell-systems/polywave/main/assets/social-preview.png" width="50%" alt="polywave"></a>

Parallel AI agent coordination. Disjoint file ownership, git worktree isolation, tier-gated execution, and human-reviewed plans. A Scout agent maps the codebase into a coordination plan; Wave agents implement their assigned files simultaneously.

[![Shell](https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)](https://github.com/blackwell-systems/polywave)

[Protocol](https://github.com/blackwell-systems/polywave-protocol) ·
[Claude Code](https://github.com/blackwell-systems/polywave) ·
[Codex](https://github.com/blackwell-systems/polywave-codex) ·
[Go](https://github.com/blackwell-systems/polywave-go)

### goldenthread

<a href="https://github.com/blackwell-systems/goldenthread"><img src="https://raw.githubusercontent.com/blackwell-systems/goldenthread/main/asset-banner-social.jpg" width="50%" alt="goldenthread"></a>

Go structs to TypeScript and Zod, one source of truth. Discriminated unions, enums, maps, and validation rules compile to runtime-checked Zod schemas; opt-in json-tag inference bridges plain types. Built for Wails and web frontends. Apache-2.0.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-6fa2c9?style=for-the-badge)](https://github.com/blackwell-systems/goldenthread)

### GCP Emulator Suite

Local implementations of Google Cloud APIs for development and CI. No GCP credentials required. Used by 10 projects, including Apereo CAS, Flipt and Camunda.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/license-Apache--2.0-6fa2c9?style=for-the-badge)](https://github.com/blackwell-systems/gcp-secret-manager-emulator/blob/main/LICENSE)

[Secret Manager](https://github.com/blackwell-systems/gcp-secret-manager-emulator) (275K+ downloads) ·
[KMS](https://github.com/blackwell-systems/gcp-kms-emulator) ·
[IAM](https://github.com/blackwell-systems/gcp-iam-emulator) ·
[Eventarc](https://github.com/blackwell-systems/gcp-eventarc-emulator) ·
[Auth](https://github.com/blackwell-systems/gcp-emulator-auth) ·
[IAM Control Plane](https://github.com/blackwell-systems/gcp-iam-control-plane) ·
[Core](https://github.com/blackwell-systems/gcp-emulator)

---

### Research

11 self-published papers (Zenodo DOIs), several with industry response. A research program on tokenizer-attention coupling proving that BPE merge decisions permanently constrain transformer attention capacity, plus systems work on distributed convergence and memory reclamation.

**Tokenizer-Attention Coupling** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20925910-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20925910)
How BPE merge decisions permanently shape transformer internal organization. 43 tokenizers, 20 providers. Controlled experiment: identical models, different tokenizer. Merge barriers produce 3-738x better structured data comprehension, zero natural language cost. 18-phase causal ablation across 2 architectures, 2 scales, 3 domains.

**Stranded Attention** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21158886-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21158886)
A previously undescribed failure mode: every attention head in a standard BPE model has structural capacity the tokenizer permanently prevents. All 384 heads at 410M and 768 at 1.3B show 4x more delimiter attention under clean boundaries. The 40pp frustration gap appears by step 5,000 and never closes.

**Developmental Atlas of Attention Head Specialization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21205389-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21205389)
First head-specialization atlas at scale: 384 heads, 7 behaviors, 131 checkpoints, 7 runs, 2 architectures. The BPE capacity tax is architecture-independent (+64.3% NeoX, +67.0% Llama). 48-56% of attention capacity in standard BPE is non-productive.

**Structural Ambiguity in JSON Tokenization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20810588-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20810588)
Cross-tokenizer analysis across 8 tokenizers, 6 providers. JSON field names fuse with the opening quote on 50-63% of tokenizers. JSON boundary merge rate 8.93% vs 1.00% for pipe; TOON tab 59.82%. JSON overhead reaches 81% at 500 rows.

**Graph Compact Format (GCF)** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20579817-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20579817)
The AI-native wire format for structured data. 2,500+ evaluations across 11 models and 4 providers. 43B+ lossless round-trips. Used by 28 projects outside Blackwell Systems. 580K+ downloads. Spec v3.6.0 Stable.
[Explore the project](https://github.com/blackwell-systems/gcf)

**The Hierarchical Identity Architecture** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20342255-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20342255)
Content-addressing as a computation primitive for software relationship intelligence. 2.75x more precise than GitNexus (p=0.0003), 193x faster indexing on enterprise repos.
[Explore the project](https://github.com/blackwell-systems/knowing) · [merkle-strata](https://github.com/blackwell-systems/merkle-strata)

**Memory Drainability** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18653776-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18653776)
Formalizes when coarse-grained allocators can reclaim memory. Proves a sharp O(1) vs Ω(t) dichotomy for bounded retention. Validated empirically (238x recycle-rate differential).
[Explore the project](https://github.com/blackwell-systems/drainability)

**Normalization Confluence: An Exact, Mechanized Theory of When Repair Can Replace Commutativity** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23311489-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.23311489)
When can repair replace commutativity? Exact conditions at three scales with a proved hierarchy, organized by a three-layer framework into a 60-regime atlas. Tested where it could fail: Dijkstra's self-stabilization and invariant confluence recovered with the framework frozen, and two preregistered predictions confirmed, one on CouchDB/PouchDB replication (reported upstream). 4,797 results machine-checked in Coq, no axioms.
[Explore the project](https://github.com/blackwell-systems/normalization-confluence) · [Site](https://blackwell-systems.github.io/normalization-confluence/) · [Engineer's guide](https://blackwell-systems.github.io/normalization-confluence/guide/)

**Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18671870-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18671870)
Coordination-free convergence via well-founded compensation. A third convergence regime alongside CRDTs and invariant confluence: operations may conflict and break invariants, and with a terminating repair, replicas converge exactly when two checkable conditions hold.
[Explore the project](https://github.com/blackwell-systems/normalization-confluence)

**Federated Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18677400-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18677400)
Multi-organizational convergence through morphism validity preservation over acyclic networks.

**The Categorical Structure of Federated Convergence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23311468-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.23311468)
A federation's consistent states as a finite limit, gluing over sub-federations, and the obstruction on cycles as holonomy. The exact minimum coordination is NP-hard and fixed-parameter tractable in the size of the coordinated core. Structural results mechanized in Coq.

---

### Upstream Contributions

50+ merged PRs across 30+ organizations. Top-10 contributor to [mcp-go](https://github.com/mark3labs/mcp-go) (9.2K stars).
Data corruption fixes, panic recovery, SDK hardening, spec compliance, transport bugs.

| Organization | What | Stars |
|:---|:---|---:|
| **Google** | Chrome DevTools MCP (GCF format), go-containerregistry | 54K |
| **Anthropic** | MCP Go, Python, PHP SDKs + servers | 85K+ |
| **LangChain** | langchain (text splitter fix) | 136K |
| **etcd** | CNCF gRPC error code fix (in review) | 51K |
| **Charmbracelet** | bubbletea, huh (in review) | 42K |
| **GitHub** | github-mcp-server | 16K |
| **HashiCorp** | terraform-provider-aws (GovCloud fix) | 10.9K |
| **pypa** | pip (locale encoding fix) | 10.2K |
| **mark3labs** | mcp-go SDK (9 PRs, top-10 contributor) | 9.2K |
| **Ant Group** | mcp-server-chart (9 bug fixes) | 4K |
| **Grafana** | mcp-grafana (3 PRs merged) | 2.9K |
| **Apache** | CouchDB (replication bug, diagnosed; fixed upstream) | 7K |

[Full list](https://blog.blackwell-systems.com/oss#upstream-contributions)

---

### Technical Background

Languages:

![C](https://img.shields.io/badge/Systems_Programming-292c34?logo=c&logoColor=white&labelColor=1a1d22&style=for-the-badge)
![Go](https://img.shields.io/badge/Go-%F0%9F%90%B9-292c34?logo=go&logoColor=white&style=for-the-badge)
![Rust](https://img.shields.io/badge/Rust-%F0%9F%A6%80-292c34?logo=rust&logoColor=white&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-%F0%9F%90%8D-292c34?logo=python&logoColor=ffdd54&style=for-the-badge)
![Java](https://img.shields.io/badge/Java-%E2%98%95-292c34?logo=openjdk&logoColor=white&style=for-the-badge)
![Node.js](https://img.shields.io/badge/Node.js-292c34?logo=nodedotjs&logoColor=white&style=for-the-badge)

Platforms & Shells:

![Platform](https://img.shields.io/badge/Platform-%F0%9F%8D%8E%20macOS%20%7C%20%F0%9F%90%A7%20Linux%20%7C%20%F0%9F%AA%9F%20WSL-292c34?style=for-the-badge)
![Zsh](https://img.shields.io/badge/Zsh-292c34?logo=zsh&logoColor=white&style=for-the-badge)
![Bash](https://img.shields.io/badge/Bash-292c34?logo=gnubash&logoColor=white&style=for-the-badge)
![PowerShell](https://img.shields.io/badge/PowerShell-6b7280?logo=powershell&logoColor=white&style=for-the-badge)

Developer Tooling:

![Git](https://img.shields.io/badge/Git-%F0%9F%94%A7-292c34?logo=git&logoColor=6fa2c9&style=for-the-badge)
![Terraform](https://img.shields.io/badge/Terraform-292c34?logo=terraform&logoColor=6fa2c9&style=for-the-badge)
![AWS%20CDK](https://img.shields.io/badge/AWS%20CDK-292c34?logo=amazonaws&logoColor=6fa2c9&style=for-the-badge)
![Datadog](https://img.shields.io/badge/Datadog-292c34?logo=datadog&logoColor=6fa2c9&style=for-the-badge)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-292c34?logo=opentelemetry&logoColor=6fa2c9&style=for-the-badge)
![Containers](https://img.shields.io/badge/Containers-%F0%9F%90%B3%20Docker-292c34?logo=docker&logoColor=6fa2c9&style=for-the-badge)
![GCP](https://img.shields.io/badge/Google%20Cloud-292c34?logo=googlecloud&logoColor=6fa2c9&style=for-the-badge)

Artificial Intelligence:

[![GPT](https://img.shields.io/badge/GPT-%F0%9F%A4%96%20OpenAI-292c34?logo=openai&logoColor=6fa2c9&style=for-the-badge)](https://openai.com/)
[![Claude](https://img.shields.io/badge/Claude-%F0%9F%A7%A0%20Anthropic-292c34?logo=anthropic&logoColor=6fa2c9&style=for-the-badge)](https://www.anthropic.com/)
[![Gemini](https://img.shields.io/badge/Gemini-%E2%9C%A8%20Google-292c34?logo=googlegemini&logoColor=6fa2c9&style=for-the-badge)](https://deepmind.google/technologies/gemini/)
