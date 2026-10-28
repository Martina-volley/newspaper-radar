# SI 的 AI 工具選報

更新日期：2026-10-28（Asia/Taipei）

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 1 | [Liquid AI LFM3 小型多模態模型家族](https://huggingface.co/blog/LiquidAI/lfm3) | Liquid AI 於 10/27 開放六款約 2B 級模型，涵蓋文字、影像與影片、語音、視聽整合，以及能輸出機率的決策模型；權重已可從 Hugging Face 取得。文字模型主打本機代理、工具呼叫與 256K context，4-bit 約需 1 GB 記憶體，但採 LFM Open License，不是 Apache 或 MIT。效能數據由 Liquid AI 公布，模型卡也提醒小模型不適合複雜多步推理與代理程式設計；可先依授權及硬體限制，測試自家任務的正確率、延遲和工具呼叫穩定度。 |
| 2 | [OpenAI 與 Oracle 擴大企業 AI 合作](https://openai.com/index/oracle-apps-in-chatgpt/) | OpenAI 與 Oracle 於 10/27 宣布把 Oracle 應用與資料帶進 ChatGPT，並推出或規劃 AI Security Mesh、AI Workspace、App Composer 與中小企業方案。Oracle AI Workspace 仍在開發中；Oracle 也註明功能、時程與價格可能改變。美國 Oracle 客戶可透過 Marketplace 採購 OpenAI API、Codex 和 ChatGPT Work。評估企業流程前，應確認產品實際開放狀態、資料權限、核准機制，以及應用部署和使用成本。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 3 | [Microsoft MAI Image 2.7 圖像編修預覽](https://microsoft.ai/news/mai-image-2-7-debut/) | Microsoft AI 於 10/27 開放 MAI Image 2.7 預覽，可重塑場景風格、調整光線、修改圖片內文字或符號，並修復既有素材；目前可在 MAI Playground 等指定入口試用，文字生成圖片功能尚未推出。Microsoft 引述 Artificial Analysis 評估稱模型在多種編修項目都有進步，這是特定評測結果，不能直接代表各類設計工作。可用同一組商品圖和品牌素材測試局部修改是否保留構圖、文字與細節。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| 小型模型按任務拆分，多模態工具也走向專用化 | [Liquid AI LFM3](#item-01)、[MAI Image 2.7](#item-03) | LFM3 以不同小模型分工處理文字、視聽與結構化判斷，MAI Image 2.7 則集中改進圖片編修，反映工具更傾向針對明確任務設計。 | 以自有資料測試品質、速度、硬體需求、授權和編修可控度。 |
| 代理從回答問題走向操作企業流程 | [OpenAI 與 Oracle 合作](#item-02)、[Liquid AI LFM3](#item-01) | Oracle 將 AI 接到企業應用及核准流程，LFM3 則提供可本機部署並呼叫工具的小模型；兩者分別處理組織層與裝置端的代理落地。 | 檢查資料與工具權限、人工核准、執行紀錄、模型失誤時的停止與回復方式。 |

## 來源

- [Liquid AI 與 Hugging Face：Build specialized multimodal models with LFM3（2026-10-27）](https://huggingface.co/blog/LiquidAI/lfm3)
- [Liquid AI：Introducing LFM3: Every Modality for Specialized Intelligence（2026-10-27）](https://www.liquid.ai/blog/lfm3)
- [Hugging Face：LiquidAI/LFM3-1.7B 模型卡與授權](https://huggingface.co/LiquidAI/LFM3-1.7B)
- [OpenAI：OpenAI expands partnership with Oracle to bring its apps to ChatGPT（2026-10-27）](https://openai.com/index/oracle-apps-in-chatgpt/)
- [Oracle：Oracle and OpenAI: Put frontier AI to work for your business（2026-10-27）](https://blogs.oracle.com/ai-and-datascience/oracle-openai)
- [Microsoft AI：MAI Image 2.7 debuts above GPT Image 2.5 Flare on Artificial Analysis and #3 on Arena（2026-10-27）](https://microsoft.ai/news/mai-image-2-7-debut/)
