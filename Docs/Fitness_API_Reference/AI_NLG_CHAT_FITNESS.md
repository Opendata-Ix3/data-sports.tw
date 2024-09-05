---
title: Fitness Service RESTful API reference (AI NLG CHAT FITNESS)

---

# Fitness Service RESTful API reference (AI NLG CHAT FITNESS)

## 目錄
1. [概述](#概述)
2. [授權與認證](#授權與認證)
3. [API端點](#API)
4. [請求格式](#請求格式)
5. [回應格式](#回應格式)
6. [錯誤處理](#錯誤處理)
7. [使用範例](#使用範例)

## 概述
本指引提供如何與體適能 API 介接說明。透過此文字生成式 API，開發者可以快速串接聊天機器人，讓使用者使用自然語言與聊天機器人對話(詢問有關體適能常模問題，或是使用加值模組常模資料庫評估個人運動表現)。在此之前，開發者請先參考 Authorization 章節之說明完成授權與認證。

## 授權與認證
使用加值模組 API 之前，需要先取得授權 Token。所有 API 請求必須包含以下標頭：

- `Authorization: Bearer {YOUR_ACCESS_TOKEN}`

### API
向下述 API 端點發送請求以取得回應：
- URL: `<https://{domain}/ai/nlg/chat_fitness>`
- 方法: `GET`
- 標頭: `Authorization: Bearer {YOUR_ACCESS_TOKEN}`

### 請求格式
- 請求格式與參數:
```shell=
https://{domain}/ai/nlg/chat_fitness?prompt={prompt}[&user_id={user_id}&version={version}]
```

| 名稱 | 類型 | 說明 | 備註 | 必要欄位 | 
| -------- | -------- | -------- | -------- | -------- |
| prompt | string | 使用者聊天訊息 |  | 是 |
| user_id | string | 使用者帳號 |  | 否 |
| version | string | API 版號(yyyy-MM-dd) | 無版號則使用預設版本 | 否 |

### 回應格式
- 回應格式與內容:
  ```json
  {
    "code": 200,
    "message": "操作成功 (Operation Successfully)",
    "timestamp": 1725519375744,
    "prompt": "我是21歲男生，仰臥起坐60秒可以做47下，表現如何?",
    "answer": "根據您提供的數據，我可以提供一個參考，根據20-24歲男性的仰臥起坐60秒數據：\n\n- 0-20%: 0-31次\n- 20-40%: 32-36次\n- 40-60%: 37-40次\n- 60-80%: 41-46次\n- 80-100%: 47次以上\n\n您提到可以做47次，這將把您置於80-100%的等級範圍內，顯示您的表現非常優秀。"
  }

### 錯誤處理
| 錯誤代碼 | 說明 | 可能原因 | 建議解決方案 |
| -------- | -------- | -------- | -------- |
| 400 | 缺少參數 | 請求缺少必要參數 | 檢查參數是否完整 |
| 401 | 未經授權 | 認證失敗 | 檢查帳號和密碼是否正確 |
| 404 | 資源不存在 | 無法找到請求資源 | 檢查URL是否有拼寫錯誤 |

### 使用範例
- 使用 Curl 介接 API 的指令如下:
```shell=
curl -X GET "https://{domain}/ai/nlg/chat_fitness?prompt={prompt}&version=2024-08-15"
-H "accept: application/json" -H "Authorization: Bearer {YOUR_ACCESS_TOKEN}"
```