from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

app = FastAPI()

# Predefined file links with hashed URLs and tokens
FILES = {
    # Example: sha256("https://files.com/file1.txt")
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
