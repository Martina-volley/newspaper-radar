# SI 的 AI 工具選報

更新日期：2026-10-30（Asia/Taipei）

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 1 | [Gemini 4 Carbon：長程工程與資安模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) | Google DeepMind 於 10/28 發表 Gemini 4 Carbon，主打長程工程任務與資安防禦，並公布漏洞發現、利用驗證及修補等基準成績；這些數字是 Google 援引的特定評測結果。Carbon 目前先提供給部分資安防禦者，再逐步擴至可信任夥伴，尚未向一般開發者與消費者開放。若屬初期測試對象，可用隔離環境檢查多步程式任務的完成率、越權風險與人工覆核成本。 |
| 2 | [GPT-6 Luna（10/28 版）](https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum) | OpenAI 於 10/29 發布系統卡增補，說明 GPT-6 Luna 更新後回覆更精簡，並減少過度附和；依 Preparedness Framework，官方將此版本的資安及生物化學能力評為 High，並沿用前版的防護架構。公告沒有提供完整的產品 rollout 細節，也不能只憑系統卡判定每位使用者已拿到更新。可用既有提示集比較回答長度、拒答與指令遵循，再確認實際帳戶版本。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 3 | [Palantir Foundry Pilot 正式版](https://www.palantir.com/docs/docs/foundry/announcements) | Palantir 於 10/29 將 Pilot 轉為正式版：使用者可用自然語言建立連接 Foundry Ontology 的 React 應用或 Workshop 小工具，在即時預覽中修整，再透過導引流程部署。它把介面建置、資料模型與部署放在同一工作區；正式版可用範圍仍取決於 Foundry 租戶與權限。導入前應以測試資料確認產生的資料操作、Ontology 權限、部署審核與版本回復方式。 |
| 4 | [ChatGPT 的 dot 開始支援簡訊互動](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) | OpenAI 於 10/28 開始向美國 Pro 使用者 beta 推出以 iMessage 或 RCS 傳訊給 dot；dot 也能主動傳送可能相關的更新，並沿用 ChatGPT app 中的記憶與外掛。此功能尚非全球開放，且訊息由第三方 Linq 傳送；OpenAI 說明 dot 只能與帳戶本人互傳，不會因此取得其他簡訊對話。可先檢查帳戶資格、記憶與外掛內容，以及第三方訊息服務的資料處理方式。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 5 | [OpenAI 更新 Model Spec 行為指引](https://openai.com/index/updated-model-spec/) | OpenAI 於 10/29 將 Model Spec 依照忠於人類意圖、減少傷害、誠實透明、支持自主與關懷五項價值重新整理，也補入脈絡、監督和自主性指引。這是模型行為的公開目標與規範，不等於目前所有已部署模型都已完全符合；OpenAI 也明確表示模型尚未完全反映這份規格。團隊可用實際任務檢查指引如何處理脈絡、使用者選擇與副作用，再與產品現況分開評估。 |
| 6 | [Claude Haiku 4.5 從部分方案的模型選單退場](https://support.claude.com/en/articles/17444146-claude-haiku-4-5-was-removed-from-the-model-selector) | Anthropic 原於 10/15 預告，並已在 10/29 將 Haiku 4.5 從 Free、Pro、Max 方案的 Claude chat、Cowork 和 Design 模型選單移除，由 Haiku 5.5 取代；Claude Code、Team、Enterprise 與 API 不受此次變更影響，既有對話也未刪除。延續舊對話時會改由 Haiku 5.5 回覆。若依賴舊版結果，可保存代表性提示並比較替換後的品質、速度與成本。 |
| 7 | [GPT-6.1 Terra 加入 Palantir AIP 實驗模型](https://www.palantir.com/docs/docs/foundry/announcements) | Palantir 於 10/29 開放符合資格的商用 AIP 租戶，透過 Azure OpenAI 或 Direct OpenAI 試用 GPT-6.1 Terra；美國地理限制租戶目前列出的入口是 Direct OpenAI。模型支援文字、影像、結構化輸出及 Responses API 工具呼叫，但仍屬實驗性模型，管理員須啟用模型家族與實驗模型設定。採用前先確認租戶資格、服務商、資料區域及 token 費用，再用固定任務比較輸出和工具呼叫可靠度。 |

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| 能力提升同時要求更明確的任務邊界 | [Gemini 4 Carbon](#item-01)、[GPT-6 Luna](#item-02)、[OpenAI Model Spec](#item-05) | Carbon 強調長程工程與資安，Luna 調整回答方式，而 Model Spec 把意圖、監督與自主性寫得更清楚；能力、回應風格和行為原則正一起演進。 | 用代表性任務測試持續執行、指令遵循、越權與不確定性表達，並分清規格目標和現行模型行為。 |
| AI 開始從工作台延伸到可部署介面與持續通訊 | [Palantir Foundry Pilot](#item-03)、[ChatGPT dot 簡訊](#item-04) | Pilot 把提示轉成可部署的業務介面，dot 則把助理帶進簡訊並主動傳送更新；兩者都讓 AI 在單次對話之外延續工作。 | 檢查部署權限、資料連線、主動通知控制、外部服務商與使用者撤回方式。 |
| 版本更新不只新增功能，也會改變既有工作流程 | [GPT-6.1 Terra in AIP](#item-07)、[Claude Haiku 4.5 退場](#item-06) | Terra 擴大可選模型，但仍受租戶與實驗設定限制；Haiku 4.5 則已從部分方案選單移除，提醒團隊同時追蹤新模型入口與舊版退場。 | 盤點方案、地區、管理員設定及 API 狀態，並用固定測試集驗證模型切換前後的差異。 |

## 來源

- [Google：Introducing Gemini 4 Carbon（2026-10-28）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)
- [OpenAI Deployment Safety Hub：GPT-6 Luna October 28 update（發布於 2026-10-29）](https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum)
- [Palantir Foundry：October 2026 announcements（含 2026-10-29 Pilot GA 與 GPT-6.1 Terra AIP 更新）](https://www.palantir.com/docs/docs/foundry/announcements)
- [OpenAI Help Center：ChatGPT release notes（2026-10-28 dot beta）](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [OpenAI：An updated Model Spec for more capable and beneficial AI（2026-10-29）](https://openai.com/index/updated-model-spec/)
- [Claude Help Center：Claude Haiku 4.5 was removed from the model selector（2026-10-29 生效）](https://support.claude.com/en/articles/17444146-claude-haiku-4-5-was-removed-from-the-model-selector)
