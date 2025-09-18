from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
import string, random

app = FastAPI()

# In-memory storage for demo
url_store = {}

class URLRequest(BaseModel):
    url: HttpUrl

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.post("/shorten")
def shorten_url(request: URLRequest):
    short_code = generate_short_code()
    while short_code in url_store:
        short_code = generate_short_code()
    url_store[short_code] = request.url
    return {"short_url": f"/" + short_code}

@app.get("/{short_code}")
def redirect_url(short_code: str, req: Request):
    url = url_store.get(short_code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url)
