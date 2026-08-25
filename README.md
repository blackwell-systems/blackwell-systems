[![Blackwell Systems™](https://raw.githubusercontent.com/blackwell-systems/blackwell-docs-theme/main/badge-trademark.svg)](https://github.com/blackwell-systems) [![Stars](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/blackwell-systems/blackwell-systems/main/stars-badge.json)](https://github.com/blackwell-systems)

## AI Infrastructure & Systems Engineering

Building tools for the agentic AI stack. Wire formats, code intelligence, MCP infrastructure, conformance testing.

---

### GCF (Graph Compact Format)

<a href="https://github.com/blackwell-systems/gcf"><img src="https://raw.githubusercontent.com/blackwell-systems/gcf/main/assets/gcf-hero-wire-delta.png" width="75%" alt="GCF"></a>

The AI-native wire format for structured data. 100% comprehension on every frontier model. 50-92% fewer tokens than JSON. 2,500+ LLM evaluations across 11 models and 4 providers. 43B+ lossless round-trips across 5 formats. Deployed in 18 production systems including Chrome DevTools MCP. Zero training required.

[![Spec](https://img.shields.io/badge/spec-gcformat.com-2563eb?style=for-the-badge)](https://gcformat.com)
[![Benchmarks](https://img.shields.io/badge/benchmarks-2%2C400%2B%20evals-22c55e?style=for-the-badge)](https://gcformat.com/guide/benchmarks.html)
[![Playground](https://img.shields.io/badge/playground-live-2563eb?style=for-the-badge)](https://gcformat.com/playground.html)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20579817-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20579817)

[Spec](https://github.com/blackwell-systems/gcf) ·
[Go](https://github.com/blackwell-systems/gcf-go) ·
[TypeScript](https://github.com/blackwell-systems/gcf-typescript) ·
[Python](https://github.com/blackwell-systems/gcf-python) ·
[Rust](https://github.com/blackwell-systems/gcf-rust) ·
[Swift](https://github.com/blackwell-systems/gcf-swift) ·
[Kotlin](https://github.com/blackwell-systems/gcf-kotlin) ·
[Proxy](https://github.com/blackwell-systems/gcf-proxy) ·
[Tree-sitter](https://github.com/blackwell-systems/tree-sitter-gcf)

### agent-lsp

<a href="https://github.com/blackwell-systems/agent-lsp"><img src="https://raw.githubusercontent.com/blackwell-systems/agent-lsp/main/assets/social-preview.png" width="50%" alt="agent-lsp"></a>

Code intelligence infrastructure for AI agents. 65 tools, 30 CI-verified languages, 24 agent workflows. Single Go binary. Uses GCF as default output format.

### mcp-assert

<a href="https://github.com/blackwell-systems/mcp-assert"><img src="https://raw.githubusercontent.com/blackwell-systems/mcp-assert/main/assets/social-preview.png" width="50%" alt="mcp-assert"></a>

Conformance testing for MCP servers. 102 servers scanned, 34 bugs found, 12 upstream issues filed. Fuzz testing, schema linting, per-assertion Docker isolation.

### knowing

<a href="https://github.com/blackwell-systems/knowing"><img src="https://raw.githubusercontent.com/blackwell-systems/knowing/main/assets/knowing-social-preview.jpg" width="50%" alt="knowing"></a>

Self-adapting code intelligence engine. The system GCF was extracted from. 28 MCP tools, graph-native analysis, session deduplication.

### polywave

<a href="https://github.com/blackwell-systems/polywave"><img src="https://raw.githubusercontent.com/blackwell-systems/polywave/main/assets/social-preview.png" width="50%" alt="polywave"></a>

Parallel AI agent coordination. Disjoint file ownership, git worktree isolation, tier-gated execution, and human-reviewed plans. A Scout agent maps the codebase into a coordination plan; Wave agents implement their assigned files simultaneously.

[Protocol](https://github.com/blackwell-systems/polywave-protocol) ·
[Claude Code](https://github.com/blackwell-systems/polywave) ·
[Codex](https://github.com/blackwell-systems/polywave-codex) ·
[Go](https://github.com/blackwell-systems/polywave-go)

### GCP Emulator Suite

Local implementations of Google Cloud APIs for development and CI. No GCP credentials required.

[Secret Manager](https://github.com/blackwell-systems/gcp-secret-manager-emulator) (50K+ downloads) ·
[KMS](https://github.com/blackwell-systems/gcp-kms-emulator) ·
[IAM](https://github.com/blackwell-systems/gcp-iam-emulator) ·
[Eventarc](https://github.com/blackwell-systems/gcp-eventarc-emulator) ·
[Auth](https://github.com/blackwell-systems/gcp-emulator-auth) ·
[IAM Control Plane](https://github.com/blackwell-systems/gcp-iam-control-plane) ·
[Core](https://github.com/blackwell-systems/gcp-emulator)

---

### Research

9 published papers. A research program on tokenizer-attention coupling proving that BPE merge decisions permanently constrain transformer attention capacity, plus systems work on distributed convergence and memory reclamation.

**Tokenizer-Attention Coupling** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20925910-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20925910)
How BPE merge decisions permanently shape transformer internal organization. 43 tokenizers, 20 providers. Controlled experiment: identical models, different tokenizer. Merge barriers produce 3-738x better structured data comprehension, zero natural language cost. 18-phase causal ablation across 2 architectures, 2 scales, 3 domains.

**Stranded Attention** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21158886-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21158886)
A previously undescribed failure mode: every attention head in a standard BPE model has structural capacity the tokenizer permanently prevents. All 384 heads at 410M and 768 at 1.3B show 4x more delimiter attention under clean boundaries. The 40pp frustration gap appears by step 5,000 and never closes.

**Developmental Atlas of Attention Head Specialization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21205389-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21205389)
First head-specialization atlas at scale: 384 heads, 7 behaviors, 131 checkpoints, 7 runs, 2 architectures. The BPE capacity tax is architecture-independent (+64.3% NeoX, +67.0% Llama). 48-56% of attention capacity in standard BPE is non-productive.

**Structural Ambiguity in JSON Tokenization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20810588-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20810588)
Cross-tokenizer analysis across 8 tokenizers, 6 providers. JSON field names fuse with the opening quote on 50-63% of tokenizers. JSON boundary merge rate 8.93% vs 1.00% for pipe; TOON tab 59.82%. JSON overhead reaches 81% at 500 rows.

**Graph Compact Format (GCF)** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20579817-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20579817)
The AI-native wire format for structured data. 2,500+ evaluations across 11 models and 4 providers. 43B+ lossless round-trips. Deployed in 18 production systems. Spec v3.5.1 Stable.
[Explore the project](https://github.com/blackwell-systems/gcf)

**The Hierarchical Identity Architecture** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20342255-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20342255)
Content-addressing as a computation primitive for software relationship intelligence. 2.75x more precise than GitNexus (p=0.0003), 193x faster indexing on enterprise repos.
[Explore the project](https://github.com/blackwell-systems/knowing) · [merkle-strata](https://github.com/blackwell-systems/merkle-strata)

**Memory Drainability** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18653776-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18653776)
Formalizes when coarse-grained allocators can reclaim memory. Proves a sharp O(1) vs Ω(t) dichotomy for bounded retention. Validated empirically (238x recycle-rate differential).
[Explore the project](https://github.com/blackwell-systems/drainability)

**Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18671870-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18671870)
Coordination-free convergence via well-founded compensation. Third convergence regime alongside CRDTs and invariant confluence.
[Explore the project](https://github.com/blackwell-systems/normalization-confluence)

**Federated Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18677400-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18677400)
Multi-organizational convergence through morphism validity preservation over acyclic networks.

---

### Upstream Contributions

33 merged PRs across 32 organizations. #6 contributor to [mcp-go](https://github.com/mark3labs/mcp-go) (8.7K stars).
Data corruption fixes, panic recovery, SDK hardening, spec compliance, transport bugs.

| Organization | What | Stars |
|:---|:---|---:|
| **Google** | Chrome DevTools MCP (GCF format), go-containerregistry | 47K |
| **Anthropic** | MCP Go, Python, PHP SDKs + servers | 85K+ |
| **LangChain** | langchain (text splitter fix) | 136K |
| **etcd** | CNCF (gRPC error code fix) | 51K |
| **Charmbracelet** | bubbletea, huh | 42K |
| **GitHub** | github-mcp-server | 16K |
| **HashiCorp** | terraform-provider-aws (GovCloud fix) | 10.9K |
| **pypa** | pip (locale encoding fix) | 10.2K |
| **mark3labs** | mcp-go SDK (9 PRs, #6 contributor) | 8.7K |
| **Ant Group** | mcp-server-chart (9 bug fixes) | 4K |
| **Grafana** | mcp-grafana (3 PRs merged) | 2.9K |

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

![Git](https://img.shields.io/badge/Git-%F0%9F%94%A7-292c34?logo=git&logoColor=f41c80&style=for-the-badge)
![Terraform](https://img.shields.io/badge/Terraform-292c34?logo=terraform&logoColor=f41c80&style=for-the-badge)
![AWS%20CDK](https://img.shields.io/badge/AWS%20CDK-292c34?logo=amazonaws&logoColor=f41c80&style=for-the-badge)
![Datadog](https://img.shields.io/badge/Datadog-292c34?logo=datadog&logoColor=f41c80&style=for-the-badge)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-292c34?logo=opentelemetry&logoColor=f41c80&style=for-the-badge)
![Containers](https://img.shields.io/badge/Containers-%F0%9F%90%B3%20Docker-292c34?logo=docker&logoColor=f41c80&style=for-the-badge)
![GCP](https://img.shields.io/badge/Google%20Cloud-292c34?logo=googlecloud&logoColor=f41c80&style=for-the-badge)

Artificial Intelligence:

[![GPT](https://img.shields.io/badge/GPT-%F0%9F%A4%96%20OpenAI-292c34?logo=openai&logoColor=f41c80&style=for-the-badge)](https://openai.com/)
[![Claude](https://img.shields.io/badge/Claude-%F0%9F%A7%A0%20Anthropic-292c34?logo=anthropic&logoColor=f41c80&style=for-the-badge)](https://www.anthropic.com/)
[![Gemini](https://img.shields.io/badge/Gemini-%E2%9C%A8%20Google-292c34?logo=googlegemini&logoColor=f41c80&style=for-the-badge)](https://deepmind.google/technologies/gemini/)
