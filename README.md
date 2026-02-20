[![Blackwell Systems™](https://raw.githubusercontent.com/blackwell-systems/blackwell-docs-theme/main/badge-trademark.svg)](https://github.com/blackwell-systems)

## Systems Engineer & Researcher

**Currently:** Product engineering, backend systems, and cloud infrastructure  
**Focus:** Memory management, distributed systems, performance engineering  
**Building toward:** Deep systems work and research roles

## Featured Research

### Memory Drainability: Understanding Structural Memory Leaks
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18653776.svg)](https://doi.org/10.5281/zenodo.18653776)

Allocators using coarse-grained reclamation (slabs, arenas, epochs) can exhibit unbounded retention even when
all objects are freed. A single long-lived allocation pins an entire granule. This work formalizes when bounded
retention is possible and provides measurement tools validated on Redis, where deleting 50% of keys freed 195K
objects but reclaimed 0 slabs

**[→ Explore the project](https://github.com/blackwell-systems/drainability)**

**Components:** 
[Paper](https://doi.org/10.5281/zenodo.18653776) •
[Theory](https://github.com/blackwell-systems/drainability-framework) •
[Measurement](https://github.com/blackwell-systems/drainability-profiler) • [Reference
Implementation](https://github.com/blackwell-systems/temporal-slab) •
[Validation](https://github.com/blackwell-systems/redis-drainprof) 

### Normalization Confluence: Coordination-Free Convergence with Compensation
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18671870.svg)](https://doi.org/10.5281/zenodo.18671870)  

Event-driven systems can converge without coordination even when operations violate invariants and don't
commute—if compensation is well-founded and commutative. This work identifies a third convergence regime
alongside CRDTs and invariant confluence, where compensated results commute even though operations don't.

### Federated Normalization Confluence: Multi-Organizational Convergence
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18677400.svg)](https://doi.org/10.5281/zenodo.18677400)

Extends normalization confluence to federated environments where multiple registries are connected by morphisms
encoding cross-organizational constraints. For tree-shaped networks, proves federated convergence requires only
morphism validity preservation—all other conditions derive from network acyclicity via an authority argument

**[→ Explore the project](https://github.com/blackwell-systems/semantic-eventual-consistency)**

- **Single-registry:** WFC + CC conditions guarantee convergence for registry-governed streams
- **Federated extension:** Authority argument proves tree-shaped networks require only morphism validity
preservation
- Build-time verification tools (`gsm`, `nccheck`) with exhaustive state-space enumeration

**Components:** [Core Paper](https://doi.org/10.5281/zenodo.18671870) • [Federated
Paper](https://doi.org/10.5281/zenodo.18677400) • [gsm Library](https://github.com/blackwell-systems/gsm) •
[nccheck Verifier](https://github.com/blackwell-systems/nccheck)

## Technical Background

Languages:

![C](https://img.shields.io/badge/Systems_Programming-292c34?logo=c&logoColor=white&labelColor=1a1d22)
![Go](https://img.shields.io/badge/Go-%F0%9F%90%B9-292c34?logo=go&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-%F0%9F%A6%80-292c34?logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-%F0%9F%90%8D-292c34?logo=python&logoColor=ffdd54)
![Java](https://img.shields.io/badge/Java-%E2%98%95-292c34?logo=openjdk&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-292c34?logo=nodedotjs&logoColor=white)

Platforms & Shells:

![Platform](https://img.shields.io/badge/Platform-%F0%9F%8D%8E%20macOS%20%7C%20%F0%9F%90%A7%20Linux%20%7C%20%F0%9F%AA%9F%20WSL-292c34)
![Zsh](https://img.shields.io/badge/Zsh-292c34?logo=zsh&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-292c34?logo=gnubash&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-6b7280?logo=powershell&logoColor=white)

Developer Tooling:

![Git](https://img.shields.io/badge/Git-%F0%9F%94%A7-292c34?logo=git&logoColor=f41c80)
![Terraform](https://img.shields.io/badge/Terraform-292c34?logo=terraform&logoColor=f41c80)
![AWS%20CDK](https://img.shields.io/badge/AWS%20CDK-292c34?logo=amazonaws&logoColor=f41c80)
![Datadog](https://img.shields.io/badge/Datadog-292c34?logo=datadog&logoColor=f41c80)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-292c34?logo=opentelemetry&logoColor=f41c80)
![Containers](https://img.shields.io/badge/Containers-%F0%9F%90%B3%20Docker-292c34?logo=docker&logoColor=f41c80)

Artificial Intelligence:

[![GPT](https://img.shields.io/badge/GPT-%F0%9F%A4%96%20OpenAI-292c34?logo=openai&logoColor=f41c80)](https://openai.com/)
[![Claude](https://img.shields.io/badge/Claude-%F0%9F%A7%A0%20Anthropic-292c34?logo=anthropic&logoColor=f41c80)](https://www.anthropic.com/)

- Product Engineer
- Cloud/Platform & backend engineer:  APIs, Infrastructure as Code, Automation
- Compliance Automation for FDA-regulated systems
- Exploring blockchain security and on-chain systems
- Building developer tooling: secrets orchestration, reproducible environments, and CLI workflows
