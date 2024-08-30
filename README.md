# 運動數據公益平臺 data-sports.tw 開發者專區
## 什麼是 API Token
### 作為身份的替代
- 在取用數據時，只要在第一次以帳號/密碼取得令牌（Token）後，在Token到期失效前，都可以用它來取用平臺上的數據
- 當Token到期時，要重新輸入帳號／密碼，再取得新的Token，就可以用新的Token進行取用

### 如何在Swagger上測試Token
- 先至平臺註冊成為「運用者」
  ![swagger_register](https://github.com/user-attachments/assets/8d93e8fa-867b-490b-9e0f-a84a68d63ca2)
- 再到Swagger介面執行『Common 通用』中的「/member/login」取得Token
  ![swagger_login-1](https://github.com/user-attachments/assets/9b35bf88-be48-457e-9237-c12c01fb40b1)
- 到Swagger介面的『Authorize』把 "Bearer" + " " + Token 一起填入欄位，即可取得使用權利
  ![swagger_login-2](https://github.com/user-attachments/assets/c7f02595-8887-4509-aa52-d59a81324833)
- 在該Token失效前，可以持續在Swagger的「Consumer 數據運用者」使用「/data/processed」取得 [指定類型]、[指定資料筆數]的最新數據
  ![swagger_get-data](https://github.com/user-attachments/assets/862377b1-44f5-4a8f-954c-7f2de1ccc78c)
  
## 以程式取得 API Token 的範例
### 執行說明
- 預設在CoLab上執行
    > **所以還沒有提供venv與requirements.txt等設定說明**
- 輸出
    - 查詢結果
    - 本月剩餘的查詢次數
    - Token字串
#### 需自行填入的參數
1. 自己的帳號、密號(例如下面...)
```
MY_MEMBER_NAME = "little test"    # 帳號
MY_PASSWORD = "big result"    # 密碼
```

2. 想要查詢的數據類別(例如下面...)
```
main_type = "PhysicalFitness"    # 體適能: PhysicalFitness
type = "ResistanceTraining"    # 阻力訓練: ResistanceTraining
subtype = ""    # 可能沒有「子類型」
data_size = 100    # 每次查詢可以有 [100筆 | 1000筆 | 10000筆] 三種範圍
```

