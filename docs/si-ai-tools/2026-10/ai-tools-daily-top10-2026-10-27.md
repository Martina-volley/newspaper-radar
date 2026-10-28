# SI 的 AI 工具選報

更新日期：2026-10-27（Asia/Taipei）

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 1 | [Claude for Nonprofits 外掛](https://claude.com/resources/articles/expanding-claude-for-nonprofits) | Anthropic 於 10/26 推出面向經驗證非營利組織的 Claude 外掛，內含募款研究與提案、行銷、人事及董事會工作流程，也能依組織政策回答員工可否在特定情境使用 AI。外掛由約 30 個非營利組織共同設計，重點是把組織背景、政策和常用任務帶進日常工作；這是供應商介紹的功能與案例，實際可用技能、資料連接和組織資格仍需在帳戶中確認。若適用，可先用公開募款資料測試來源引用，再檢查內部捐款資料權限與政策回答是否正確。 |
| 2 | [GPT-6.1 Terra 登上 GitHub Copilot](https://github.blog/changelog/2026-10-26-gpt-6-1-terra-in-github-copilot/) | GitHub 於 10/26 將 OpenAI 的 GPT-6.1 Terra 加入 Copilot，供日常代理程式開發與終端工作使用；官方定位是比 GPT-6.1 Sol 成本低，並稱早期測試在終端和 C# 任務中較 GPT-5.6 Terra 解出更多題目。模型按供應商牌價採用量計費，正分批向 Pro、Pro+、Max、Business 與 Enterprise 推出，企業管理員可由模型政策控制。GitHub 未在公告交代比較方法與任務數；可用固定的終端操作及 C# 任務比較完成率、修正次數、延遲和實際費用。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 3 | [Gemini API：新付費專案預設儲存請求](https://ai.google.dev/gemini-api/docs/changelog) | Google 於 10/26 調整 Gemini API 的 Generate Content：新建的付費專案預設會儲存請求（`store=true`），與 Interactions API 的行為一致；既有專案設定不變。開發者可對個別請求設 `store=false`，或在 AI Studio Logs and Datasets 關閉 Generate Content API 記錄。若系統會送出個資、機密提示或客戶內容，應先確認專案建立日期、請求參數和記錄設定，再測試日誌中實際留下哪些資料。 |
| 4 | [ChatGPT 自訂 GPT 轉移至外掛的時程](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq) | OpenAI 的更新說明指出，自訂 GPT 將逐步轉移到外掛：受影響的 Enterprise 工作區已自 10/26 停止建立新 GPT（FedRAMP 除外），既有 GPT 標準退役日為 12/11，符合條件並獲核准延後的工作區可至 2027/2/11。遷移後原 GPT 會變成唯讀；指示與知識檔可轉入外掛，但自訂 Actions 不會自動轉移，且新外掛預設為私人。GPT 建立者可先盤點常用工作流程與 Actions，等待帳戶開放遷移後用熟悉提示測試替代外掛及分享權限。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 5 | [CodeRabbit Secure 採用 GPT-6.1 Sol](https://openai.com/index/gpt-6-1-sol-coderabbit-code-security/) | OpenAI 於 10/26 介紹 CodeRabbit 將 GPT-6.1 Sol 用於安全代理，協助跨檔案、相依套件與相連程式庫分析 PR 風險；CodeRabbit Secure 也能在隔離沙箱嘗試驗證使用者選定的發現，並為支援的問題草擬修補 PR。這是供應商發布的客戶案例，系統還結合其他模型與安全工具，並非只靠單一模型完成掃描；正式修補仍須人工審查。可先在測試倉庫檢查誤報、沙箱隔離、跨倉庫權限和修補後測試結果。 |
| 6 | [Fanatics 上線 Shop the Look 商品搭配推薦](https://openai.com/index/fanatics-streamline-fan-experience/) | Fanatics 於 10/26 在旗下多個商店網站上線 AI 商品搭配功能：消費者瀏覽球衣時，可看到依球隊、庫存和風格搭配的商品建議，清單會隨目錄每日更新。OpenAI 稱此體驗在約 30,000 項 MLB 商品測試中，互動率比舊版高 10%；這是合作雙方公布的單一案例數據，不代表其他零售目錄也會得到相同提升。可留意推薦是否受庫存與品牌規則約束，並用自家商品分類測量點擊、加購和退貨等完整指標。 |

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| AI 工作流程開始包裝成產業或組織專用能力 | [Claude for Nonprofits](#item-01)、[ChatGPT 自訂 GPT 遷移](#item-04)、[Fanatics Shop the Look](#item-06) | 非營利外掛與零售推薦把通用模型接上特定資料和任務，而自訂 GPT 遷移則要求既有工作流程重新檢查指示、工具和分享方式。 | 比對資料權限、來源可追溯性、替代工作流程的行為，以及使用者是否仍能取得原有功能。 |
| 模型表現之外，部署設定與驗證流程更重要 | [GPT-6.1 Terra](#item-02)、[Gemini API 儲存預設](#item-03)、[CodeRabbit Secure](#item-05) | 新模型選擇、API 請求記錄和程式碼安全代理各自帶來不同的成本或資料風險，採用時不能只看模型能力。 | 核實計費與模型政策、專案儲存設定、日誌內容、沙箱隔離和人工核准點。 |

## 來源

- [Anthropic：Expanding Claude for Nonprofits](https://claude.com/resources/articles/expanding-claude-for-nonprofits)
- [GitHub Changelog：GPT-6.1 Terra in GitHub Copilot](https://github.blog/changelog/2026-10-26-gpt-6-1-terra-in-github-copilot/)
- [Google AI for Developers：Gemini API Release notes](https://ai.google.dev/gemini-api/docs/changelog)
- [OpenAI Help Center：Custom GPT retirement and migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq)
- [OpenAI：GPT-6.1 Sol helps CodeRabbit strengthen security across complex codebases](https://openai.com/index/gpt-6-1-sol-coderabbit-code-security/)
- [OpenAI：How Fanatics and OpenAI streamline the fan experience](https://openai.com/index/fanatics-streamline-fan-experience/)
