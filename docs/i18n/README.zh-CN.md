[English](../../README.md) · **简体中文** · [Русский](README.ru.md) · [हिन्दी](README.hi.md)

[![Blackwell Systems™](https://raw.githubusercontent.com/blackwell-systems/blackwell-docs-theme/main/badge-trademark.svg)](https://github.com/blackwell-systems) [![Stars](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/blackwell-systems/blackwell-systems/main/stars-badge.json)](https://github.com/blackwell-systems)

## Blackwell Systems：构建智能体技术栈，发布可验证的证据

创始人：Dayna Blackwell。我构建智能体 AI 技术栈赖以运行的开放基础设施，并交付支撑它的证据：持久化智能体、线路格式、代码智能、MCP 工具链以及一致性测试，其背后皆有研究支撑。独立，证据优先。

---

### GCF（Graph Compact Format）

<a href="https://github.com/blackwell-systems/gcf"><img src="https://raw.githubusercontent.com/blackwell-systems/gcf/main/assets/gcf-hero-wire-delta.png" width="75%" alt="GCF"></a>

面向 AI 原生的结构化数据线路格式。在每一款前沿模型上实现 100% 的理解率。相较 JSON 减少 50-92% 的 token。跨 11 个模型、4 家提供商的 2,500+ 次 LLM 评测。跨 5 种格式的 43B+ 次无损往返。已在 20 个生产系统中部署，包括 Chrome DevTools MCP。无需任何训练。

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

用 Go 构建 AI 智能体的完整框架：模型（OpenAI、Anthropic、Gemini）、工具、类型化多步流程、记忆与 RAG、MCP、多智能体协调，以及类型化的人在回路，全部构建于同一个持久化、仅追加的日志之上。这份日志正是关键所在：副作用至多触发一次（恢复的运行绝不会重复扣款或重复发送邮件），数以千计的并发运行可在单个进程中挺过崩溃与节点交接，无需集群，每次运行都会产出可通过密码学验证的审计追踪（RFC 6962 Merkle 证明，无需信任供应商即可校验），共享的受治理状态可被证明是收敛的。为无人值守运行并在审计下行动的环境智能体而生。

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

面向 AI 智能体的代码智能基础设施。65 个工具，30 种经 CI 验证的语言，24 个智能体工作流。单个 Go 二进制文件。默认使用 GCF 作为输出格式。

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/agent-lsp?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/agent-lsp/blob/main/LICENSE)

### mcp-assert

<a href="https://github.com/blackwell-systems/mcp-assert"><img src="https://raw.githubusercontent.com/blackwell-systems/mcp-assert/main/assets/social-preview.png" width="50%" alt="mcp-assert"></a>

面向 MCP 服务器的一致性测试。已扫描 102 个服务器，发现 34 个缺陷，向上游提交 12 个问题。模糊测试、模式检查，以及每断言级别的 Docker 隔离。

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/mcp-assert?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/mcp-assert/blob/main/LICENSE)

### knowing

<a href="https://github.com/blackwell-systems/knowing"><img src="https://raw.githubusercontent.com/blackwell-systems/knowing/main/assets/knowing-social-preview.jpg" width="50%" alt="knowing"></a>

自适应的代码智能引擎。GCF 正是从这套系统中提取而来。28 个 MCP 工具，图原生分析，会话去重。

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/knowing?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/knowing/blob/main/LICENSE)

### polywave

<a href="https://github.com/blackwell-systems/polywave"><img src="https://raw.githubusercontent.com/blackwell-systems/polywave/main/assets/social-preview.png" width="50%" alt="polywave"></a>

并行 AI 智能体协调。互不相交的文件所有权、git worktree 隔离、分层门控执行，以及经人工评审的方案。Scout 智能体将代码库映射为一份协调方案；Wave 智能体同时实现各自分配到的文件。

[![Shell](https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)](https://github.com/blackwell-systems/polywave)

[Protocol](https://github.com/blackwell-systems/polywave-protocol) ·
[Claude Code](https://github.com/blackwell-systems/polywave) ·
[Codex](https://github.com/blackwell-systems/polywave-codex) ·
[Go](https://github.com/blackwell-systems/polywave-go)

### goldenthread

<a href="https://github.com/blackwell-systems/goldenthread"><img src="https://raw.githubusercontent.com/blackwell-systems/goldenthread/main/asset-banner-social.jpg" width="50%" alt="goldenthread"></a>

将 Go 结构体转为 TypeScript 与 Zod，单一事实来源。可区分联合类型、枚举、映射与校验规则会编译为运行时校验的 Zod 模式；可选启用的 json-tag 推断可桥接普通类型。为 Wails 与 Web 前端而生。Apache-2.0。

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-6fa2c9?style=for-the-badge)](https://github.com/blackwell-systems/goldenthread)

### GCP Emulator Suite

面向开发与 CI 的 Google Cloud API 本地实现。无需任何 GCP 凭据。

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/license-Apache--2.0-6fa2c9?style=for-the-badge)](https://github.com/blackwell-systems/gcp-secret-manager-emulator/blob/main/LICENSE)

[Secret Manager](https://github.com/blackwell-systems/gcp-secret-manager-emulator)（50K+ 次下载）·
[KMS](https://github.com/blackwell-systems/gcp-kms-emulator) ·
[IAM](https://github.com/blackwell-systems/gcp-iam-emulator) ·
[Eventarc](https://github.com/blackwell-systems/gcp-eventarc-emulator) ·
[Auth](https://github.com/blackwell-systems/gcp-emulator-auth) ·
[IAM Control Plane](https://github.com/blackwell-systems/gcp-iam-control-plane) ·
[Core](https://github.com/blackwell-systems/gcp-emulator)

---

### 研究

9 篇自主发表的论文（Zenodo DOI），其中数篇已获得业界回应。一项关于 tokenizer 与注意力耦合的研究计划，证明了 BPE 合并决策会永久性地约束 transformer 的注意力容量，另有关于分布式收敛与内存回收的系统性工作。

**Tokenizer-Attention Coupling** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20925910-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20925910)
BPE 合并决策如何永久性地塑造 transformer 的内部组织。43 个 tokenizer，20 家提供商。受控实验：相同模型，不同 tokenizer。合并屏障带来 3-738 倍更强的结构化数据理解能力，且自然语言方面零代价。跨 2 种架构、2 种规模、3 个领域的 18 阶段因果消融。

**Stranded Attention** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21158886-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21158886)
一种此前未被描述的失效模式：标准 BPE 模型中的每一个注意力头都拥有被 tokenizer 永久阻断的结构性容量。在 410M 规模下的全部 384 个头以及 1.3B 规模下的 768 个头，在边界清晰的情况下均显示出 4 倍的分隔符注意力。40pp 的挫败差距在第 5,000 步时便已出现，且永不闭合。

**Developmental Atlas of Attention Head Specialization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21205389-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21205389)
首份大规模的注意力头专门化图谱：384 个头，7 种行为，131 个检查点，7 次运行，2 种架构。BPE 容量税与架构无关（NeoX +64.3%，Llama +67.0%）。标准 BPE 中 48-56% 的注意力容量无实际产出。

**Structural Ambiguity in JSON Tokenization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20810588-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20810588)
跨 8 个 tokenizer、6 家提供商的分析。JSON 字段名在 50-63% 的 tokenizer 上会与起始引号融合。JSON 边界合并率为 8.93%，而竖线为 1.00%；TOON 制表符为 59.82%。在 500 行时，JSON 开销高达 81%。

**Graph Compact Format (GCF)** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20579817-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20579817)
面向 AI 原生的结构化数据线路格式。跨 11 个模型、4 家提供商的 2,500+ 次评测。43B+ 次无损往返。已在 20 个生产系统中部署。Spec v3.5.1 Stable。
[Explore the project](https://github.com/blackwell-systems/gcf)

**The Hierarchical Identity Architecture** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20342255-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20342255)
以内容寻址作为软件关系智能的计算原语。比 GitNexus 精确 2.75 倍（p=0.0003），在企业级仓库上的索引速度快 193 倍。
[Explore the project](https://github.com/blackwell-systems/knowing) · [merkle-strata](https://github.com/blackwell-systems/merkle-strata)

**Memory Drainability** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18653776-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18653776)
形式化了粗粒度分配器何时可回收内存。证明了有界保留下 O(1) 与 Ω(t) 之间的一道清晰分界。已经实证验证（238 倍的回收率差异）。
[Explore the project](https://github.com/blackwell-systems/drainability)

**Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18671870-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18671870)
通过良基补偿实现无需协调的收敛。继 CRDT 与不变量合流之后的第三种收敛范式。
[Explore the project](https://github.com/blackwell-systems/normalization-confluence)

**Federated Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18677400-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18677400)
在无环网络上通过态射有效性保持实现多组织收敛。

---

### 上游贡献

跨生态系统的 40+ 个已合并 PR。[mcp-go](https://github.com/mark3labs/mcp-go)（8.7K stars）的第 6 号贡献者。
数据损坏修复、panic 恢复、SDK 加固、规范合规、传输层缺陷修复。

| 组织 | 内容 | Stars |
|:---|:---|---:|
| **Google** | Chrome DevTools MCP（GCF 格式）、go-containerregistry | 47K |
| **Anthropic** | MCP Go、Python、PHP SDK + 服务器 | 85K+ |
| **LangChain** | langchain（文本分割器修复） | 136K |
| **etcd** | CNCF gRPC 错误码修复（审查中） | 51K |
| **Charmbracelet** | bubbletea、huh | 42K |
| **GitHub** | github-mcp-server | 16K |
| **HashiCorp** | terraform-provider-aws（GovCloud 修复） | 10.9K |
| **pypa** | pip（区域设置编码修复） | 10.2K |
| **mark3labs** | mcp-go SDK（9 个 PR，第 6 号贡献者） | 8.7K |
| **Ant Group** | mcp-server-chart（9 个缺陷修复） | 4K |
| **Grafana** | mcp-grafana（3 个已合并 PR） | 2.9K |

[Full list](https://blog.blackwell-systems.com/oss#upstream-contributions)

---

### 技术背景

语言：

![C](https://img.shields.io/badge/Systems_Programming-292c34?logo=c&logoColor=white&labelColor=1a1d22&style=for-the-badge)
![Go](https://img.shields.io/badge/Go-%F0%9F%90%B9-292c34?logo=go&logoColor=white&style=for-the-badge)
![Rust](https://img.shields.io/badge/Rust-%F0%9F%A6%80-292c34?logo=rust&logoColor=white&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-%F0%9F%90%8D-292c34?logo=python&logoColor=ffdd54&style=for-the-badge)
![Java](https://img.shields.io/badge/Java-%E2%98%95-292c34?logo=openjdk&logoColor=white&style=for-the-badge)
![Node.js](https://img.shields.io/badge/Node.js-292c34?logo=nodedotjs&logoColor=white&style=for-the-badge)

平台与 Shell：

![Platform](https://img.shields.io/badge/Platform-%F0%9F%8D%8E%20macOS%20%7C%20%F0%9F%90%A7%20Linux%20%7C%20%F0%9F%AA%9F%20WSL-292c34?style=for-the-badge)
![Zsh](https://img.shields.io/badge/Zsh-292c34?logo=zsh&logoColor=white&style=for-the-badge)
![Bash](https://img.shields.io/badge/Bash-292c34?logo=gnubash&logoColor=white&style=for-the-badge)
![PowerShell](https://img.shields.io/badge/PowerShell-6b7280?logo=powershell&logoColor=white&style=for-the-badge)

开发者工具：

![Git](https://img.shields.io/badge/Git-%F0%9F%94%A7-292c34?logo=git&logoColor=6fa2c9&style=for-the-badge)
![Terraform](https://img.shields.io/badge/Terraform-292c34?logo=terraform&logoColor=6fa2c9&style=for-the-badge)
![AWS%20CDK](https://img.shields.io/badge/AWS%20CDK-292c34?logo=amazonaws&logoColor=6fa2c9&style=for-the-badge)
![Datadog](https://img.shields.io/badge/Datadog-292c34?logo=datadog&logoColor=6fa2c9&style=for-the-badge)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-292c34?logo=opentelemetry&logoColor=6fa2c9&style=for-the-badge)
![Containers](https://img.shields.io/badge/Containers-%F0%9F%90%B3%20Docker-292c34?logo=docker&logoColor=6fa2c9&style=for-the-badge)
![GCP](https://img.shields.io/badge/Google%20Cloud-292c34?logo=googlecloud&logoColor=6fa2c9&style=for-the-badge)

人工智能：

[![GPT](https://img.shields.io/badge/GPT-%F0%9F%A4%96%20OpenAI-292c34?logo=openai&logoColor=6fa2c9&style=for-the-badge)](https://openai.com/)
[![Claude](https://img.shields.io/badge/Claude-%F0%9F%A7%A0%20Anthropic-292c34?logo=anthropic&logoColor=6fa2c9&style=for-the-badge)](https://www.anthropic.com/)
[![Gemini](https://img.shields.io/badge/Gemini-%E2%9C%A8%20Google-292c34?logo=googlegemini&logoColor=6fa2c9&style=for-the-badge)](https://deepmind.google/technologies/gemini/)
