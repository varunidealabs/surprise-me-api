# Surprise Me API

Personal profile API with JWT authentication. Get your cohort data securely using your email and unique handle.

## 🔐 Authentication Required

**Important:** All profile requests now require authentication. You must first login with your email to get a token.

## 🚀 API Endpoints

### 1. Login Endpoint (Get Your Token)
**URL:** `https://web-production-4f250.up.railway.app/auth/login`
**Method:** POST

**Request:**
```json
{
  "email": "your-email@example.com"
}
```

**Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### 2. Profile Endpoint (Get Your Data)
**URL:** `https://web-production-4f250.up.railway.app/get-profile`
**Method:** POST
**Authentication:** Bearer Token Required

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

## 📱Complete Guide to Make API Requests

### Step 1: Install Postman
1. Go to [postman.com](https://www.postman.com/downloads/)

2. Download Postman for your computer (Windows/Mac/Linux)
3. Install and create a free account (or sign in if you have one)

### Step 2: First Login to Get Your Token
1. **Open Postman** → Click "New" → Select "HTTP Request"
   
ModuleNotFoundError: No module named 'jose'

Traceback (most recent call last):

  File "/opt/venv/bin/uvicorn", line 8, in <module>

    sys.exit(main())

             ^^^^^^

  File "/opt/venv/lib/python3.12/site-packages/click/core.py", line 1442, in __call__

    return self.main(*args, **kwargs)

           ^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/venv/lib/python3.12/site-packages/click/core.py", line 1363, in main

    rv = self.invoke(ctx)

         ^^^^^^^^^^^^^^^^

  File "/opt/venv/lib/python3.12/site-packages/click/core.py", line 1226, in invoke

    return ctx.invoke(self.callback, **ctx.params)

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/venv/lib/python3.12/site-packages/click/core.py", line 794, in invoke

    return callback(*args, **kwargs)

           ^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/venv/lib/python3.12/site-packages/uvicorn/main.py", line 416, in main

    run(

  File "/opt/venv/lib/python3.12/site-packages/uvicorn/main.py", line 587, in run

    server.run()

  File "/opt/venv/lib/python3.12/site-packages/uvicorn/server.py", line 61, in run

    return asyncio.run(self.serve(sockets=sockets))

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/root/.nix-profile/lib/python3.12/asyncio/runners.py", line 194, in run

    return runner.run(main)

           ^^^^^^^^^^^^^^^^

  File "/root/.nix-profile/lib/python3.12/asyncio/runners.py", line 118, in run

    return self._loop.run_until_complete(task)

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/root/.nix-profile/lib/python3.12/asyncio/base_events.py", line 687, in run_until_complete

    return future.result()

           ^^^^^^^^^^^^^^^

  File "/opt/venv/lib/python3.12/site-packages/uvicorn/server.py", line 68, in serve

    config.load()

  File "/opt/venv/lib/python3.12/site-packages/uvicorn/config.py", line 467, in load

    self.loaded_app = import_from_string(self.app)

                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/venv/lib/python3.12/site-packages/uvicorn/importer.py", line 24, in import_from_string

    raise exc from None

  File "/opt/venv/lib/python3.12/site-packages/uvicorn/importer.py", line 21, in import_from_string

    module = importlib.import_module(module_str)

             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module

    return _bootstrap._gcd_import(name[level:], package, level)

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import

  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load

  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked

  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked

  File "<frozen importlib._bootstrap_external>", line 995, in exec_module

  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed

  File "/app/app.py", line 5, in <module>

    from jose import JWTError, jwt

ModuleNotFoundError: No module named 'jose'
2. **Set Method**: Change dropdown from "GET" to **"POST"**
3. **Enter Login URL**: Copy and paste:
   ```
   https://web-production-4f250.up.railway.app/auth/login
   ```

4. **Add Headers**: Click "Headers" tab → Add:
   - Key: `Content-Type`
   - Value: `application/json`

5. **Add Body**: Click "Body" tab → Select **"raw"** → Paste:
   ```json
   {
     "email": "your-actual-email@example.com"
   }
   ```
   
   Replace `your-actual-email@example.com` with your real email address

6. **Send**: Click the blue "Send" button
7. **Copy Token**: From the response, copy the token value (long string starting with `eyJ...`)

### Step 3: Use Token to Get Your Profile
1. **Create New Request**: Click "New" → Select "HTTP Request"
2. **Set Method**: Change dropdown to **"POST"**
3. **Enter Profile URL**: Copy and paste:
   ```
   https://web-production-4f250.up.railway.app/get-profile
   ```
   
   <img width="1052" height="123" alt="image" src="https://github.com/user-attachments/assets/d7454031-14dd-410c-b5fa-54c403186792" />

4. **Add Headers**: Click "Headers" tab → Add these two headers:
   - Key: `Content-Type`, Value: `application/json`
   - Key: `Authorization`, Value: `Bearer YOUR_TOKEN_HERE`
     
     Replace `YOUR_TOKEN_HERE` with the token you copied from step 2
     
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

### Step 4: View Your Profile
- Your profile data will appear in the response section below
- Look for your name, company, and LinkedIn in the response
- If you get an "Invalid token" error, repeat Step 2 to get a fresh token

## 📝 Important Information

### Handle Format
Your handle follows: `25C1-XXX` (where XXX is your 3-digit number)

### Token Expiry
- Tokens are valid for 24 hours
- If you get authentication errors, get a new token by repeating Step 2

### Security Notes
- Never share your authentication token
- Your email must be registered in the system to get a token
- Tokens are automatically generated when you login with a valid email

## 🔧 Troubleshooting

### Common Issues:

**"Email not found" Error:**
- Make sure you're using the exact email address from your registration
- Contact admin if your email should be in the system

**"Invalid token" Error:**
- Get a new token by calling the login endpoint again
- Make sure you're using `Bearer ` prefix in Authorization header
- Check that the token is copied completely (starts with `eyJ`)

**"Handle not found" Error:**
- Verify your handle format: `25C1-XXX`
- Make sure you're using your assigned 3-digit number

**Request Failed:**
- Check your internet connection
- Verify the URL is correct
- Ensure Content-Type header is set to `application/json`
