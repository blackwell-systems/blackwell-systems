[![Blackwell Systems™](https://raw.githubusercontent.com/blackwell-systems/blackwell-docs-theme/main/badge-trademark.svg)](https://github.com/blackwell-systems) [![Stars](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/blackwell-systems/blackwell-systems/main/stars-badge.json)](https://github.com/blackwell-systems)

## AI Infrastructure & Systems Engineering

Building tools for the agentic AI stack. Wire formats, code intelligence, MCP infrastructure, conformance testing.

---

### GCF (Graph Compact Format)

<a href="https://github.com/blackwell-systems/gcf"><img src="https://raw.githubusercontent.com/blackwell-systems/gcf/main/assets/gcf-infographic.png" width="50%" alt="GCF"></a>

The AI-native wire format for structured data. 100% comprehension on every frontier model. 53-71% fewer tokens than JSON, 25.5% fewer than TOON. 1,700+ LLM evaluations across 10+ models and 3 providers. 23B+ lossless round-trips across 5 formats. Zero training required.

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

**Graph Compact Format (GCF)** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20579817-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20579817)
The AI-native wire format for structured data. 1,700+ evaluations across 10+ models and 3 providers. 23B+ lossless round-trips. Spec v3.1 Stable.
[Explore the project](https://github.com/blackwell-systems/gcf)

**The Hierarchical Identity Architecture** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20342254-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20342254)
Content-addressing as a computation primitive for software relationship intelligence.
[Explore the project](https://github.com/blackwell-systems/knowing) · [merkle-strata](https://github.com/blackwell-systems/merkle-strata)

**Memory Drainability** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18653776-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18653776)
Formalizes when coarse-grained allocators can reclaim memory. Validated on Redis: 50% key deletion freed 195K objects, reclaimed 0 slabs.
[Explore the project](https://github.com/blackwell-systems/drainability)

**Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18671870-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18671870)
Coordination-free convergence via well-founded compensation. Third convergence regime alongside CRDTs and invariant confluence.
[Explore the project](https://github.com/blackwell-systems/normalization-confluence)

**Federated Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18677400-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18677400)
Multi-organizational convergence through morphism validity preservation over acyclic networks.

---

### Upstream Contributions

27 merged PRs. #6 contributor to [mcp-go](https://github.com/mark3labs/mcp-go) (8.7K stars).
Data corruption fixes, panic recovery, SDK hardening, spec compliance, transport bugs.

| Organization | What | Stars |
|:---|:---|---:|
| **Anthropic** | MCP Go, Python, PHP SDKs + servers | 85K+ |
| **Google** | go-containerregistry (OCI artifact fix) | 3.8K |
| **GitHub** | github-mcp-server | 16K |
| **Grafana** | mcp-grafana (3 PRs merged) | 2.9K |
| **LangChain** | langchain (text splitter fix) | 136K |
| **Stretchr** | testify (suite panic fix) | 26K |
| **etcd** | CNCF (gRPC error code fix) | 51K |
| **Charmbracelet** | bubbletea, huh | 42K |
| **mark3labs** | mcp-go SDK (9 PRs, #6 contributor) | 8.7K |
| **Ant Group** | mcp-server-chart (9 bug fixes) | 4K |

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
