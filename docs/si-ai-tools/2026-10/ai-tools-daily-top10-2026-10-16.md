# SI 的 AI 工具選報

更新日期：2026-10-16（Asia/Taipei）

觀察窗口：2026-10-15 至 2026-10-16。檢查最近七期日報後，以 10/15 新公告和正式推出為主；廠商自測數字均註明來源或比較條件。

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 1 | [NVIDIA Nemotron 3.5 Super VL 與 Bolt](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/) | NVIDIA 於 10/15 開放多模態代理模型 Super VL（120B 總參數、12B 啟用參數），同時推出可在 24GB 記憶體運行的 Bolt 74B-A9B；Super VL 和 Bolt 權重已可下載，較小的 Bolt E4B 預計 10/23 才推出。它把視覺、影片理解與代理工作帶到自架和邊緣部署，但「同級最快」等表現是 NVIDIA 的比較。先依模型卡確認授權、硬體與量化版本，再以實際圖像、影片和工具任務測速度、準確率及記憶體用量。 |
| 2 | [GPT-Live-1.1 與 ChatGPT 新語音](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) | OpenAI 於 10/15 開始在 ChatGPT Voice 推出 GPT-Live-1.1 與較小的 Quip，增加法、德、印、日、韓、墨西哥西語等語音，以及英文 Bubbie；Plus 以上以 Live 為預設，其他用戶使用 Quip，實際可選聲音會依地區和帳戶而異。系統卡表示針對性合成安全測試中，部分敏感類別較前代有統計上顯著退步；該測試不是實際使用比例。可用多語言、插話與敏感內容樣本檢查辨識、延遲和安全回應。 |
| 3 | [GitHub Code Security：AI Scan 與 Agentic Autofix](https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available/) | GitHub 於 10/15 將 PR 漏洞 AI Scan 和程式碼警示的 Agentic Autofix 都升為正式版。AI Scan 補查 CodeQL 尚未涵蓋的語言與框架，結果僅供參考、不會阻擋合併；Autofix 可跨檔案提出修正、重跑 CodeQL，再開草稿 PR 供人審查。私有 repo 需相應安全方案，兩者會使用 Code Security AI 額度；Autofix 也會耗用 GitHub Actions 分鐘。可先在測試專案比對 AI Scan 誤報及修補後測試結果，並設好額度預算。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 4 | [Figma Specs、Code Layers 與 MCP 工作流](https://www.figma.com/blog/build-by-design/) | Figma 於 10/15 開放 Code Layers 公測，讓團隊把本機、GitHub 或 MCP 帶入的程式原型放到設計畫布協作；Specs 也開始向付費方案推出公測，作為可連結設計、程式與文件的專案脈絡。Figma MCP 新增從 AI 工具建立 code layer、操作 Specs 等能力。不同功能的方案與推出進度有別，程式碼層也尚未涵蓋複雜程式庫；適合先驗證設計和實作往返時，狀態、版本與審核紀錄是否保留。 |
| 5 | [Arcade Tool Recommendation](https://www.arcade.dev/blog/tool-recommendation/) | Arcade 於 10/15 推出 MCP 工具目錄檢索，代理可先依任務挑出相關工具，減少每輪都把大量工具定義放進上下文。Arcade 的測試稱 10 輪對話的工具定義輸入 token 最多減少 91%；其 408 次 Codex 與 Claude Code 測試中，總帳單平均下降 7.6%，但 95% 區間為 2.5% 至 12.6%，且節省幅度受工具數、結果是否留在上下文及模型影響。可先用自己的 MCP 目錄比較選取召回率、漏掉工具的比例與總任務成本。 |
| 6 | [Formaloo OI／Formaloo 5.0](https://www.formaloo.com/blog/formaloo-5-formaloo-oi-launch) | Formaloo 於 10/15 宣布推出以 Intake Agent、決策模型和工作流程代理處理表單、審核、入職等營運流程，並可連接既有 CRM、ERP 等系統；新版本正分批推出，完整方案預計數週內到齊。公告稱重要決定仍由人員把關，這屬於供應商的產品定位。若評估導入，先用低風險流程確認代理的判斷依據、例外升級、資料回寫和人工核准點。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---:|---|---|
| 7 | [GitHub Copilot 模型退場時程](https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november/) | GitHub 宣布 11/16 起在 Copilot 各介面退場 Claude Opus 4.8、Claude Opus 5 與 GPT-5.6 Terra，建議改用 Opus 5.5、GPT-6.1 Sol 或 GPT-6 Luna；年繳個人方案的 Opus 4.8 使用者例外。管理員應先確認替代模型政策，再以現有代理提示與工具流程做回歸測試。 |
| 8 | [Claude Haiku 4.5 在一般方案的退場安排](https://support.claude.com/en/articles/17444146-claude-haiku-4-5-is-leaving-the-model-selector) | Anthropic 於 10/15 通知，Haiku 4.5 將於 10/29 從 Free、Pro、Max 的聊天、Cowork 和 Design 模型選單移除並改由 Haiku 5.5 接替；Claude Code、Team／Enterprise 與 API 不受這次變更影響，既有對話也會保留。若依賴一般方案的 Haiku 4.5，應在期限前比較新模型的回覆和工作流程相容性。 |

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| 代理修改程式要把偵測、驗證與審查接起來 | [GitHub Code Security：AI Scan 與 Agentic Autofix](#item-03)、[Formaloo OI／Formaloo 5.0](#item-06) | GitHub 先找出 PR 風險，再讓代理提出可驗證的修補；Formaloo 則把營運資料轉成工作流與決策，兩者都需要明確的人員核准與例外處理。 | 測試錯誤建議、無法自動修復和高風險案例，確認人工能在動作生效前攔截。 |
| 大量工具的代理流程更重視脈絡整理 | [Arcade Tool Recommendation](#item-05)、[Figma Specs、Code Layers 與 MCP 工作流](#item-04) | Arcade 依任務挑出少數可用工具，Figma 則讓設計、規格和程式原型透過 MCP 交給代理；兩者都在處理代理拿到哪些上下文、如何使用。 | 以相同任務量測工具召回、上下文 token、設計還原度與來回修改時間。 |
| 模型升級同時帶來部署與遷移選擇 | [NVIDIA Nemotron 3.5 Super VL 與 Bolt](#item-01)、[GPT-Live-1.1 與 ChatGPT 新語音](#item-02)、[GitHub Copilot 模型退場時程](#item-07)、[Claude Haiku 4.5 退場安排](#item-08) | NVIDIA 推進可自行部署的視覺代理，語音產品改用新模型，而 Copilot 與 Claude 也為舊模型列出退場日期；選型需一併考慮硬體、服務入口與版本相容。 | 記錄模型授權、可用方案、替代模型的品質差異與切換期限。 |

## 來源

- [NVIDIA：Nemotron 3.5 Super VL 與 Bolt（2026-10-15）](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)
- [Hugging Face：Nemotron 3.5 Super VL 官方模型卡](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16)
- [OpenAI Help Center：ChatGPT release notes（2026-10-15）](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [OpenAI Deployment Safety Hub：GPT-Live-1.1 system card](https://deploymentsafety.openai.com/gpt-live-1-1/avoiding-deceptive-interactions-with-users)
- [GitHub Changelog：AI Scan for pull requests GA（2026-10-15）](https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available/)
- [GitHub Changelog：Agentic autofix GA（2026-10-15）](https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/)
- [Figma：Build by design（2026-10-15）](https://www.figma.com/blog/build-by-design/)
- [Arcade：Tool Recommendation（2026-10-15）](https://www.arcade.dev/blog/tool-recommendation/)
- [Arcade Docs：Tool Recommendation 設定與限制](https://docs.arcade.dev/en/operate/governance/mcp-gateways/tool-recommendation)
- [Formaloo：Formaloo OI is live（2026-10-15）](https://www.formaloo.com/blog/formaloo-5-formaloo-oi-launch)
- [GitHub Changelog：Copilot 模型將於 11 月退場（2026-10-15）](https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november/)
- [Anthropic Help Center：Claude Haiku 4.5 退場安排（2026-10-15）](https://support.claude.com/en/articles/17444146-claude-haiku-4-5-is-leaving-the-model-selector)
