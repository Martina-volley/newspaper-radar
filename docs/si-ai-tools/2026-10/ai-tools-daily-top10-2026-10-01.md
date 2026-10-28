# AI 工具日報 - Top 10

更新日期：2026-10-01（Asia/Taipei）

## Highlight

| # | 工具／模型 | 近期動態與觀察 |
|---:|---|---|
| 1 | [GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol/) | OpenAI 9/29 發布 GPT-6.1 Sol，主打接近 GPT-6 Astra 的 agentic coding、computer use 與專業工作能力，標準 token 價格約為 Astra 的五分之一；這是今日最直接的能力／成本重新定價訊號。 |
| 2 | [Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5) | Anthropic 9/28 發布 Sonnet 5.5，官方稱速度提升 30% 以上、多數工作成本最多低 30%，並以 Terminal-Bench 4.0 的 agentic coding 表現切入日常 coding 與文件工作。 |
| 3 | [OpenAI Agents API（含 computer use）](https://openai.com/index/devday-2026-recap/) | OpenAI 9/29 將 computer use、tool search、tool calling、context compaction 與 multi-agent 能力帶入 Agents API；agent 開發的基本單位正從 prompt chain 轉成可受管的長任務 runtime。 |

## Middle

| # | 工具／模型 | 近期動態與觀察 |
|---:|---|---|
| 4 | [OpenAI Dots](https://openai.com/index/devday-2026-recap/) | 9/29 發布的 always-on agent，可持續承擔責任並結合 ChatGPT Space、插件與團隊協作；因前一份日報已出現，本日列 Middle，重點是持續狀態、權限與人工接管。 |
| 5 | [VectifyAI PageIndex v0.2.20](https://github.com/VectifyAI/PageIndex/releases) | 官方 9/28 釋出 v0.2.20，加入更快的 Flash indexing、local／cloud 一致 SDK 與 agent tools；它把向量檢索替換成對文件樹的推理，適合測試長 PDF 的召回品質與可解釋性。 |
| 6 | [Gemini 3.8 Live with Live Avatar](https://deepmind.google/blog/) | Google DeepMind 9 月新增 Live Avatar，延續 Gemini 3.8 Live 與 Extended Thinking 的即時多模態路線；因近期報告已多次出現 Gemini Live，本日只列 Middle，應比較延遲、打斷恢復與工具成功率。 |

## Also Notable

| # | 工具／模型 | 近期動態與觀察 |
|---:|---|---|
| 7 | [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) | GitHub 9/30 趨勢快照顯示其為 agent sandbox 的強勢訊號，並有 9/29–10/1 的 milestone 節奏；它以宣告式 policy 限制檔案、網路與 process，適合做 runtime security spike。 |
| 8 | [Rocketride Server](https://github.com/rocketride-org/rocketride-server) | 9/23–9/30 快照顯示本週增加約 8,308 stars，為本週 AI repo 加速最快項目之一；C++ 核心、可擴充節點與多模型 provider 組合成可部署 pipeline，但仍需驗證隔離與長流程回復。 |
| 9 | [DreamNum Univer](https://github.com/dream-num/univer) | GitHub 官方組織頁顯示 repo 9/29 仍有更新，定位為讓 AI agents 操作試算表、文件、簡報、畫布與 relational tables 的 Office harness；值得測試版本化變更、審查與 rollback。 |
| 10 | [Google Private AI Compute secure server-side memory](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/) | Google 9/23 公布跨裝置持久記憶的 Private AI Compute 架構，將連續性與隱私邊界放在同一設計；它不是單一工具，但會影響長期 agent 的資料位置、加密與可驗證治理。 |

## 本日趨勢總結

| 趨勢 | 今日觀察 | 對團隊的意義 |
|---|---|---|
| 能力／成本重新分層 | GPT-6.1 Sol 與 Sonnet 5.5 同週把高能力、低成本與更快吞吐推到產品主線。 | 模型評估要同時記錄任務成功率、token、延遲、快取命中率與每次任務成本。 |
| Agent 進入受管 runtime | Agents API、Dots 與 OpenShell 分別處理工具、長任務、sandbox 與政策。 | 驗收條件應包含狀態恢復、網路／檔案邊界、人工核准、審計與停止機制。 |
| 文件與 Office 成為 agent 執行面 | PageIndex 對文件樹推理，Univer 對試算表／文件／簡報提供可操作工作區。 | 高價值測試要保留來源、版本差異、權限、rollback 與人類 review 證據。 |
| 記憶從便利性走向隱私架構 | Private AI Compute 將跨裝置長期記憶與隱私計算一起產品化。 | 設計 memory 時需明確定義租戶隔離、刪除、加密、資料留存與跨裝置同步邊界。 |

## 資料來源

- [OpenAI DevDay 2026 Recap](https://openai.com/index/devday-2026-recap/)
- [OpenAI GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol/)
- [Anthropic Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)
- [VectifyAI PageIndex releases](https://github.com/VectifyAI/PageIndex/releases)
- [GitHub AI trending snapshot](https://whatstrending.ai/repos)
- [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell)
- [DreamNum GitHub organization](https://github.com/dream-num)
- [Google Private AI Compute](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/)
