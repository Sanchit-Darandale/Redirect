from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import random

app = FastAPI()

# List of bot usernames
BOTS = ["Silent_File_Store_6_Bot", "Silent_File_Store_1_Bot", "@Silent_File_Store_3_Bot"]

@app.get("/server/{code}")
def redirect_to_bot(code: str):
    # Pick a random bot
    bot = random.choice(BOTS)
    # Construct Telegram URL
    redirect_url = f"https://t.me/{BOTS}?start={code}"
    return RedirectResponse(url=redirect_url)
