# SI 的 AI 工具選報

更新日期：2026-11-19（Asia/Taipei）

觀察窗口：以 11/18 官方更新為主，另納入 11/17 發布且本期首次整理的 GPT-6.2。部分功能採預覽或分批開放；模型效能比較以供應商評測為準。

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 1 | [Project Genie 加入 Genie 4：即時編輯互動世界](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/) | Google 於 11/18 將 Genie 4 推出於 Project Genie，符合資格的 Google AI Ultra 訂戶可建立、分享和改編互動世界；探索途中能用文字改變場景，並加入隨情境變化的原生音訊。更新也加入協助建構世界的 Project Genie agent 與社群作品庫。這仍是實驗性產品，開放範圍限符合資格的 Ultra 訂戶，AI Pro 用戶目前可加入候補名單。創作者可先用簡短指令測試場景修改是否穩定、音訊是否貼合情境，以及作品分享範圍。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 2 | [GPT-6.2 Astra 與 Sol：進入 GitHub Copilot、Work 和 Codex](https://openai.com/index/introducing-gpt-6-2-astra-sol/) | OpenAI 於 11/17 發布 GPT-6.2 Astra 與 Sol：Astra 面向複雜專業任務，Sol 面向日常工作；兩者在 ChatGPT Work 和 Codex 以預覽提供。GitHub 同日將兩款模型一般提供給 Copilot Pro+、Max、Business 與 Enterprise，主打代理程式開發與程式碼審查，使用量按供應商牌價計費。OpenAI 公布的效能數據來自其指定基準與設定，Copilot 的早期審查結果也非獨立測試。導入前應核對方案、管理員模型政策及費用，再用自有 issue 比較缺陷檢出率、誤報和修正成本。 |
| 3 | [Gemini 4 Neon 一般提供於 GitHub Copilot](https://github.blog/changelog/2026-11-18-gemini-4-neon-in-github-copilot/) | GitHub 於 11/18 將 Gemini 4 Neon 一般提供給 Copilot Pro+、Max、Business 和 Enterprise 使用者，可在多種 Copilot 介面選用，並正分批開放。Google 將 Neon 定位為低成本代理程式開發模型，並稱相較 Gemini 4 Carbon 回應較快、較少未要求的程式修改；這些比較屬供應商評測。用既有工作流程測試時，應同時檢查修改範圍、測試結果、延遲與按用量計費金額。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 4 | [GitHub Copilot 新增八種服務連接器](https://github.blog/changelog/2026-11-18-connect-supabase-box-calendly-and-more-to-copilot/) | GitHub 於 11/18 在公開預覽中新增 Box、Buildkite、Calendly、ClickUp、Mixpanel、Supabase、Webflow 和 Wix 連接器，使用 GitHub 驗證的 MCP 伺服器，可在 Copilot 多種介面跨工作階段連接。Business 與 Enterprise 管理員須開啟預覽政策；若 MCP 允許清單逐項列出服務，也要新增相應項目，部分服務另需在服務端授權。試用前先限定資料與操作權限，再驗證搜尋、寫入和代理操作的授權邊界。 |
| 5 | [GitHub Copilot 團隊外掛設定一般提供](https://github.blog/changelog/2026-11-18-customize-github-copilot-for-your-team/) | GitHub 於 11/18 將團隊層級的 Copilot 自訂設定轉為一般提供；Business 與 Enterprise 的團隊維護者或組織擁有者可指定核准的 Agent Plugins 作為團隊預設。設定只套用於直接成員，不會由父團隊自動傳給子團隊；組織與企業政策仍優先，成員在政策允許時可關閉外掛。管理員可先盤點 marketplace 來源和外掛權限，再以一個試點團隊核對預設是否符合實際工作需要。 |
| 6 | [ChatGPT Live Dictation：即時顯示語音轉錄](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) | OpenAI 於 11/18 更新 ChatGPT 聽寫：說話時即可看到轉成的文字，能切換顯示逐字稿，並取消原本 10 分鐘錄音上限。官方稱正向所有方案、iOS、Android、網頁和桌面版全球推出；實際介面可能因分批 rollout 尚未出現。可用中英夾雜、專有名詞和背景雜音測試修正需求，再決定是否適合用於會議或長段口述。 |

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| 代理工作開始同時考慮模型、工具與團隊規則 | [GPT-6.2 in Copilot](#item-02) · [Gemini 4 Neon in Copilot](#item-03) · [Copilot 連接器](#item-04) · [Copilot 團隊外掛](#item-05) | Copilot 一邊增加可選模型，一邊讓團隊接入外部服務並共享核准外掛；代理能做什麼，逐漸由模型能力、資料連接和管理政策共同決定。 | 以試點團隊檢查模型權限、外掛來源、MCP 允許清單及可寫入範圍；再比較任務品質、人工覆核和實際用量費用。 |
| AI 介面朝即時互動與可調整輸出發展 | [Project Genie／Genie 4](#item-01) · [ChatGPT Live Dictation](#item-06) | Genie 4 讓使用者在世界生成後繼續用指令改變場景，Live Dictation 則讓口述文字在輸入途中可見；兩者都把等待生成完成後再修正的流程往即時互動推進。 | 測試連續指令能否維持場景或語意一致，並記錄語音轉錄錯誤、修正時間及生成延遲。 |

## 來源

- [Google DeepMind：Genie 4 is now available（2026-11-18）](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/)
- [OpenAI：Introducing GPT-6.2 Astra and Sol（2026-11-17）](https://openai.com/index/introducing-gpt-6-2-astra-sol/)
- [GitHub Changelog：OpenAI’s GPT-6.2 Astra and GPT-6.2 Sol now available（2026-11-17）](https://github.blog/changelog/2026-11-17-openais-gpt-6-2-astra-and-gpt-6-2-sol-now-available/)
- [GitHub Changelog：Gemini 4 Neon in GitHub Copilot（2026-11-18）](https://github.blog/changelog/2026-11-18-gemini-4-neon-in-github-copilot/)
- [GitHub Changelog：Connect Supabase, Box, Calendly, and more to Copilot（2026-11-18）](https://github.blog/changelog/2026-11-18-connect-supabase-box-calendly-and-more-to-copilot/)
- [GitHub Changelog：Customize GitHub Copilot for your team（2026-11-18）](https://github.blog/changelog/2026-11-18-customize-github-copilot-for-your-team/)
- [OpenAI Help Center：ChatGPT release notes（2026-11-18）](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
