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
   - Add these two headers:
     
     **Header 1:**
     - **Key:** `Content-Type`
     - **Value:** `application/json`
     
     **Header 2:**
     - **Key:** `Authorization`
     - **Value:** `Bearer YOUR_TOKEN_HERE`
     - Replace `YOUR_TOKEN_HERE` with your copied token

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

## Important Details

### Authentication Token
- **Location:** Authorization header
- **Format:** `Bearer YOUR_TOKEN`
- **Validity:** 24 hours
- **Note:** Always include "Bearer " before your token

### Handle Format
- **Pattern:** `25C1-XXX`
- **Example:** `25C1-001`, `25C1-015`
- **Range:** 001 to 015

### Headers Required
All requests need:
- `Content-Type: application/json`
- Profile requests also need: `Authorization: Bearer YOUR_TOKEN`

## Troubleshooting

**"Email not found"**
- Use exact email from registration
- Contact admin if email should be registered

**"Invalid token"**
- Get new token using login endpoint
- Check "Bearer " prefix in Authorization header
- Ensure complete token copied (starts with `eyJ`)

**"Handle not found"**
- Verify handle format: `25C1-XXX`
- Check your assigned number

**Request fails**
- Verify internet connection
- Check URL spelling
- Ensure all headers are set correctly
- Make sure request method is POST for both endpoints

## Step 4: View API Statistics (Optional)

You can view live API usage statistics without authentication:

1. **Open Browser**
   - Go to: `https://web-production-4f250.up.railway.app/dashboard`
   - No authentication needed
   - Page auto-refreshes every 30 seconds

2. **Dashboard Shows:**
   - Total API requests
   - Successful requests
   - Unique users
   - Recent activity

## Quick Reference

### Login Endpoint
- **URL:** `/auth/login`
- **Method:** POST
- **Body:** `{"email": "your-email"}`
- **Headers:** `Content-Type: application/json`

### Profile Endpoint  
- **URL:** `/get-profile`
- **Method:** POST
- **Body:** `{"handle": "25C1-XXX"}`
- **Headers:** 
  - `Content-Type: application/json`
  - `Authorization: Bearer YOUR_TOKEN`

### Dashboard (Browser)
- **URL:** `/dashboard`
- **Method:** GET (open in browser)
- **Auth:** None required
