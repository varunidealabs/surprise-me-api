# Surprise Me API

Simple API to retrieve personal profile information using unique handles.

## 🚀 API Endpoint

**URL:** `https://web-production-4f250.up.railway.app/get-profile`

**Method:** POST

**Request:**
```json
{
  "handle": "25C1-XXX"
}
```

**Response:**
```json
{
  "message": "🎉 Hey [Name]! Here's your amazing profile:",
  "data": {
    "handle": "25C1-001",
    "name": "[Name]",
    "company": "💼 [Company]",
    "linkedin": "[LinkedIn URL]",
    "email": "[Email]"
  },
  "fun_fact": "You're part of an exclusive cohort of X amazing people!"
}
```

## 📱Guide to Make API Request

### Step 1: Install Postman
1. Go to [postman.com](https://www.postman.com/downloads/)

2. Download Postman for your computer (Windows/Mac/Linux)
3. Install and create a free account (or sign in if you have one)

### Step 2: Make Your First Request
1. **Open Postman** → Click "New" → Select "HTTP Request"
   
 <img width="469" height="441" alt="image" src="https://github.com/user-attachments/assets/167a2f27-3657-4f33-a3bc-f181bf9a4eba" />

2. **Set Method**: Change dropdown from "GET" to **"POST"**
3. **Enter URL**: Copy and paste:
   ```
   https://web-production-4f250.up.railway.app/get-profile
   ```
   
   <img width="1052" height="123" alt="image" src="https://github.com/user-attachments/assets/d7454031-14dd-410c-b5fa-54c403186792" />

4. **Add Headers**: Click "Headers" tab → Add:
   - Key: `Content-Type`
   - Value: `application/json`
     
     <img width="1039" height="213" alt="image" src="https://github.com/user-attachments/assets/413f1280-34d9-4d62-a498-e47cd58e8094" />

5. **Add Body**: Click "Body" tab → Select **"raw"** → Paste:
   ```json
   {
     "handle": "25C1-XXX"
   }
   ```
   
   <img width="1038" height="334" alt="image" src="https://github.com/user-attachments/assets/898cd091-5da4-46d2-aaa1-797db32a7474" />

   Replace `25C1-XXX` with your actual handle (e.g., `25C1-125`)
6. **Send**: Click the blue "Send" button

###  View Your Profile
- Your profile data will appear in the response section below
- Look for your name, company, and LinkedIn in the response
--

## 📝 Handle Format
Your handle follows: `25C1-XXX` (where XXX is your 3-digit number)
