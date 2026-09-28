[English](../../README.md) · [简体中文](README.zh-CN.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · **العربية**

[![Blackwell Systems™](https://raw.githubusercontent.com/blackwell-systems/blackwell-docs-theme/main/badge-trademark.svg)](https://github.com/blackwell-systems) [![Stars](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/blackwell-systems/blackwell-systems/main/stars-badge.json)](https://github.com/blackwell-systems)

## Blackwell Systems: بناء منظومة الوكلاء ونشر الأدلة

المؤسِّسة: Dayna Blackwell. أبني البنية التحتية المفتوحة التي تعمل عليها منظومة الذكاء الاصطناعي الوكيلي، وأقدّم الأدلة التي تدعمها: وكلاء دائمون، وصيغ نقل بيانات، وذكاء بَرمجي للشفرة، وأدوات MCP، واختبارات المطابقة، مع البحث في الأساس. مستقلة، والدليل أولاً.

---

### GCF (Graph Compact Format)

<a href="https://github.com/blackwell-systems/gcf"><img src="https://raw.githubusercontent.com/blackwell-systems/gcf/main/assets/gcf-hero-wire-delta.png" width="75%" alt="GCF"></a>

صيغة نقل بيانات أصيلة للذكاء الاصطناعي مخصّصة للبيانات المُهيكلة. فهم بنسبة 100% على كل نموذج رائد. عدد رموز أقل بنسبة 50-92% مقارنةً بـ JSON. أكثر من 2,500 تقييم لنماذج اللغة الكبيرة عبر 11 نموذجًا و4 مزوّدين. أكثر من 43 مليار دورة ذهاب وإياب بلا فقدان عبر 5 صيغ. منشورة في 20 نظامًا إنتاجيًا بما في ذلك Chrome DevTools MCP. لا حاجة إلى أي تدريب.

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

إطار عمل متكامل لبناء وكلاء الذكاء الاصطناعي بلغة Go: النماذج (OpenAI وAnthropic وGemini)، والأدوات، والتدفقات المُهيكلة متعددة الخطوات، والذاكرة وRAG، وMCP، وتنسيق الوكلاء المتعددين، وحلقة الإنسان في المسار المُهيكلة، كل ذلك على سجلّ واحد دائم يقبل الإضافة فقط. السجلّ هو ما يصنع الفرق: الآثار الجانبية تُنفَّذ مرة واحدة على الأكثر (التشغيل المُستأنَف لا يخصم من بطاقة مرتين ولا يعيد إرسال بريد إلكتروني)، وآلاف عمليات التشغيل المتزامنة تنجو من الأعطال وتسليم العُقَد ضمن عملية واحدة دون عنقود، وكل تشغيل يُنتج سجلّ تدقيق قابلًا للتحقق تشفيريًا (براهين Merkle وفق RFC 6962، قابلة للفحص دون الوثوق بالمزوّد)، والحالة المُشترَكة المحكومة قابلة للتقارب على نحوٍ مُثبَت. مبني للوكلاء المحيطين الذين يعملون دون إشراف ويتصرفون تحت التدقيق.

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

بنية تحتية للذكاء البَرمجي للشفرة مخصّصة لوكلاء الذكاء الاصطناعي. 65 أداة، و30 لغة مُتحقَّقًا منها عبر CI، و24 سير عمل للوكلاء. ملف Go تنفيذي واحد. يستخدم GCF بوصفه صيغة الإخراج الافتراضية.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/agent-lsp?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/agent-lsp/blob/main/LICENSE)

### mcp-assert

<a href="https://github.com/blackwell-systems/mcp-assert"><img src="https://raw.githubusercontent.com/blackwell-systems/mcp-assert/main/assets/social-preview.png" width="50%" alt="mcp-assert"></a>

اختبار المطابقة لخوادم MCP. جرى فحص 102 خادم، واكتُشف 34 خللًا، ورُفعت 12 مشكلة إلى المصدر الأعلى. اختبار عشوائي (Fuzz)، وتدقيق المخططات (schema linting)، وعزل Docker لكل تأكيد.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/mcp-assert?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/mcp-assert/blob/main/LICENSE)

### knowing

<a href="https://github.com/blackwell-systems/knowing"><img src="https://raw.githubusercontent.com/blackwell-systems/knowing/main/assets/knowing-social-preview.jpg" width="50%" alt="knowing"></a>

محرّك ذكاء بَرمجي للشفرة ذاتي التكيّف. النظام الذي استُخرج منه GCF. 28 أداة MCP، وتحليل أصيل قائم على الرسوم البيانية، وإزالة تكرار الجلسات.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/knowing?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/knowing/blob/main/LICENSE)

### polywave

<a href="https://github.com/blackwell-systems/polywave"><img src="https://raw.githubusercontent.com/blackwell-systems/polywave/main/assets/social-preview.png" width="50%" alt="polywave"></a>

تنسيق متوازٍ لوكلاء الذكاء الاصطناعي. ملكية ملفات غير متقاطعة، وعزل عبر git worktree، وتنفيذ محكوم بالطبقات، وخطط مُراجَعة بشريًا. يقوم وكيل Scout بتخطيط قاعدة الشفرة إلى خطة تنسيق؛ ويُنفّذ وكلاء Wave الملفات المُسندة إليهم في آنٍ واحد.

[![Shell](https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)](https://github.com/blackwell-systems/polywave)

[Protocol](https://github.com/blackwell-systems/polywave-protocol) ·
[Claude Code](https://github.com/blackwell-systems/polywave) ·
[Codex](https://github.com/blackwell-systems/polywave-codex) ·
[Go](https://github.com/blackwell-systems/polywave-go)

### goldenthread

<a href="https://github.com/blackwell-systems/goldenthread"><img src="https://raw.githubusercontent.com/blackwell-systems/goldenthread/main/asset-banner-social.jpg" width="50%" alt="goldenthread"></a>

من بُنى Go إلى TypeScript وZod، مصدر واحد للحقيقة. تُترجَم الاتحادات المُميَّزة والتعدادات والخرائط وقواعد التحقق إلى مخططات Zod مُتحقَّق منها في وقت التشغيل؛ ويربط استنتاج json-tag الاختياري الأنواع البسيطة. مبني لواجهات Wails والواجهات الأمامية للويب. Apache-2.0.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-6fa2c9?style=for-the-badge)](https://github.com/blackwell-systems/goldenthread)

### GCP Emulator Suite

تطبيقات محلية لواجهات Google Cloud البرمجية لأغراض التطوير والتكامل المستمر. لا حاجة إلى أي بيانات اعتماد لـ GCP.

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/license-Apache--2.0-6fa2c9?style=for-the-badge)](https://github.com/blackwell-systems/gcp-secret-manager-emulator/blob/main/LICENSE)

[Secret Manager](https://github.com/blackwell-systems/gcp-secret-manager-emulator) (أكثر من 50 ألف تنزيل) ·
[KMS](https://github.com/blackwell-systems/gcp-kms-emulator) ·
[IAM](https://github.com/blackwell-systems/gcp-iam-emulator) ·
[Eventarc](https://github.com/blackwell-systems/gcp-eventarc-emulator) ·
[Auth](https://github.com/blackwell-systems/gcp-emulator-auth) ·
[IAM Control Plane](https://github.com/blackwell-systems/gcp-iam-control-plane) ·
[Core](https://github.com/blackwell-systems/gcp-emulator)

---

### البحث

9 أوراق منشورة ذاتيًا (معرّفات Zenodo DOI)، عدد منها حظي باستجابة من الصناعة. برنامج بحثي حول اقتران المُرمِّز والانتباه يُثبت أن قرارات دمج BPE تُقيّد سعة انتباه المُحوِّل بصورة دائمة، إضافةً إلى أعمال أنظمة حول التقارب الموزَّع واسترجاع الذاكرة.

**Tokenizer-Attention Coupling** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20925910-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20925910)
كيف تُشكّل قرارات دمج BPE التنظيم الداخلي للمُحوِّل بصورة دائمة. 43 مُرمِّزًا، و20 مزوّدًا. تجربة مضبوطة: نماذج متطابقة، ومُرمِّز مختلف. تُنتج حواجز الدمج فهمًا للبيانات المُهيكلة أفضل بمقدار 3-738 ضعفًا، دون أي كلفة على اللغة الطبيعية. استئصال سببي من 18 مرحلة عبر بنيتين ومقياسين و3 مجالات.

**Stranded Attention** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21158886-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21158886)
نمط إخفاق لم يُوصَف من قبل: كل رأس انتباه في نموذج BPE قياسي يمتلك سعة بنيوية يمنعها المُرمِّز بصورة دائمة. تُظهر كل الرؤوس البالغ عددها 384 عند 410M و768 عند 1.3B انتباهًا للفواصل أكثر بأربعة أضعاف في ظل حدود نظيفة. تظهر فجوة الإحباط البالغة 40 نقطة مئوية بحلول الخطوة 5,000 ولا تُغلق أبدًا.

**Developmental Atlas of Attention Head Specialization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21205389-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21205389)
أول أطلس لتخصّص الرؤوس على نطاق واسع: 384 رأسًا، و7 سلوكيات، و131 نقطة تفتيش، و7 عمليات تشغيل، وبنيتان. ضريبة سعة BPE مستقلة عن البنية (+64.3% لـ NeoX، +67.0% لـ Llama). ما بين 48-56% من سعة الانتباه في BPE القياسي غير مُنتِج.

**Structural Ambiguity in JSON Tokenization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20810588-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20810588)
تحليل عابر للمُرمِّزات عبر 8 مُرمِّزات و6 مزوّدين. تندمج أسماء حقول JSON مع علامة الاقتباس الافتتاحية على 50-63% من المُرمِّزات. معدل دمج حدود JSON 8.93% مقابل 1.00% للخط العمودي (pipe)؛ وعلامة الجدولة في TOON 59.82%. تبلغ نفقات JSON الإضافية 81% عند 500 صف.

**Graph Compact Format (GCF)** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20579817-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20579817)
صيغة نقل بيانات أصيلة للذكاء الاصطناعي مخصّصة للبيانات المُهيكلة. أكثر من 2,500 تقييم عبر 11 نموذجًا و4 مزوّدين. أكثر من 43 مليار دورة ذهاب وإياب بلا فقدان. منشورة في 20 نظامًا إنتاجيًا. Spec v3.5.1 Stable.
[Explore the project](https://github.com/blackwell-systems/gcf)

**The Hierarchical Identity Architecture** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20342255-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20342255)
العنونة بالمحتوى بوصفها بدائية حوسبية لذكاء العلاقات البرمجية. أدقّ بمقدار 2.75 ضعفًا من GitNexus (p=0.0003)، وأسرع في الفهرسة بمقدار 193 ضعفًا على المستودعات المؤسسية.
[Explore the project](https://github.com/blackwell-systems/knowing) · [merkle-strata](https://github.com/blackwell-systems/merkle-strata)

**Memory Drainability** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18653776-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18653776)
يُصوغ رسميًا متى يمكن للمُخصِّصات الخشنة التحبّب أن تسترجع الذاكرة. يُثبت انقسامًا حادًا بين O(1) وΩ(t) للاحتفاظ المحدود. جرى التحقق منه تجريبيًا (فارق في معدل إعادة التدوير يبلغ 238 ضعفًا).
[Explore the project](https://github.com/blackwell-systems/drainability)

**Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18671870-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18671870)
تقارب بلا تنسيق عبر تعويض مُؤسَّس على نحوٍ سليم. نظام التقارب الثالث إلى جانب CRDTs والتقارب الثابت (invariant confluence).
[Explore the project](https://github.com/blackwell-systems/normalization-confluence)

**Federated Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18677400-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18677400)
تقارب متعدد المؤسسات عبر الحفاظ على صلاحية التشاكل (morphism) فوق شبكات لا دورية.

---

### مساهمات المصدر الأعلى

أكثر من 40 طلب سحب (PR) مُدمَجًا عبر المنظومة. المساهم رقم 6 في [mcp-go](https://github.com/mark3labs/mcp-go) (8.7K stars).
إصلاحات لتلف البيانات، واستعادة من حالات panic، وتصليب SDK، والامتثال للمواصفات، وأخطاء النقل.

| المؤسسة | ماذا | Stars |
|:---|:---|---:|
| **Google** | Chrome DevTools MCP (صيغة GCF)، go-containerregistry | 47K |
| **Anthropic** | حزم تطوير MCP Go وPython وPHP + خوادم | 85K+ |
| **LangChain** | langchain (إصلاح مُقسِّم النصوص) | 136K |
| **etcd** | إصلاح رمز خطأ CNCF gRPC (قيد المراجعة) | 51K |
| **Charmbracelet** | bubbletea، huh | 42K |
| **GitHub** | github-mcp-server | 16K |
| **HashiCorp** | terraform-provider-aws (إصلاح GovCloud) | 10.9K |
| **pypa** | pip (إصلاح ترميز اللغة المحلية) | 10.2K |
| **mark3labs** | mcp-go SDK (9 طلبات سحب، المساهم رقم 6) | 8.7K |
| **Ant Group** | mcp-server-chart (9 إصلاحات لأخطاء) | 4K |
| **Grafana** | mcp-grafana (3 طلبات سحب مُدمَجة) | 2.9K |

[Full list](https://blog.blackwell-systems.com/oss#upstream-contributions)

---

### الخلفية التقنية

اللغات:

![C](https://img.shields.io/badge/Systems_Programming-292c34?logo=c&logoColor=white&labelColor=1a1d22&style=for-the-badge)
![Go](https://img.shields.io/badge/Go-%F0%9F%90%B9-292c34?logo=go&logoColor=white&style=for-the-badge)
![Rust](https://img.shields.io/badge/Rust-%F0%9F%A6%80-292c34?logo=rust&logoColor=white&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-%F0%9F%90%8D-292c34?logo=python&logoColor=ffdd54&style=for-the-badge)
![Java](https://img.shields.io/badge/Java-%E2%98%95-292c34?logo=openjdk&logoColor=white&style=for-the-badge)
![Node.js](https://img.shields.io/badge/Node.js-292c34?logo=nodedotjs&logoColor=white&style=for-the-badge)

المنصّات والأصداف (Shells):

![Platform](https://img.shields.io/badge/Platform-%F0%9F%8D%8E%20macOS%20%7C%20%F0%9F%90%A7%20Linux%20%7C%20%F0%9F%AA%9F%20WSL-292c34?style=for-the-badge)
![Zsh](https://img.shields.io/badge/Zsh-292c34?logo=zsh&logoColor=white&style=for-the-badge)
![Bash](https://img.shields.io/badge/Bash-292c34?logo=gnubash&logoColor=white&style=for-the-badge)
![PowerShell](https://img.shields.io/badge/PowerShell-6b7280?logo=powershell&logoColor=white&style=for-the-badge)

أدوات المطوّرين:

![Git](https://img.shields.io/badge/Git-%F0%9F%94%A7-292c34?logo=git&logoColor=6fa2c9&style=for-the-badge)
![Terraform](https://img.shields.io/badge/Terraform-292c34?logo=terraform&logoColor=6fa2c9&style=for-the-badge)
![AWS%20CDK](https://img.shields.io/badge/AWS%20CDK-292c34?logo=amazonaws&logoColor=6fa2c9&style=for-the-badge)
![Datadog](https://img.shields.io/badge/Datadog-292c34?logo=datadog&logoColor=6fa2c9&style=for-the-badge)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-292c34?logo=opentelemetry&logoColor=6fa2c9&style=for-the-badge)
![Containers](https://img.shields.io/badge/Containers-%F0%9F%90%B3%20Docker-292c34?logo=docker&logoColor=6fa2c9&style=for-the-badge)
![GCP](https://img.shields.io/badge/Google%20Cloud-292c34?logo=googlecloud&logoColor=6fa2c9&style=for-the-badge)

الذكاء الاصطناعي:

[![GPT](https://img.shields.io/badge/GPT-%F0%9F%A4%96%20OpenAI-292c34?logo=openai&logoColor=6fa2c9&style=for-the-badge)](https://openai.com/)
[![Claude](https://img.shields.io/badge/Claude-%F0%9F%A7%A0%20Anthropic-292c34?logo=anthropic&logoColor=6fa2c9&style=for-the-badge)](https://www.anthropic.com/)
[![Gemini](https://img.shields.io/badge/Gemini-%E2%9C%A8%20Google-292c34?logo=googlegemini&logoColor=6fa2c9&style=for-the-badge)](https://deepmind.google/technologies/gemini/)
