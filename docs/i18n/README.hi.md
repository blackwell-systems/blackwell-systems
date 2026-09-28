[English](../../README.md) · [简体中文](README.zh-CN.md) · [Русский](README.ru.md) · **हिन्दी**

[![Blackwell Systems™](https://raw.githubusercontent.com/blackwell-systems/blackwell-docs-theme/main/badge-trademark.svg)](https://github.com/blackwell-systems) [![Stars](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/blackwell-systems/blackwell-systems/main/stars-badge.json)](https://github.com/blackwell-systems)

## Blackwell Systems: एजेंटिक स्टैक का निर्माण, प्रमाण का प्रकाशन

संस्थापक: Dayna Blackwell। मैं वह ओपन इन्फ्रास्ट्रक्चर बनाती हूँ जिस पर एजेंटिक AI स्टैक चलता है, और उसका समर्थन करने वाले प्रमाण भी प्रस्तुत करती हूँ: टिकाऊ एजेंट, वायर फ़ॉर्मैट, कोड इंटेलिजेंस, MCP टूलिंग, और कॉन्फ़ॉर्मेंस परीक्षण, जिनकी नींव में शोध है। स्वतंत्र, प्रमाण-प्रथम।

---

### GCF (Graph Compact Format)

<a href="https://github.com/blackwell-systems/gcf"><img src="https://raw.githubusercontent.com/blackwell-systems/gcf/main/assets/gcf-hero-wire-delta.png" width="75%" alt="GCF"></a>

संरचित डेटा के लिए AI-नेटिव वायर फ़ॉर्मैट। हर फ्रंटियर मॉडल पर 100% समझ। JSON की तुलना में 50-92% कम टोकन। 4 प्रदाताओं के 11 मॉडलों पर 2,500+ LLM मूल्यांकन। 5 फ़ॉर्मैटों में 43B+ हानि-रहित राउंड-ट्रिप। Chrome DevTools MCP सहित 20 प्रोडक्शन सिस्टमों में तैनात। किसी प्रशिक्षण की आवश्यकता नहीं।

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

Go में AI एजेंट बनाने के लिए एक सम्पूर्ण फ्रेमवर्क: मॉडल (OpenAI, Anthropic, Gemini), टूल, टाइप्ड बहु-चरणीय फ़्लो, मेमोरी और RAG, MCP, बहु-एजेंट समन्वय, और टाइप्ड human-in-the-loop, ये सब एक ही टिकाऊ, केवल-जोड़ (append-only) जर्नल पर। अंतर यही जर्नल पैदा करता है: साइड इफ़ेक्ट अधिकतम एक बार चलते हैं (पुनः शुरू किया गया रन कभी किसी कार्ड से दोबारा शुल्क नहीं लेता या ईमेल दोबारा नहीं भेजता), हज़ारों समवर्ती रन बिना किसी क्लस्टर के एक ही प्रोसेस में क्रैश और नोड हैंडऑफ़ को झेल जाते हैं, हर रन एक क्रिप्टोग्राफ़िक रूप से सत्यापन-योग्य ऑडिट ट्रेल उत्पन्न करता है (RFC 6962 Merkle प्रमाण, विक्रेता पर भरोसा किए बिना जाँचने योग्य), और साझा शासित स्थिति प्रमाणित रूप से अभिसारी होती है। ऐसे परिवेशी एजेंटों के लिए बनाया गया जो बिना निगरानी के चलते हैं और ऑडिट के अधीन कार्य करते हैं।

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

AI एजेंटों के लिए कोड इंटेलिजेंस इन्फ्रास्ट्रक्चर। 65 टूल, 30 CI-सत्यापित भाषाएँ, 24 एजेंट वर्कफ़्लो। एकल Go बाइनरी। डिफ़ॉल्ट आउटपुट फ़ॉर्मैट के रूप में GCF का उपयोग करता है।

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/agent-lsp?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/agent-lsp/blob/main/LICENSE)

### mcp-assert

<a href="https://github.com/blackwell-systems/mcp-assert"><img src="https://raw.githubusercontent.com/blackwell-systems/mcp-assert/main/assets/social-preview.png" width="50%" alt="mcp-assert"></a>

MCP सर्वरों के लिए कॉन्फ़ॉर्मेंस परीक्षण। 102 सर्वर स्कैन किए गए, 34 बग पाए गए, 12 अपस्ट्रीम इश्यू दायर किए गए। फ़ज़ परीक्षण, स्कीमा लिंटिंग, प्रति-अभिकथन Docker आइसोलेशन।

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/mcp-assert?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/mcp-assert/blob/main/LICENSE)

### knowing

<a href="https://github.com/blackwell-systems/knowing"><img src="https://raw.githubusercontent.com/blackwell-systems/knowing/main/assets/knowing-social-preview.jpg" width="50%" alt="knowing"></a>

स्व-अनुकूलनशील कोड इंटेलिजेंस इंजन। वह सिस्टम जिससे GCF निकाला गया था। 28 MCP टूल, ग्राफ़-नेटिव विश्लेषण, सत्र डिडुप्लिकेशन।

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/github/license/blackwell-systems/knowing?style=for-the-badge&color=6fa2c9)](https://github.com/blackwell-systems/knowing/blob/main/LICENSE)

### polywave

<a href="https://github.com/blackwell-systems/polywave"><img src="https://raw.githubusercontent.com/blackwell-systems/polywave/main/assets/social-preview.png" width="50%" alt="polywave"></a>

समानांतर AI एजेंट समन्वय। असंयुक्त फ़ाइल स्वामित्व, git worktree आइसोलेशन, टियर-गेटेड निष्पादन, और मानव-समीक्षित योजनाएँ। एक Scout एजेंट कोडबेस को एक समन्वय योजना में मैप करता है; Wave एजेंट अपनी सौंपी गई फ़ाइलों को एक साथ लागू करते हैं।

[![Shell](https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)](https://github.com/blackwell-systems/polywave)

[Protocol](https://github.com/blackwell-systems/polywave-protocol) ·
[Claude Code](https://github.com/blackwell-systems/polywave) ·
[Codex](https://github.com/blackwell-systems/polywave-codex) ·
[Go](https://github.com/blackwell-systems/polywave-go)

### goldenthread

<a href="https://github.com/blackwell-systems/goldenthread"><img src="https://raw.githubusercontent.com/blackwell-systems/goldenthread/main/asset-banner-social.jpg" width="50%" alt="goldenthread"></a>

Go स्ट्रक्ट से TypeScript और Zod तक, सत्य का एकल स्रोत। डिस्क्रिमिनेटेड यूनियन, एनम, मैप, और वैलिडेशन नियम रनटाइम पर जाँचे जाने वाले Zod स्कीमा में कम्पाइल होते हैं; ऑप्ट-इन json-tag इन्फ़रेंस सादे टाइपों को जोड़ता है। Wails और वेब फ्रंटएंड के लिए बनाया गया। Apache-2.0।

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-6fa2c9?style=for-the-badge)](https://github.com/blackwell-systems/goldenthread)

### GCP Emulator Suite

विकास और CI के लिए Google Cloud API के स्थानीय कार्यान्वयन। किसी GCP क्रेडेंशियल की आवश्यकता नहीं।

[![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)](https://go.dev)
[![License](https://img.shields.io/badge/license-Apache--2.0-6fa2c9?style=for-the-badge)](https://github.com/blackwell-systems/gcp-secret-manager-emulator/blob/main/LICENSE)

[Secret Manager](https://github.com/blackwell-systems/gcp-secret-manager-emulator) (50K+ डाउनलोड) ·
[KMS](https://github.com/blackwell-systems/gcp-kms-emulator) ·
[IAM](https://github.com/blackwell-systems/gcp-iam-emulator) ·
[Eventarc](https://github.com/blackwell-systems/gcp-eventarc-emulator) ·
[Auth](https://github.com/blackwell-systems/gcp-emulator-auth) ·
[IAM Control Plane](https://github.com/blackwell-systems/gcp-iam-control-plane) ·
[Core](https://github.com/blackwell-systems/gcp-emulator)

---

### शोध

9 स्व-प्रकाशित पेपर (Zenodo DOI), जिनमें से कई को उद्योग की प्रतिक्रिया मिली। टोकनाइज़र-अटेंशन युग्मन पर एक शोध कार्यक्रम, जो सिद्ध करता है कि BPE मर्ज निर्णय ट्रांसफ़ॉर्मर की अटेंशन क्षमता को स्थायी रूप से सीमित करते हैं, साथ ही वितरित अभिसरण और मेमोरी पुनर्ग्रहण पर सिस्टम्स कार्य।

**Tokenizer-Attention Coupling** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20925910-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20925910)
BPE मर्ज निर्णय किस तरह ट्रांसफ़ॉर्मर के आंतरिक संगठन को स्थायी रूप से आकार देते हैं। 43 टोकनाइज़र, 20 प्रदाता। नियंत्रित प्रयोग: समरूप मॉडल, भिन्न टोकनाइज़र। मर्ज अवरोधक संरचित डेटा की समझ में 3-738 गुना बेहतर परिणाम देते हैं, प्राकृतिक भाषा पर शून्य लागत के साथ। 2 आर्किटेक्चर, 2 स्केल, 3 डोमेन में 18-चरणीय कारणात्मक एब्लेशन।

**Stranded Attention** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21158886-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21158886)
एक पूर्व-अवर्णित विफलता मोड: एक मानक BPE मॉडल में प्रत्येक अटेंशन हेड में संरचनात्मक क्षमता होती है जिसे टोकनाइज़र स्थायी रूप से रोक देता है। 410M पर सभी 384 हेड और 1.3B पर 768 हेड स्पष्ट सीमाओं के तहत 4 गुना अधिक डिलिमिटर अटेंशन दिखाते हैं। 40pp फ़्रस्ट्रेशन अंतर चरण 5,000 तक प्रकट होता है और कभी बंद नहीं होता।

**Developmental Atlas of Attention Head Specialization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21205389-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.21205389)
बड़े पैमाने पर पहला हेड-विशेषज्ञता एटलस: 384 हेड, 7 व्यवहार, 131 चेकपॉइंट, 7 रन, 2 आर्किटेक्चर। BPE क्षमता कर आर्किटेक्चर-निरपेक्ष है (+64.3% NeoX, +67.0% Llama)। मानक BPE में 48-56% अटेंशन क्षमता अनुत्पादक है।

**Structural Ambiguity in JSON Tokenization** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20810588-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20810588)
8 टोकनाइज़र, 6 प्रदाताओं में क्रॉस-टोकनाइज़र विश्लेषण। JSON फ़ील्ड नाम 50-63% टोकनाइज़रों पर उद्घाटक उद्धरण चिह्न के साथ जुड़ जाते हैं। JSON सीमा मर्ज दर 8.93% बनाम पाइप के लिए 1.00%; TOON टैब 59.82%। JSON ओवरहेड 500 पंक्तियों पर 81% तक पहुँच जाता है।

**Graph Compact Format (GCF)** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20579817-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20579817)
संरचित डेटा के लिए AI-नेटिव वायर फ़ॉर्मैट। 4 प्रदाताओं के 11 मॉडलों पर 2,500+ मूल्यांकन। 43B+ हानि-रहित राउंड-ट्रिप। 20 प्रोडक्शन सिस्टमों में तैनात। Spec v3.5.1 Stable।
[Explore the project](https://github.com/blackwell-systems/gcf)

**The Hierarchical Identity Architecture** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20342255-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.20342255)
सॉफ़्टवेयर संबंध इंटेलिजेंस के लिए एक कम्प्यूटेशन आदिम के रूप में कंटेंट-एड्रेसिंग। GitNexus से 2.75 गुना अधिक सटीक (p=0.0003), एंटरप्राइज़ रिपॉज़िटरी पर 193 गुना तेज़ इंडेक्सिंग।
[Explore the project](https://github.com/blackwell-systems/knowing) · [merkle-strata](https://github.com/blackwell-systems/merkle-strata)

**Memory Drainability** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18653776-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18653776)
औपचारिक रूप से परिभाषित करता है कि मोटे-दाने वाले आवंटक कब मेमोरी पुनर्ग्रहित कर सकते हैं। परिबद्ध अवधारण के लिए O(1) बनाम Ω(t) की एक तीव्र द्विभाजिका सिद्ध करता है। अनुभवजन्य रूप से सत्यापित (238 गुना रीसायकल-दर अंतर)।
[Explore the project](https://github.com/blackwell-systems/drainability)

**Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18671870-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18671870)
सुस्थापित क्षतिपूर्ति के माध्यम से समन्वय-मुक्त अभिसरण। CRDT और इन्वेरिएंट कॉन्फ़्लुएंस के साथ-साथ तीसरा अभिसरण नियम।
[Explore the project](https://github.com/blackwell-systems/normalization-confluence)

**Federated Normalization Confluence** [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18677400-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.18677400)
अचक्रीय नेटवर्कों पर मॉर्फ़िज़्म वैधता संरक्षण के माध्यम से बहु-संगठनात्मक अभिसरण।

---

### अपस्ट्रीम योगदान

पूरे इकोसिस्टम में 40+ मर्ज किए गए PR। [mcp-go](https://github.com/mark3labs/mcp-go) (8.7K stars) में #6 योगदानकर्ता।
डेटा भ्रष्टाचार सुधार, panic रिकवरी, SDK सुदृढ़ीकरण, स्पेक अनुपालन, ट्रांसपोर्ट बग।

| संगठन | क्या | Stars |
|:---|:---|---:|
| **Google** | Chrome DevTools MCP (GCF फ़ॉर्मैट), go-containerregistry | 47K |
| **Anthropic** | MCP Go, Python, PHP SDK + सर्वर | 85K+ |
| **LangChain** | langchain (टेक्स्ट स्प्लिटर सुधार) | 136K |
| **etcd** | CNCF gRPC एरर कोड सुधार (समीक्षाधीन) | 51K |
| **Charmbracelet** | bubbletea, huh | 42K |
| **GitHub** | github-mcp-server | 16K |
| **HashiCorp** | terraform-provider-aws (GovCloud सुधार) | 10.9K |
| **pypa** | pip (locale एन्कोडिंग सुधार) | 10.2K |
| **mark3labs** | mcp-go SDK (9 PR, #6 योगदानकर्ता) | 8.7K |
| **Ant Group** | mcp-server-chart (9 बग सुधार) | 4K |
| **Grafana** | mcp-grafana (3 PR मर्ज किए गए) | 2.9K |

[Full list](https://blog.blackwell-systems.com/oss#upstream-contributions)

---

### तकनीकी पृष्ठभूमि

भाषाएँ:

![C](https://img.shields.io/badge/Systems_Programming-292c34?logo=c&logoColor=white&labelColor=1a1d22&style=for-the-badge)
![Go](https://img.shields.io/badge/Go-%F0%9F%90%B9-292c34?logo=go&logoColor=white&style=for-the-badge)
![Rust](https://img.shields.io/badge/Rust-%F0%9F%A6%80-292c34?logo=rust&logoColor=white&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-%F0%9F%90%8D-292c34?logo=python&logoColor=ffdd54&style=for-the-badge)
![Java](https://img.shields.io/badge/Java-%E2%98%95-292c34?logo=openjdk&logoColor=white&style=for-the-badge)
![Node.js](https://img.shields.io/badge/Node.js-292c34?logo=nodedotjs&logoColor=white&style=for-the-badge)

प्लेटफ़ॉर्म और शेल:

![Platform](https://img.shields.io/badge/Platform-%F0%9F%8D%8E%20macOS%20%7C%20%F0%9F%90%A7%20Linux%20%7C%20%F0%9F%AA%9F%20WSL-292c34?style=for-the-badge)
![Zsh](https://img.shields.io/badge/Zsh-292c34?logo=zsh&logoColor=white&style=for-the-badge)
![Bash](https://img.shields.io/badge/Bash-292c34?logo=gnubash&logoColor=white&style=for-the-badge)
![PowerShell](https://img.shields.io/badge/PowerShell-6b7280?logo=powershell&logoColor=white&style=for-the-badge)

डेवलपर टूलिंग:

![Git](https://img.shields.io/badge/Git-%F0%9F%94%A7-292c34?logo=git&logoColor=6fa2c9&style=for-the-badge)
![Terraform](https://img.shields.io/badge/Terraform-292c34?logo=terraform&logoColor=6fa2c9&style=for-the-badge)
![AWS%20CDK](https://img.shields.io/badge/AWS%20CDK-292c34?logo=amazonaws&logoColor=6fa2c9&style=for-the-badge)
![Datadog](https://img.shields.io/badge/Datadog-292c34?logo=datadog&logoColor=6fa2c9&style=for-the-badge)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-292c34?logo=opentelemetry&logoColor=6fa2c9&style=for-the-badge)
![Containers](https://img.shields.io/badge/Containers-%F0%9F%90%B3%20Docker-292c34?logo=docker&logoColor=6fa2c9&style=for-the-badge)
![GCP](https://img.shields.io/badge/Google%20Cloud-292c34?logo=googlecloud&logoColor=6fa2c9&style=for-the-badge)

कृत्रिम बुद्धिमत्ता:

[![GPT](https://img.shields.io/badge/GPT-%F0%9F%A4%96%20OpenAI-292c34?logo=openai&logoColor=6fa2c9&style=for-the-badge)](https://openai.com/)
[![Claude](https://img.shields.io/badge/Claude-%F0%9F%A7%A0%20Anthropic-292c34?logo=anthropic&logoColor=6fa2c9&style=for-the-badge)](https://www.anthropic.com/)
[![Gemini](https://img.shields.io/badge/Gemini-%E2%9C%A8%20Google-292c34?logo=googlegemini&logoColor=6fa2c9&style=for-the-badge)](https://deepmind.google/technologies/gemini/)
