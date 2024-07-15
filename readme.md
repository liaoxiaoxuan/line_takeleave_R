# Line Take Leave Bot   

這個專案是透過 Line Bot 和 Line Notify，自動回覆家長請假的訊息，並將訊息轉傳至私人帳號或群組。  
此專案的動機在於自動化處理班級學生請假訊息，方便導師掌握學生出缺情況。  

## 專案簡介 

我本身是一位高職導師，每天需要掌握班上學生的出缺狀況。  
透過 LINE 為孩子請假，已是現今趨勢，而我所回覆的內容通常大同小異，不外乎讓家長知道導師已收到訊息、告知家長請假手。    
因此，開發了一個自動化系統來回覆這些請假訊息。  
此外，為了掌握班上學生的出缺狀況，系統會將家長的請假訊息轉傳 至我的私人帳號或群組。

## 功能 

1. 自動回覆家長幫孩子請假的 Line 訊息。 
2. 根據不同的請假類型提供相應的回覆內容。   
3. 將家長的請假訊息轉傳至私人帳號或群組。   

## 安裝說明 
### 1. 複製此專案到本地端   

```sh
git clone https://github.com/liaoxiaoxuan/  line_takeleave_pub.git
```

### 2. 進入專案目錄 

```sh
cd line_takeleave_pub
```

### 3. 安裝所需的套件   

```sh
pip install -r requirements.txt
```

### 4. 配置設定檔案 

4-1. 打開 `..\local\config.json`  
4-2. 填入 LINE Channel Access Token 和 Channel Secret   

## 使用方法 

### 1. 啟動 Flask 應用    

```sh
python app.py
```

### 2. 設置 Webhook URL 

2-1. 登錄 LINE Developers   
2-2. 將 Webhook URL 設置為 `https://your-domain/callback`    
    
