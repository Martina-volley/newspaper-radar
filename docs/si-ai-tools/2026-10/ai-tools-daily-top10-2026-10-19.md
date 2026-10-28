# SI 的 AI 工具選報

更新日期：2026-10-19（Asia/Taipei）

觀察窗口：2026-10-16 至 2026-10-19。週末期間可查核的新公告較少，因此以 10/16–10/18 官方更新為主，另納入近五日的 Google Research 與 AtScale 發布；模型效能數字均標示為發布方測試，不視為普遍結果。

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 1 | [DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | DeepSeek 官方 Hugging Face 模型卡在 10/17 更新 1017 版，稱推理、程式、代理與視覺基準均有進步，並採 MIT 授權；卡片列出 1M context，模型規模約 763B 參數。DeepSeek 報告的 DeepSWE v1.1 為 77.0，舊版為 74.2，但測試使用 Claude Code harness，分數不能直接代表實際專案表現。權重可下載，不代表一般工作站能負擔；先核對硬體、推論框架與授權，再用固定程式任務測成功率、記憶體和延遲。 |
| 2 | [GPT-6 Pro 多代理與工具更新](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) | OpenAI 於 10/16 更新 ChatGPT GPT-6 Pro：回覆更快、工具與外掛使用改善，並開始讓多個代理平行處理任務，使用者可查看進度與已完成子任務。此更新逐步提供給符合資格的 Pro 用戶，受工作區設定影響；公告未提供對照測試或適用任務範圍。可用同一組多步工作比較完成時間、錯誤率、代理分工透明度及用量。 |
| 3 | [Junie Local 擴大硬體支援](https://junie.jetbrains.com/blog/) | JetBrains 於 10/16 表示 Junie Local 可在 NVIDIA RTX Spark 執行，Windows 支援也轉為穩定版；產品定位是模型與程式碼在本機處理，不按 token 計費。它降低了本機代理的設定門檻，但硬體相容清單與實際速度仍需依設備確認，且離線本機模型未必適合所有高難度任務。可用自己的程式庫測試安裝、編譯、測試和長任務，並確認網路活動只限模型下載。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 4 | [ChatGPT Slides](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) | ChatGPT 於 10/16 開始推出簡報協作：可從對話、檔案或大綱建立簡報，在 Space 中共同編輯、留言，並匯出 PowerPoint、PDF 或 Google Slides。現正向具 Space 權限的 Pro、Business、Enterprise 用戶分批推出，且 web 與桌面版支援不同；不代表所有帳戶已可用。先用既有範本測試版面一致性、圖表資料核對、多人修改紀錄與匯出後的可編輯性。 |
| 5 | [Google Research Harness²](https://github.com/google-research/harness2) | Google Research 公開 Harness²，讓代理在模型權重不變的情況下，依任務執行「提出、探測、組合」來調整提示、工具、記憶與子代理等 harness 元件；支援 Codex、OpenCode，並提供 JobBench、LAB、WorkBuddy-Bench 等評測流程。專案標明不屬 Google 官方支援產品，且公布的最高增益來自少數模型與基準組合。可先跑單一任務與基線比較，確認耗用額度、基準資料存取限制及重現性，再評估遞迴改良是否值得成本。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 6 | [AtScale for AI](https://www.atscale.com/press/atscale-for-ai/) | AtScale 於 10/15 推出由 Ava、CoModel、Canary 組成的企業 AI 套件，主張以共用指標定義、語意層與測試流程，讓代理查詢遵循既有商業邏輯。這是供應商的新產品組合與定位，公告未提供獨立準確率驗證；價值取決於企業是否已治理指標與資料模型。若評估，選一個財務或營運指標，檢查定義、權限、SQL 結果與版本變更是否可追溯。 |
| 7 | [Google Earth AI 地理空間代理](https://research.google/blog/putting-earth-ai-to-work-geospatial-agents-for-our-planets-biggest-challenges/) | Google Research 於 10/14 表示，正透過 Ask Google Earth 與 Agent-to-Agent 服務擴大地理空間代理的實驗性使用；技術報告描述代理如何串接地球觀測模型、空間工具與規劃，處理跨資料類型的分析。這仍是實驗性存取，不等於一般使用者已全面開放，且示範與合作測試不能取代實地驗證。可確認申請資格、資料覆蓋範圍、空間推論誤差和結果來源，再用已知地區做交叉比對。 |

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| 代理的產出開始同時受模型、工具和工作流程影響 | [DeepSeek-V4.1-Flash-1017](#item-01)、[GPT-6 Pro 多代理與工具更新](#item-02)、[Google Research Harness²](#item-05) | DeepSeek 更新模型能力、GPT-6 Pro 把工作拆給平行代理、Harness² 則改造代理周邊配置；三者分別作用在代理效能的模型、協作和執行框架。 | 用同一組任務記錄完成率、總延遲、token／硬體成本與人工返工，避免只比較單一基準分數。 |
| 本機執行與受治理的企業資料各自建立信任條件 | [Junie Local 擴大硬體支援](#item-03)、[AtScale for AI](#item-06) | Junie 把程式碼留在本機，AtScale 則把企業指標定義帶進代理查詢；一方控制資料外流，一方控制答案採用的商業語意。 | 檢查本機代理的網路行為、組織權限、指標定義版本與查詢結果是否能稽核。 |
| AI 從文字與程式任務延伸到多人協作和地理分析 | [ChatGPT Slides](#item-04)、[Google Earth AI 地理空間代理](#item-07) | Slides 把 AI 產物帶入多人編輯與簡報交付，Earth AI 則以模型和空間工具回答地理問題；兩者都需要讓使用者看懂並驗證生成內容。 | 以真實簡報與已知地區資料測試內容正確性、來源標示、修改紀錄和匯出結果。 |

## 來源

- [DeepSeek 官方 Hugging Face：DeepSeek-V4.1-Flash-1017 模型卡與技術報告](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
- [OpenAI Help Center：ChatGPT release notes（2026-10-16）](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [JetBrains Junie Blog：Junie Local Comes to the NVIDIA RTX Spark（2026-10-16）](https://junie.jetbrains.com/blog/)
- [Google Research：Harness² 官方 GitHub 專案與文件](https://github.com/google-research/harness2)
- [Google Research：Putting Earth AI to work（2026-10-14）](https://research.google/blog/putting-earth-ai-to-work-geospatial-agents-for-our-planets-biggest-challenges/)
- [AtScale：AtScale for AI 發布公告（2026-10-15）](https://www.atscale.com/press/atscale-for-ai/)
