from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi import HTTPException

app = FastAPI()

# Allow requests from your frontend's domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-site.netlify.app"],  # replace with your actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File links
FILES = {
    "abc123": {
        "token": "securetoken",
        "url": "https://files.com/file1.txt"
    },
    "xyz456": {
        "token": "anotherToken",
        "url": "https://drive.google.com/uc?id=abc123&export=download"
    }
}

@app.get("/download")
async def download(hash: str, token: str):
    file_entry = FILES.get(hash)
    if not file_entry:
        raise HTTPException(status_code=404, detail="Invalid hash")

    if file_entry["token"] != token:
        raise HTTPException(status_code=403, detail="Invalid token")

    return RedirectResponse(url=file_entry["url"])
