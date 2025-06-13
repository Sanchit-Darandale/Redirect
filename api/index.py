from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import random

app = FastAPI()

# List of bot usernames
BOTS = ["Silent_File_Store_6_Bot", "Silent_File_Store_1_Bot", "Silent_File_Store_3_Bot"]

@app.get("/")
def dash():
    return "Moye Moye!"
    
@app.get("/server/{code}", response_class=HTMLResponse)
async def show_redirect_page(code: str):
    bot = random.choice(BOTS)
    # Construct Telegram URL
    redirect_url = f"https://t.me/{bot}?start={code}"
    return RedirectResponse(url=redirect_url)
