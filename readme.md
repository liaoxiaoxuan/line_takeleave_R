# Line Take Leave Bot   

這個專案是透過 Line Bot 和 Line Notify，自動回覆家長請假的訊息，並將訊息轉傳至私人帳號或群組。  
此專案的動機在於自動化處理班級學生請假訊息，方便導師掌握學生出缺情況。  

## 專案簡介 

我本身是一位高職導師，每天需要掌握班上學生的出缺狀況。  
透過 LINE 為孩子請假，已是現今趨勢，而我所回覆的內容通常大同小異，不外乎讓家長知道導師已收到訊息、告知家長請假手。    
因此，開發了一個自動化系統來回覆這些請假訊息。  
此外，為了掌握班上學生的出缺狀況，系統會將家長的請假訊息轉傳至我的私人帳號或群組。

## 功能 

1. 自動回覆家長幫孩子請假的 Line 訊息。 
2. 根據不同的請假類型提供相應的回覆內容。   
3. 將家長的請假訊息轉傳至私人帳號或群組。   

## 安裝說明 
1. 複製此專案到本地端   

    ```sh
    git clone https://github.com/liaoxiaoxuan/line_takeleave_pub.git
    ```

2. 進入專案目錄 

    ```sh
    cd line_takeleave_pub
    ```

3. 安裝所需套件   

    ```sh
    pip install -r requirements.txt
    ```

4. 配置設定檔案  
設置配置文件`config.json`，包含 LINE Bot 的 Channel Access Token、Channel Secret 和 Line Notify Token：
    ```json
    {
    "channel_access_token": "YOUR_CHANNEL_ACCESS_TOKEN",
    "channel_secret": "YOUR_CHANNEL_SECRET",
    "line_notify_token": "YOUR_LINE_NOTIFY_TOKEN"
    }
    ```

## 使用方法 

### 1. 啟動 Flask 應用    

```sh
python app.py
```

### 2. 設置 Webhook URL 

2-1. 登錄 LINE Developers   
2-2. 將 Webhook URL 設置為 `https://your-domain/callback`    

## 程式說明    

### 程式架構    
這個專案使用 Flask 框架來建立 Web 應用，並與 LINE Bot SDK 和 LINE Notify 進行互動。主要分為以下幾個模組：   

1. Flask 應用（app.py） 

- 主要負責接收來自 LINE 平台的 Webhook 請求，並根據收到的事件進行處理。  
- 包含了 `callback()` 函數來處理 `/callback` 的 POST 請求，並使用 `WebhookHandler` 驗證簽名及處理請求。    

2. LINE Bot SDK（linebot.v3）  

- 提供了 `WebhookHandler` 來處理 LINE 平台發送的事件，例如消息事件。   
- 使用 `MessagingApi` 來與 LINE Messaging API 進行互動，例如發送回覆消息。 

3. LINE Notify 

- 使用 `requests` 模組發送 HTTP POST 請求到 LINE Notify API，將收到的訊息轉發至指定的 LINE 帳號或群組。   

4. 設定檔案（config.json）  

- 包含了 channel_access_token、channel_secret 和 line_notify_token 的配置資訊，用於授權 LINE Bot 和 LINE Notify 的使用權限。    

### 主要函數   
- `callback()`：處理來自 `/callback` 的 POST 請求，驗證簽名並使用 WebhookHandler 處理請求。 
- `handle_message(event)`：處理 LINE 發送的訊息事件，根據訊息內容回覆相應的文字。   
- `replyMessage(user_message_lower)`：根據家長的請假訊息，自動回覆對應的內容。  
- `line_notify_image(message)`：透過 LINE Notify 將訊息轉傳至私人帳號或群組。   

### 主要模組    
- `Flask`：用於建立 Web 應用。    
- `linebot`：用於處理 LINE Bot 和 LINE Notify 的互動。    
- `requests`：用於發送 HTTP 請求。    

## 常見問題 

1. 如何設定 LINE Bot 的 Webhook URL？   
登入 LINE Developers，將 Webhook URL 設置為 https://your-domain/callback 。 

2. 如何取得 LINE Bot 的 Channel Access Token 和 Channel Secret？    
在 LINE Developers 開發者控制台創建 Messaging API，即可取得 Channel Access Token 和 Channel Secret。    

3. 如何取得 LINE Notify 的 Token？  
登入 LINE Notify，獲取權杖（Token）即可使用 LINE Notify API。   

## 其他參考資源 

### 1. Line message API 聊天機器人 
    
- 使用flask來串接line message API 聊天機器人   
https://www.youtube.com/watch?v=TSLFkwvj8xA 
- flask_lineAPI    
https://github.com/wilsonsujames/flask_lineAPI/blob/master/line_api/app.py  

### 2. Line Bot 串接 Line Notify 轉傳訊息    

- Line-Bot 串接 Line-Notify 實現跨群組轉播訊息  
https://medium.com/@m23568n/line-bot%E4%B8%B2%E6%8E%A5line-notify%E5%AF%A6%E7%8F%BE%E8%B7%A8%E7%BE%A4%E7%B5%84%E8%BD%89%E6%92%AD%E8%A8%8A%E6%81%AF-c0acfed7d9f6 
- 【GAS】用Line Bot&Line Notify轉發群組訊息給自己   
https://emtech.cc/post/line2notify/ 

## 貢獻與成果  

1. 自動化回覆家長請假訊息   
專案旨在自動化處理家長透過 Line 發送的請假訊息，大幅簡化了導師和家長之間的溝通流程。使用者可以即時收到請假訊息通知，並迅速作出回應，提升了導師管理請假狀況的效率。  

2. 效能提升和操作便利性    
通過整合 LINE Bot SDK 和 LINE Notify，成功實現了即時通知和訊息轉發功能，使得家長和導師能夠快速溝通，確保學生請假事務的及時處理。這不僅提高了操作的便利性，也降低了人工處理請假訊息所需的時間和成本。    

3. 技術技能展示    
展示了使用 Flask 框架、LINE Bot SDK 和 LINE Notify API 開發系統的能力，並透過 Python 實現了對 LINE 平台的有效整合和應用。這些技術不僅僅是技術能力的展示，更是在提升學校管理和溝通方面的實際應用。   

## 未來展望 
未來，計劃進一步提升自動回覆的演算法，例如導入 Google AI Gemini、ChatGPT API 等模型，增強對不同請假情境的辨識和處理能力。同時，也將考慮導入更多的機器學習技術，以進一步提升系統的自動化和智慧化水準。   
