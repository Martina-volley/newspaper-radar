# SI 的 AI 工具選報

更新日期：2026-11-09（Asia/Taipei）

觀察窗口：2026-11-06 至 2026-11-08。週末可核對的一手更新集中於 11/6，以下均按原發布日標示。

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 1 | [OpenAI BioBasicsBench：評估 AI 代理解讀實驗室原始資料](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) | OpenAI 於 11/6 發布 BioBasicsBench，以 100 項日常濕實驗室任務測試代理能否判讀凝膠、顯微影像、儀器輸出與實驗紀錄，也要辨認控制組錯誤及證據不足。官方報告在 xhigh 推理設定下，GPT‑6 Astra 平均得分 66.7%，GPT‑5.6 Sol 為 43.8%；這是 OpenAI 與生技公司 Ligo 建置並公布的評測，平均得分不等於任務成功率，也尚非獨立重現。研究團隊可先用自己的匿名化樣本測試影像判讀、控制組檢查和拒絕過度推論的能力，再決定是否適合輔助研究。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 2 | [Claude 專案標籤：按成本代碼檢視企業支出（Beta）](https://support.claude.com/en/articles/18251257-track-spend-by-cost-code-with-project-tags) | Anthropic 於 11/6 為符合資格的 Enterprise 組織推出專案標籤 Beta，可用成本中心、WBS 或客戶案件代碼標記專案，再從管理介面或 API 查看大部分專案支出。標籤只計入專案內的使用；標記生效約需兩小時，也不會回補生效前的支出，API、Claude for Office 等部分產品不在範圍內。HIPAA、CMEK、ZDR、最少資料保留及美國以外資料儲存的組織不符合資格。財務或管理團隊可先用低風險專案對帳，確認標籤覆蓋範圍、延遲與帳單金額的差異。 |
| 3 | [GitHub Copilot：VS Code 代理支援排程自動化與遠端預覽](https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2/) | GitHub 於 11/6 彙整本週 Copilot 更新：VS Code 本機自動化新增 cron 排程與工作區自訂代理；Agents 視窗也可預覽遠端應用並使用互動畫布，目前仍為預覽功能。排程讓代理能按時啟動工作，遠端預覽則可在本機編輯器檢查另一台機器上的結果；實際適用性取決於工作區設定、遠端瀏覽器支援和預覽版穩定度。可先用唯讀、可回復的例行任務驗證觸發時間、工具權限、失敗通知及中止方式，再讓代理修改檔案。 |
| 4 | [GitHub Copilot 成效儀表板新增 Chat 與 VS Code Agents 使用量](https://github.blog/changelog/2026-11-06-copilot-impact-dashboard-adds-chat-and-vs-code-agent-usage/) | GitHub 於 11/6 將 Copilot Chat 與 VS Code Agents 視窗納入企業及組織的 28 日使用報告與代理互動圖表。這補上原本看不到 Chat 的使用情況，但互動統計不會改變既有採用階段：Chat 和 VS Code Agents 不計入階段判定；使用者須在 28 日內至少兩天使用某功能才算該功能有互動，同一人可被多個功能分別計數。管理者可先確認使用度量政策、檢視權限與報表期間，再把互動數和代理任務完成品質分開解讀。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---|---|---|

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| AI 工作導入開始拆分衡量品質、採用與成本 | [BioBasicsBench](#item-01) · [Claude 專案成本標籤](#item-02) · [Copilot VS Code 自動化](#item-03) · [Copilot 使用儀表板](#item-04) | BioBasicsBench評估代理能否正確判讀工作證據，Copilot讓排程和互動情況可見，Claude則把專案支出歸因；三者分別衡量品質、使用與成本，不能用單一指標代替成效。 | 用自有任務檢查代理答案及失敗率；核對排程權限與中止流程；確認費用標籤覆蓋和報表定義後，再比較各項指標。 | 

## 來源

- [OpenAI：Measuring how AI agents handle everyday wet-lab science（2026-11-06）](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/)
- [Claude Help Center：Track spend by cost code with project tags](https://support.claude.com/en/articles/18251257-track-spend-by-cost-code-with-project-tags)
- [GitHub Changelog：GitHub Copilot weekly releases — November 2（2026-11-06）](https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2/)
- [GitHub Changelog：Copilot impact dashboard adds chat and VS Code agent usage（2026-11-06）](https://github.blog/changelog/2026-11-06-copilot-impact-dashboard-adds-chat-and-vs-code-agent-usage/)
