# SI 的 AI 工具選報

更新日期：2026-11-13（Asia/Taipei）

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 1 | [Gemini 4 Hydrogen：面向日常代理工作的新模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) | Google 於 11/12 發布 Gemini 4 Hydrogen，定位為快速執行日常編碼與代理任務的模型，可透過 Gemini API、AI Studio、Gemini for business 和 Gemini App 等管道使用；Search 也同步升級至 Hydrogen。Google 宣稱模型在多項自家評測中改善速度、代理任務表現與安全性，這些數據尚非獨立重現。團隊可先以固定的編碼、工具呼叫及受阻任務集比較成功率、延遲、token 用量與越權行為，再評估是否適合作為日常執行模型。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 2 | [Gemini Decisions API：一次完成多項封閉式判斷](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) | Google 於 11/11 發布 Gemini Decisions API 與 Gemini Decision 1，讓開發者用一次多模態輸入，提出最多 1,000 個是非、選項或評分問題，取得各答案的機率與信心分數。Google 標示延遲約 150–250 毫秒，輸入每百萬 token 0.10 美元且不計輸出 token；這些速度與成本資訊來自供應商，實際結果仍受問題設計、輸入長度與服務負載影響。它適合路由、政策檢查、分類或評分，不取代需要生成說明或處理開放式問題的模型；導入前可用標記資料測量準確率、校準度與錯誤決策成本。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---|---|---|

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| 代理系統開始把「思考與執行」和「快速判斷」分開處理 | [Gemini 4 Hydrogen](#item-01) · [Gemini Decisions API](#item-02) | Hydrogen 負責較完整的生成與多步驟工作，Decisions API 則針對有限選項快速評分；將工作交給合適的模型層，可能減少不必要的文字生成與等待，但需先證明路由正確且成本確實下降。 | 以相同任務集比較路由準確率、端到端延遲、總 token 費用及錯誤代價；特別檢查低信心結果是否能升級交由 Hydrogen 或人工處理。 |

## 來源

- [Google：Introducing Gemini 4 Hydrogen（2026-11-12）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)
- [Google：Gemini Decisions API: Fast, calibrated multimodal decisions（2026-11-11）](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)
