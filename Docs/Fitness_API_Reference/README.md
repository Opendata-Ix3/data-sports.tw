# Summary

- [ Fitness 體適能加值模組 API 開發指南 ](README.md)
  - [ (認證授權) 取得存取令牌(Token) ](AUTHORIZATION.md)
  - [ (體適能) 查詢全部常模類型 ](FITNESS_NORM_TYPE.md)
  - [ (體適能) 查詢特定常模資料 ](FITNESS_NORM_DATA.md)


## 測試前提醒

- 若要測試上列各服務，請將各項說明內的網址中 {domain} 代換成**目前的測試環境domain**。
- 並且把header的Authorization的 {YOUR_ACCESS_TOKEN} 換成自己的token，注意 Bearer 與 token 之間要記得保留一格空白哦~~

例如：

```shell=
https://{domain}/fitness/norm/type[?version={version}]
```

`Authorization: Bearer {YOUR_ACCESS_TOKEN}`


換成

```shell=
https://qa-api.sportservice.tw/fitness/norm/type
```

`Authorization: Bearer abc123456789xyz`

&nbsp;
- 目前的測試環境domain：qa-api.sportservice.tw
- 若需要正式domain，請另外與本團隊聯絡，非常感謝。


<!--   - [ (人工智慧) 與 AI 機器人聊天(可詢問體適能常模，或使用加值模組常模資料庫評估個人運動表現) ](AI_NLG_CHAT_FITNESS.md)   -->
<!--   - [ (人工智慧) 查詢問答資料庫 ](AI_NLU_QNA.md)   -->
<!--   - [ (人工智慧) 提取關鍵字內容 ](AI_NLU_TEXT_ANALYSIS.md)   -->
<!--   - [ (人工智慧) 與 AI 機器人聊天(不限體適能常模與運動表現評估話題) ](AI_NLG_CHAT.md)   -->

<!-- - [ 附錄 ]   -->
<!--   - [ 人工智慧相關 API 功能特性比較說明表 ](AI_NLG_NLU_DESC.md)   -->
