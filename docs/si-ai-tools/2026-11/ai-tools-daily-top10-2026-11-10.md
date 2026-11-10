# SI 的 AI 工具選報

更新日期：2026-11-10（Asia/Taipei）

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 1 | [Claude Fable 5.2 與 Mythos 5.2：技術模型升級、分級開放](https://www.anthropic.com/claude-fable-and-mythos-5-2) | Anthropic 於 11/9 發布 Fable 5.2 與 Mythos 5.2：兩者使用相同底層模型，但 Fable 保留資安與生物學防護、提供一般使用者；Mythos 則限通過審核的資安及生命科學研究機構申請。Fable 已可在 Claude 各平台及 API 使用。Anthropic 表示模型在多項自家評測中提升，標準價為每百萬輸入 token 8 美元、輸出 40 美元；可選 Fast mode，價格加倍。效能、案例與安全比較均由 Anthropic 提供，尚非獨立重現。團隊可用固定程式與多模態任務比較品質、速度、成本及防護誤擋，再確認所需模型的申請資格。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 2 | [ChatGPT Enterprise 上架 AWS Marketplace](https://openai.com/index/chatgpt-enterprise-aws-marketplace/) | OpenAI 於 11/9 開放透過 AWS Marketplace 採購 ChatGPT Enterprise，企業可沿用現有 AWS 採購與帳務流程，符合條件的支出也可計入 AWS 承諾額度。公告稱產品功能與直接向 OpenAI 購買一致；Healthcare 與 Financial Services 版本也可由符合資格的客戶洽詢。上架簡化採購，但是否能抵扣承諾額度及適用資格仍需向 OpenAI 或 AWS 確認。採購前可比對合約、資料區域、管理功能與實際計費方式。 |
| 3 | [OpenAI Control Room：追蹤並停止研究模型工作負載](https://openai.com/index/introducing-control-room/) | OpenAI 於 11/9 說明其研究基礎設施已部署 Control Room，為訓練、評測及資料處理等工作分配識別碼，並在推論層檢查工作是否仍獲授權；人員或監測系統下令停止後，官方表示最遲 35 秒可中止後續模型輸出。服務失效時採 fail-closed，拒絕新的推論請求；其餘研究工作負載仍在逐步佈署。這是 OpenAI 內部系統，並非對外產品，效能和完整覆蓋率目前由 OpenAI 自述。設計類似管控的團隊可檢查停止延遲、授權檢查是否位於可信執行層，以及控制服務故障時的處置。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 4 | [CodeRabbit × Codex：客戶稱軟體交付量提高 20 倍](https://openai.com/index/coderabbit-codex-daybreak/) | OpenAI 於 11/9 發布 CodeRabbit 客戶案例：CodeRabbit 以自家工具檢查 AI 產生的程式碼，並稱使用 Codex 後，同一工程團隊近半年交付的軟體量約為原先 20 倍；該數字是 CodeRabbit 受訪者估計，未附可獨立重現的計算方法。案例也指出，多代理增加後，團隊須重新整理測試、發版與人工核准流程。可借鏡其做法，先以固定期間記錄合併量、缺陷率、審查時間與回復成本，再評估產出增加是否帶來實際價值。 |

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| 模型與代理擴大工作範圍，授權、採購和品質控制需同步 | [Claude Fable／Mythos 5.2](#item-01) · [ChatGPT Enterprise on AWS](#item-02) · [OpenAI Control Room](#item-03) · [CodeRabbit × Codex](#item-04) | Claude 依模型防護與資格區分存取，Control Room 在研究執行時保留中止能力，CodeRabbit 則為大量代理產出的程式碼加上審查；Marketplace 降低企業採購摩擦，這些措施分別處理權限、執行控制、品質與部署通路。 | 核對模型資格與防護誤擋；確認採購和資料條款；量測停止延遲及故障處理；以缺陷率和人工審查成本檢查交付量變化。 |

## 來源

- [Anthropic：Claude Fable 5.2 and Mythos 5.2（2026-11-09）](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- [OpenAI：ChatGPT Enterprise now available in AWS Marketplace（2026-11-09）](https://openai.com/index/chatgpt-enterprise-aws-marketplace/)
- [OpenAI：Introducing Control Room: Human control over AI workloads（2026-11-09）](https://openai.com/index/introducing-control-room/)
- [OpenAI：CodeRabbit scales agentic software development and ships 20x more（2026-11-09）](https://openai.com/index/coderabbit-codex-daybreak/)
