# Surprise Me API - Complete Guide

Get your cohort profile data using this secure API. Follow these steps to authenticate and retrieve your information.

## Step 1: Install Postman

1. **Download Postman**
   - Visit [postman.com/downloads](https://www.postman.com/downloads/)
   - Choose your operating system (Windows/Mac/Linux)
   - Download and install the application

2. **Create Account**
   - Open Postman after installation
   - Click "Create Account" or "Sign Up"
   - Use your email and create a password
   - Verify your email if prompted

3. **Start Using**
   - Open Postman
   - Skip workspace setup (click "Skip" if asked)
   - You're ready to make requests!

## Step 2: Get Your Authentication Token

### Create Login Request
1. **New Request**
   - Click "New" button in Postman
   - Select "HTTP Request"
<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/842c8efb-8bda-4d9e-a8c0-a52cc813d8eb" />

2. **Set Request Method**
   - Change dropdown from "GET" to **POST**

3. **Enter URL**
   ```
   https://web-production-4f250.up.railway.app/auth/login
   ```

4. **Add Headers**
   - Click "Headers" tab
   - Add new header:
     - **Key:** `Content-Type`
     - **Value:** `application/json`

5. **Add Request Body**
   - Click "Body" tab
   - Select "raw" radio button
   - In the text area, enter:
   ```json
   {
     "email": "your-email@example.com"
   }
   ```
   - Replace with your actual registered email

6. **Send Request**
   - Click blue "Send" button
   - Copy the token from response (starts with `eyJ...`)

### Expected Response
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```
<img width="600" height="400" alt="Screenshot 2025-08-15 171411" src="https://github.com/user-attachments/assets/91900de2-ef06-40b7-af92-f7d6e4d1922b" />


## Step 3: Get Your Profile Data

### Create Profile Request
1. **New Request**
   - Click "New" → "HTTP Request"

2. **Set Method**
   - Change to **POST**

3. **Enter URL**
   ```
   https://web-production-4f250.up.railway.app/get-profile
   ```

4. **Add Headers**
   - Click "Headers" tab
   - Add first header:
     - **Key:** `Content-Type`
     - **Value:** `application/json`
   
   - Click "Authorization" tab (next to Headers)
   - Select "Bearer Token" from dropdown
   - In the "Token" field, paste your copied token (without "Bearer " prefix)

5. **Add Request Body**
   - Click "Body" tab
   - Select "raw"
   - Enter:
   ```json
   {
     "handle": "25C1-XXX"
   }
   ```
   - Replace `XXX` with your 3-digit number (e.g., `25C1-001`)

6. **Send Request**
   - Click "Send"
   - Your profile data will appear below
<img width="600" height="350" alt="Screenshot 2025-08-15 171703" src="https://github.com/user-attachments/assets/cff59562-206c-42d0-9b53-404450fa2c25" />
<img width="600" height="400" alt="Screenshot 2025-08-15 171643" src="https://github.com/user-attachments/assets/63c7eafc-525e-4c6c-9049-073733262eec" />


### Expected Response
```json
{
  "message": "🎉 Hey [Your Name]! Here's your amazing profile:",
  "data": {
    "handle": "25C1-001",
    "name": "Your Name",
    "company": "💼 Your Company",
    "linkedin": "Your LinkedIn URL",
    "email": "your-email@example.com"
  },
  "fun_fact": "You're part of an exclusive cohort of 15 amazing people!"
}
```
