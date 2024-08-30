---
title: Fitness Service RESTful API reference (Authorization)

---

# Fitness Service RESTful API reference (Authorization)

## 目錄
1. [概述](#概述)
2. [授權與認證](#授權與認證)
3. [API端點](#API)
4. [請求格式](#請求格式)
5. [回應格式](#回應格式)
6. [錯誤處理](#錯誤處理)
7. [使用範例](#使用範例)

## 概述
本指引提供如何與體適能 API 介接說明。透過此授權與認證 API，開發者可以使用 Token 訪問加值模組服務，執行查詢數據或其他服務之操作。在此之前，開發者請先至`運動數據公益平台`申請專屬帳號。

## 授權與認證
使用加值模組 API 之前，需要先取得授權 Token。所有 API 請求必須包含以下標頭：

- `Authorization: Bearer {YOUR_ACCESS_TOKEN}`

### API
向下述 API 端點發送 POST 請求以獲取 Token：
- URL: `<https://api.data-sports.tw/member/login`>
- 方法: `POST`
- 標頭: `Content-Type: application/json`

### 請求格式
- 請求格式與參數:
  ```json
  {
    "membername": "YOUR_MEMBER_NAME_HERE",
    "password": "YOUR_MEMBER_PASSWORD_HERE"
  }

### 回應格式
- 回應格式與內容:
  ```json
  {
    "datetime": "2024-08-15T01:18:32.858676",
    "data": {
      "need_update_password": false,
      "status": "DB Login",
      "is_check_terms_of_use": "Checked",
      "token": "YOUR_ACCESS_TOKEN_HERE",
      "is_first_login": true
    },
    "message": "success"
  }

### 錯誤處理
| 錯誤代碼 | 說明 | 可能原因 | 建議解決方案 |
| -------- | -------- | -------- | -------- |
| 401 | 未經授權 | 認證失敗 | 檢查帳號和密碼是否正確 |
| 404 | 資源不存在 | 無法找到請求資源 | 檢查URL是否有拼寫錯誤 |
| 422 | 缺少欄位 | 請求缺少必要欄位 | 檢查參數是否完整 | 

### 使用範例
- 使用 Curl 介接 API 的指令如下:
```shell=
curl -X POST "https://api.data-sports.tw/member/login"
-H "accept: application/json" -H "Content-Type: application/json" -d "{ \"membername\": \"YOUR_MEMBER_NAME_HERE\", \"password\": \"YOUR_MEMBER_PASSWORD_HERE\"}"

```

