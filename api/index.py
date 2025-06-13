from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
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
    telegram_url = f"https://t.me/{bot}?start={code}"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DSxSilent Telegram File Bot</title>
        <style>
            body {{ text-align: center; padding-top: 100px; font-family: Arial; }}
            h1 {{ color: #2a9d8f; }}
            #getFileBtn {{ display: none; padding: 12px 20px; font-size: 16px; background: #264653; color: white; border: none; border-radius: 5px; cursor: pointer; }}
            footer {{ position: fixed; bottom: 10px; width: 100%; color: #888; }}
        </style>
    </head>
    <body>
        <h1>DSxSilent Telegram File Bot</h1>
        <p>Wait 10 seconds to get your file...</p>
        <button id="getFileBtn" onclick="window.location.href='{telegram_url}'">Get File</button>
        <footer>This website is made by Sanchit</footer>
        <script>
            setTimeout(() => {{
                document.getElementById("getFileBtn").style.display = "inline-block";
            }}, 10000);
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
