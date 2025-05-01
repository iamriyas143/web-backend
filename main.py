from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi import HTTPException

app = FastAPI()

# Allow requests from your frontend's domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://file.download1.netlify.app"],  # replace with your actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File links
FILES = {
    "abc123": {
        "token": "xyz123abc123",
        "url": "https://images.app.goo.gl/V9J1jjiqLmMASrP89"
    },
    "xyz456": {
        "token": "abc123xyz123",
        "url": "https://youtu.be/a3Ue-LN5B9U?si=lQel_ypvIkbDuG2u"
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
