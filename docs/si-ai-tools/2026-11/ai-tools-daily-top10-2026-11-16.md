# SI 的 AI 工具選報

更新日期：2026-11-16（Asia/Taipei）

週末回看：近期具操作影響的官方更新集中於 11/13；另將今天生效的 Copilot 模型退役列入焦點，並標明原公告日期。

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 1 | [GitHub Copilot 模型退役：11/16 生效，另有 12/14 遷移時程](https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november/) | GitHub 10/15 公告的第一批退役於今天生效：Copilot 的 Claude Opus 4.8、Claude Opus 5 與 GPT-5.6 Terra 於 11/16 停用；Opus 4.8 仍保留給年繳個人訂閱者。企業與商務方案可用替代模型分別是 Opus 5.5，以及 GPT-6.1 Sol 或 GPT-6 Luna，管理員需確認模型政策已允許。GitHub 11/13 又公布第二批模型將於 12/14 退役。正在使用相關模型的團隊今天應先檢查自動化工作流、模型政策與替代模型輸出；退役後不需另行手動移除。

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 2 | [Gemini 4 Hydrogen 正式加入 GitHub Copilot](https://github.blog/changelog/2026-11-13-gemini-4-hydrogen-in-github-copilot/) | GitHub 於 11/13 將 Gemini 4 Hydrogen 一般提供給 Copilot Pro、Pro+、Max、Business 與 Enterprise 使用者，逐步開放至 VS Code、Visual Studio、CLI、Coding Agent、Copilot App、JetBrains、Xcode 等介面。使用量依供應商牌價計費；企業管理員可透過模型政策控管存取。這是 Hydrogen 新增 Copilot 通路，並非本期重述 11/12 的模型發布。導入前應確認帳戶是否已開放及計費方式，再用既有任務比較品質、延遲和用量。 |
| 3 | [Cloudflare Kitesurf：代理瀏覽器引擎以 Apache 2.0 開源](https://blog.cloudflare.com/kitesurf-open-source) | Cloudflare 於 11/13 開放 Kitesurf 原始碼，採 Apache 2.0 授權；這套無狀態瀏覽器引擎以 Workers 執行，可解析 HTML、套用 CSS、執行 JavaScript、輸出畫面，並支援 Chrome DevTools Protocol，可自行執行或部署到 Cloudflare Workers。Cloudflare 同時說明引擎仍在積極開發，網頁標準相容性與可靠度還會改善。適合評估自架代理瀏覽環境的團隊，可先對照常用網站的渲染、登入狀態、腳本操作和失敗復原，不宜先假設能取代完整 Chrome。 |
| 4 | [llama.cpp 與 ggml 發布 v1.0.0](https://huggingface.co/blog/ggml-org/llama-cpp-v1) | ggml-org 於 11/13 發布 llama.cpp 與底層張量函式庫 ggml 的 1.0.0，並承諾未來公開 C API 的不相容變更會透過主版本號標示。這是維護與下游相容性規則的里程碑，不表示所有使用端升級都不會遇到破壞性變更；團隊仍須檢查先前移除或淘汰的介面。維護整合套件者應先固定目前版本，在 CI 跑編譯、推論與硬體後端測試，再安排升級。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 5 | [GitHub AI Scan：可透過 REST API 管理整個儲存庫掃描](https://github.blog/changelog/2026-11-13-manage-ai-scan-for-repositories-using-the-rest-api/) | GitHub 於 11/13 在公開預覽中新增 `repository_scan` 設定，讓組織或儲存庫管理者透過 REST API 開關 AI Scan。啟用設定不會立即開始掃描；有寫入權限的使用者仍須手動啟動，每次掃描會消耗 GitHub Code Security AI credits。適用範圍依儲存庫可見性與安全方案而異，GitHub Enterprise Server 不支援。可先用測試儲存庫驗證繼承／個別停用規則、422 權限回應與費用流程。 |
| 6 | [GitHub Copilot App 一般支援 GitHub Enterprise Server](https://github.blog/changelog/2026-11-13-github-enterprise-server-support-in-the-github-copilot-app/) | GitHub 於 11/13 將 Copilot App 連接 GHES 的功能轉為一般提供，使用者可在 App 中處理遠端儲存庫、Issue 與 Pull Request；需使用 1.2.0 以上版本，並先登入 GitHub.com 或 GHE.com 帳戶。GHES 不支援 cloud sessions，因此不能把雲端工作階段的能力一併視為可用。採用前應在實際企業伺服器確認登入、儲存庫權限及功能邊界。 |

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| 代理工作流程逐漸有明確的維運與權限控制 | [Copilot 模型退役](#item-01) · [Gemini 4 Hydrogen in Copilot](#item-02) · [GitHub AI Scan API](#item-05) · [Copilot App for GHES](#item-06) | Copilot 同時調整模型供應、企業內部伺服器連接與安全掃描開關；導入代理的管理工作已從挑選模型延伸到遷移時程、權限政策和實際費用。 | 核對模型退役日期與替代方案；用測試組織確認模型政策、GHES 功能限制、AI Scan 權限繼承及掃描費用。 |
| 代理基礎設施朝可自行檢視、部署與維護發展 | [Cloudflare Kitesurf](#item-03) · [llama.cpp／ggml v1.0.0](#item-04) | Kitesurf 開放代理瀏覽引擎供自行部署，llama.cpp 則以主版本規則管理本地推論 API 相容性；自行掌握執行環境也意味著團隊要承擔瀏覽器相容性與升版驗證。 | 用真實頁面測試 Kitesurf 的標準相容性和故障復原；在 llama.cpp 升級前以固定模型、硬體後端和 API 呼叫跑回歸檢查。 |

## 來源

- [GitHub Changelog：Upcoming deprecation of selected GitHub Copilot models in mid-November（2026-10-15）](https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november/)
- [GitHub Changelog：Upcoming deprecation of selected GitHub Copilot models in December（2026-11-13）](https://github.blog/changelog/2026-11-13-upcoming-deprecation-of-selected-github-copilot-models-in-december/)
- [GitHub Changelog：Gemini 4 Hydrogen in GitHub Copilot（2026-11-13）](https://github.blog/changelog/2026-11-13-gemini-4-hydrogen-in-github-copilot/)
- [Cloudflare Blog：Kitesurf is now open source（2026-11-13）](https://blog.cloudflare.com/kitesurf-open-source)
- [ggml-org：llama.cpp v1.0.0（2026-11-13）](https://huggingface.co/blog/ggml-org/llama-cpp-v1)
- [GitHub Changelog：Manage AI Scan for repositories using the REST API（2026-11-13）](https://github.blog/changelog/2026-11-13-manage-ai-scan-for-repositories-using-the-rest-api/)
- [GitHub Changelog：GitHub Enterprise Server support in the GitHub Copilot app（2026-11-13）](https://github.blog/changelog/2026-11-13-github-enterprise-server-support-in-the-github-copilot-app/)
