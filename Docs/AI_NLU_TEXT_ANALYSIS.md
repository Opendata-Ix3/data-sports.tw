---
title: Fitness Service RESTful API reference (AI NLU TEXT ANALYSIS)

---

# Fitness Service RESTful API reference (AI NLU TEXT ANALYSIS)

## 目錄
1. [概述](#概述)
2. [授權與認證](#授權與認證)
3. [API端點](#API)
4. [請求格式](#請求格式)
5. [回應格式](#回應格式)
6. [錯誤處理](#錯誤處理)
7. [使用範例](#使用範例)

## 概述
本指引提供如何與體適能 API 介接說明。透過此NLU 分析文字 API，開發者可以提取使用者輸入文字中的基本資料，包含年齡、性別、身高和體重等資料。在此之前，開發者請先參考 Authorization 章節之說明完成授權與認證。

## 授權與認證
使用加值模組 API 之前，需要先取得授權 Token。所有 API 請求必須包含以下標頭：

- `Authorization: Bearer {YOUR_ACCESS_TOKEN}`

### API
向下述 API 端點發送 POST 請求以獲取 Token：
- URL: `<https://{domain}/ai/nlu/text_analysis`>
- 方法: `GET`
- 標頭: `Authorization: Bearer {YOUR_ACCESS_TOKEN}`

### 請求格式
- 請求格式與參數:
```shell=https://{domain}/ai/nlu/text_analysis?text={text}[&user_id={user_id}]
```

| 名稱 | 說明 | 備註 | 必要欄位 | 
| -------- | -------- | -------- | -------- |
| text | 文字內容 | API 根據內容提取基本資料 | 是 |
| user_id | 使用者帳號 |  | 否 |

### 回應格式
- 回應格式與內容:
  ```json
  {
    "code": 200,
    "message": "操作成功 (Operation Successfully)",
    "timestamp": 1724988181132,
    "text": "我是21歲的男生，身高172，體重66",
    "analysis": {
      "user_id": "user123",
      "age": "21歲",
      "gender": "男生",
      "height": "172.0",
      "weight": "66.0"
    }
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
curl "https://{domain}/ai/nlu/text_analysis?text={text}"
-H "accept: application/json" -H "Authorization: Bearer {YOUR_ACCESS_TOKEN}"
```