from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt
import json
import datetime

app = FastAPI(title="Personal Data API", description="Get your cohort data by email")

SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
security = HTTPBearer()

class HandleRequest(BaseModel):
    handle: str

class LoginRequest(BaseModel):
    email: str

def create_token(email: str):
    return jwt.encode({"email": email, "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24)}, SECRET_KEY, ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["email"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def log_request(handle: str, success: bool):
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "handle": handle,
        "success": success
    }
    try:
        with open('requests.json', 'r') as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []
    
    logs.append(log_entry)
    with open('requests.json', 'w') as f:
        json.dump(logs, f, indent=2)

@app.post("/auth/login")
async def login(request: LoginRequest):
    with open('people.json', 'r') as f:
        people = json.load(f)
    
    for person in people.values():
        if person['email'] == request.email:
            return {"token": create_token(request.email)}
    
    raise HTTPException(status_code=401, detail="Email not found")

@app.post("/get-profile")
async def get_profile(request: HandleRequest, _: str = Depends(verify_token)):
    try:
        with open('people.json', 'r') as f:
            people = json.load(f)
        
        if request.handle not in people:
            log_request(request.handle, False)
            raise HTTPException(status_code=404, detail="Handle not found")
        
        person = people[request.handle]
        log_request(request.handle, True)
        
        return {
            "message": f"🎉 Hey {person['name']}! Here's your amazing profile:",
            "data": {
                "handle": person['handle'],
                "name": person['name'],
                "company": f"💼 {person['company']}",
                "linkedin": person['linkedin'],
                "email": person['email']
            },
            "fun_fact": f"You're part of an exclusive cohort of {len(people)} amazing people!"
        }
    
    except Exception as e:
        log_request(request.handle, False)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    try:
        with open('requests.json', 'r') as f:
            logs = json.load(f)
        total = len(logs)
        success = sum(1 for log in logs if log['success'])
        unique = len(set(log.get('handle', log.get('email', '')) for log in logs))
        recent = logs[-5:] if logs else []
    except FileNotFoundError:
        total = success = unique = 0
        recent = []
    
    return f"""
    <html><head><title>API Dashboard</title>
    <meta http-equiv="refresh" content="30"></head>
    <body style="font-family:Arial;margin:40px;background:#f5f5f5">
    <h1>📊 API Dashboard</h1>
    <div style="display:flex;gap:20px;margin:20px 0">
    <div style="background:white;padding:20px;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.1)">
    <h3>Total Requests</h3><h2 style="color:#2196F3">{total}</h2></div>
    <div style="background:white;padding:20px;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.1)">
    <h3>Successful</h3><h2 style="color:#4CAF50">{success}</h2></div>
    <div style="background:white;padding:20px;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.1)">
    <h3>Unique Users</h3><h2 style="color:#FF9800">{unique}</h2></div>
    </div>
    <div style="background:white;padding:20px;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.1)">
    <h3>Recent Requests</h3>
    {''.join(f'<p>{log["timestamp"][:19]} - {log.get("handle", log.get("email", "unknown"))} - {"✅" if log["success"] else "❌"}</p>' for log in recent)}
    </div></body></html>"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
