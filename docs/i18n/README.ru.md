[English](../../README.md) · [简体中文](README.zh-CN.md) · **Русский** · [हिन्दी](README.hi.md) · [العربية](README.ar.md)

[![Blackwell Systems™](https://raw.githubusercontent.com/blackwell-systems/blackwell-docs-theme/main/badge-trademark.svg)](https://github.com/blackwell-systems) [![Stars](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/blackwell-systems/blackwell-systems/main/stars-badge.json)](https://github.com/blackwell-systems)

## Blackwell Systems: строим стек агентного ИИ, публикуем доказательства

Основатель: Dayna Blackwell. Я создаю открытую инфраструктуру, на которой работает стек агентного ИИ, и предоставляю доказательства, подкрепляющие её: устойчивые агенты, форматы передачи данных, интеллектуальный анализ кода, инструментарий MCP и тестирование на соответствие, с исследованиями в основе. Независимо, доказательства прежде всего.

---

### GCF (Graph Compact Format)

<a href="https://github.com/blackwell-systems/gcf"><img src="https://raw.githubusercontent.com/blackwell-systems/gcf/main/assets/gcf-hero-wire-delta.png" width="75%" alt="GCF"></a>

AI-нативный формат передачи структурированных данных. 100% понимания на каждой передовой модели. На 50-92% меньше токенов, чем в JSON. 2500+ оценок LLM на 11 моделях от 4 провайдеров. 43 млрд+ проходов без потерь через 5 форматов. Развёрнут в 20 промышленных системах, включая Chrome DevTools MCP. Обучение не требуется.

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

Полноценный фреймворк для создания ИИ-агентов на Go: модели (OpenAI, Anthropic, Gemini), инструменты, типизированные многошаговые потоки, память и RAG, MCP, координация нескольких агентов и типизированный human-in-the-loop, всё это на едином устойчивом журнале, работающем только на добавление. Именно журнал всё меняет: побочные эффекты срабатывают не более одного раза (возобновлённый прогон никогда не спишет с карты повторно и не отправит письмо заново), тысячи одновременных прогонов переживают сбои и передачу узлов в рамках одного процесса без кластера, каждый прогон формирует криптографически проверяемый аудиторский след (доказательства Меркла по RFC 6962, проверяемые без доверия к поставщику), а разделяемое управляемое состояние доказуемо сходится. Создано для окружающих агентов, которые работают без надзора и действуют под аудитом.

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

Инфраструктура интеллектуального анализа кода для ИИ-агентов. 65 инструментов, 30 языков с проверкой в CI, 24 агентных рабочих процесса. Единый бинарник на Go. По умолчанию использует GCF как формат вывода.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/agent-lsp?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/agent-lsp/blob/main/LICENSE)

### mcp-assert

<a href="https://github.com/blackwell-systems/mcp-assert"><img src="https://raw.githubusercontent.com/blackwell-systems/mcp-assert/main/assets/social-preview.png" width="50%" alt="mcp-assert"></a>

Тестирование MCP-серверов на соответствие. Просканировано 102 сервера, найдено 34 бага, подано 12 issue в апстрим. Фаззинг, линтинг схем, изоляция в Docker для каждой проверки.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/mcp-assert?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/mcp-assert/blob/main/LICENSE)

### knowing

<a href="https://github.com/blackwell-systems/knowing"><img src="https://raw.githubusercontent.com/blackwell-systems/knowing/main/assets/knowing-social-preview.jpg" width="50%" alt="knowing"></a>

Самоадаптирующийся движок интеллектуального анализа кода. Система, из которой был выделен GCF. 28 инструментов MCP, граф-нативный анализ, дедупликация сессий.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/knowing?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/knowing/blob/main/LICENSE)

### polywave

<a href="https://github.com/blackwell-systems/polywave"><img src="https://raw.githubusercontent.com/blackwell-systems/polywave/main/assets/social-preview.png" width="50%" alt="polywave"></a>

Координация параллельных ИИ-агентов. Непересекающееся владение файлами, изоляция через git worktree, поэтапно контролируемое выполнение и планы, проверенные человеком. Агент Scout сопоставляет кодовую базу с планом координации; агенты Wave одновременно реализуют назначенные им файлы.

[![Shell](https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)](https://github.com/blackwell-systems/polywave)

[Protocol](https://github.com/blackwell-systems/polywave-protocol) ·
[Claude Code](https://github.com/blackwell-systems/polywave) ·
[Codex](https://github.com/blackwell-systems/polywave-codex) ·
[Go](https://github.com/blackwell-systems/polywave-go)

### goldenthread

<a href="https://github.com/blackwell-systems/goldenthread"><img src="https://raw.githubusercontent.com/blackwell-systems/goldenthread/main/asset-banner-social.jpg" width="50%" alt="goldenthread"></a>

Из структур Go в TypeScript и Zod, единый источник истины. Размеченные объединения, перечисления, отображения и правила валидации компилируются в проверяемые во время выполнения схемы Zod; опциональный вывод по json-тегам связывает обычные типы. Создано для Wails и веб-фронтендов. Apache-2.0.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-6fa2c9?style=for-the-badge)](https://github.com/blackwell-systems/goldenthread)

### GCP Emulator Suite

Локальные реализации API Google Cloud для разработки и CI. Учётные данные GCP не требуются.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/license-Apache--2.0-6fa2c9?style=for-the-badge)](https://github.com/blackwell-systems/gcp-secret-manager-emulator/blob/main/LICENSE)

[Secret Manager](https://github.com/blackwell-systems/gcp-secret-manager-emulator) (50K+ загрузок) ·
[KMS](https://github.com/blackwell-systems/gcp-kms-emulator) ·
[IAM](https://github.com/blackwell-systems/gcp-iam-emulator) ·
[Eventarc](https://github.com/blackwell-systems/gcp-eventarc-emulator) ·
[Auth](https://github.com/blackwell-systems/gcp-emulator-auth) ·
[IAM Control Plane](https://github.com/blackwell-systems/gcp-iam-control-plane) ·
[Core](https://github.com/blackwell-systems/gcp-emulator)

---

### Исследования

9 самостоятельно опубликованных статей (Zenodo DOI), несколько из них получили отклик индустрии. Исследовательская программа по связи токенизатора и внимания, доказывающая, что решения о слияниях BPE навсегда ограничивают ёмкость внимания трансформера, плюс системные работы по распределённой сходимости и освобождению памяти.

**Tokenizer-Attention Coupling** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20925910-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20925910)
Как решения о слияниях BPE навсегда формируют внутреннюю организацию трансформера. 43 токенизатора, 20 провайдеров. Контролируемый эксперимент: идентичные модели, разный токенизатор. Барьеры слияния дают в 3-738 раз лучшее понимание структурированных данных при нулевых потерях на естественном языке. 18-фазная причинная абляция на 2 архитектурах, 2 масштабах, 3 доменах.

**Stranded Attention** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21158886-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21158886)
Ранее не описанный режим отказа: каждая голова внимания в стандартной BPE-модели обладает структурной ёмкостью, которую токенизатор навсегда блокирует. Все 384 головы при 410M и 768 при 1.3B показывают в 4 раза больше внимания к разделителям при чистых границах. Разрыв фрустрации в 40 п.п. появляется к шагу 5000 и никогда не закрывается.

**Developmental Atlas of Attention Head Specialization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21205389-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21205389)
Первый масштабный атлас специализации голов: 384 головы, 7 типов поведения, 131 контрольная точка, 7 прогонов, 2 архитектуры. Ёмкостный налог BPE не зависит от архитектуры (+64.3% NeoX, +67.0% Llama). 48-56% ёмкости внимания в стандартной BPE непродуктивны.

**Structural Ambiguity in JSON Tokenization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20810588-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20810588)
Кросс-токенизаторный анализ на 8 токенизаторах и 6 провайдерах. Имена полей JSON сливаются с открывающей кавычкой на 50-63% токенизаторов. Частота слияния границ JSON 8.93% против 1.00% для вертикальной черты; табуляция TOON 59.82%. Накладные расходы JSON достигают 81% при 500 строках.

**Graph Compact Format (GCF)** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20579817-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20579817)
AI-нативный формат передачи структурированных данных. 2500+ оценок на 11 моделях от 4 провайдеров. 43 млрд+ проходов без потерь. Развёрнут в 20 промышленных системах. Spec v3.5.1 Stable.
[Explore the project](https://github.com/blackwell-systems/gcf)

**The Hierarchical Identity Architecture** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20342255-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20342255)
Адресация по содержимому как вычислительный примитив для интеллектуального анализа связей в ПО. В 2.75 раза точнее GitNexus (p=0.0003), индексация корпоративных репозиториев в 193 раза быстрее.
[Explore the project](https://github.com/blackwell-systems/knowing) · [merkle-strata](https://github.com/blackwell-systems/merkle-strata)

**Memory Drainability** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18653776-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18653776)
Формализует, когда крупнозернистые аллокаторы могут освобождать память. Доказывает резкую дихотомию O(1) против Ω(t) для ограниченного удержания. Подтверждено эмпирически (238-кратная разница в частоте переработки).
[Explore the project](https://github.com/blackwell-systems/drainability)

**Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18671870-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18671870)
Сходимость без координации через вполне обоснованную компенсацию. Третий режим сходимости наряду с CRDT и инвариантной конфлюэнтностью.
[Explore the project](https://github.com/blackwell-systems/normalization-confluence)

**Federated Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18677400-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18677400)
Межорганизационная сходимость через сохранение валидности морфизмов над ациклическими сетями.

---

### Вклад в апстрим

40+ смёрдженных PR по всей экосистеме. #6 контрибьютор в [mcp-go](https://github.com/mark3labs/mcp-go) (8.7K звёзд).
Исправления повреждения данных, восстановление после паник, укрепление SDK, соответствие спецификациям, баги транспорта.

| Организация | Что | Звёзды |
|:---|:---|---:|
| **Google** | Chrome DevTools MCP (формат GCF), go-containerregistry | 47K |
| **Anthropic** | MCP Go, Python, PHP SDK + серверы | 85K+ |
| **LangChain** | langchain (исправление разбивщика текста) | 136K |
| **etcd** | Исправление кода ошибки CNCF gRPC (на рассмотрении) | 51K |
| **Charmbracelet** | bubbletea, huh | 42K |
| **GitHub** | github-mcp-server | 16K |
| **HashiCorp** | terraform-provider-aws (исправление GovCloud) | 10.9K |
| **pypa** | pip (исправление кодировки локали) | 10.2K |
| **mark3labs** | mcp-go SDK (9 PR, #6 контрибьютор) | 8.7K |
| **Ant Group** | mcp-server-chart (9 исправлений багов) | 4K |
| **Grafana** | mcp-grafana (3 смёрдженных PR) | 2.9K |

[Full list](https://blog.blackwell-systems.com/oss#upstream-contributions)

---

### Технический профиль

Языки:

![C](https://img.shields.io/badge/Systems_Programming-292c34?logo=c&logoColor=white&labelColor=1a1d22&style=for-the-badge)
![Go](https://img.shields.io/badge/Go-%F0%9F%90%B9-292c34?logo=go&logoColor=white&style=for-the-badge)
![Rust](https://img.shields.io/badge/Rust-%F0%9F%A6%80-292c34?logo=rust&logoColor=white&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-%F0%9F%90%8D-292c34?logo=python&logoColor=ffdd54&style=for-the-badge)
![Java](https://img.shields.io/badge/Java-%E2%98%95-292c34?logo=openjdk&logoColor=white&style=for-the-badge)
![Node.js](https://img.shields.io/badge/Node.js-292c34?logo=nodedotjs&logoColor=white&style=for-the-badge)

Платформы и оболочки:

![Platform](https://img.shields.io/badge/Platform-%F0%9F%8D%8E%20macOS%20%7C%20%F0%9F%90%A7%20Linux%20%7C%20%F0%9F%AA%9F%20WSL-292c34?style=for-the-badge)
![Zsh](https://img.shields.io/badge/Zsh-292c34?logo=zsh&logoColor=white&style=for-the-badge)
![Bash](https://img.shields.io/badge/Bash-292c34?logo=gnubash&logoColor=white&style=for-the-badge)
![PowerShell](https://img.shields.io/badge/PowerShell-6b7280?logo=powershell&logoColor=white&style=for-the-badge)

Инструментарий разработчика:

![Git](https://img.shields.io/badge/Git-%F0%9F%94%A7-292c34?logo=git&logoColor=6fa2c9&style=for-the-badge)
![Terraform](https://img.shields.io/badge/Terraform-292c34?logo=terraform&logoColor=6fa2c9&style=for-the-badge)
![AWS%20CDK](https://img.shields.io/badge/AWS%20CDK-292c34?logo=amazonaws&logoColor=6fa2c9&style=for-the-badge)
![Datadog](https://img.shields.io/badge/Datadog-292c34?logo=datadog&logoColor=6fa2c9&style=for-the-badge)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-292c34?logo=opentelemetry&logoColor=6fa2c9&style=for-the-badge)
![Containers](https://img.shields.io/badge/Containers-%F0%9F%90%B3%20Docker-292c34?logo=docker&logoColor=6fa2c9&style=for-the-badge)
![GCP](https://img.shields.io/badge/Google%20Cloud-292c34?logo=googlecloud&logoColor=6fa2c9&style=for-the-badge)

Искусственный интеллект:

[![GPT](https://img.shields.io/badge/GPT-%F0%9F%A4%96%20OpenAI-292c34?logo=openai&logoColor=6fa2c9&style=for-the-badge)](https://openai.com/)
[![Claude](https://img.shields.io/badge/Claude-%F0%9F%A7%A0%20Anthropic-292c34?logo=anthropic&logoColor=6fa2c9&style=for-the-badge)](https://www.anthropic.com/)
[![Gemini](https://img.shields.io/badge/Gemini-%E2%9C%A8%20Google-292c34?logo=googlegemini&logoColor=6fa2c9&style=for-the-badge)](https://deepmind.google/technologies/gemini/)
