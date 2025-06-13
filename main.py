from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
import random

app = FastAPI()

BOTS = [
    "Silent_File_Store_6_Bot",
    "Silent_File_Store_1_Bot",
    "Silent_File_Store_3_Bot"
]

bot = random.choice(BOTS)

@app.get("/")
def dash():
    return "Moye Moye!"

@app.get("/server/{code}", response_class=HTMLResponse)
async def show_redirect_page(code: str):
    telegram_url = f"https://t.me/{bot}?start={code}"
    return RedirectResponse(url=telegram_url)
    
@app.get("/advance/{code}", response_class=HTMLResponse)
async def show_advance_page(code: str):
    telegram_url = f"https://t.me/{bot}?start={code}"
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>DSxSilent Telegram File Bot</title>
        <style>
            body {{
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: linear-gradient(135deg, #e0f7fa, #e1bee7);
                color: #222;
                overflow: hidden;
            }}
            h1 {{
                color: #3f51b5;
                margin-bottom: 20px;
            }}
            .timer-container {{
                position: relative;
                width: 150px;
                height: 150px;
                margin-bottom: 30px;
            }}
            .circle {{
                width: 150px;
                height: 150px;
                border-radius: 50%;
                background: conic-gradient(#3f51b5 0deg, #ccc 0deg);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 30px;
                font-weight: bold;
                color: #3f51b5;
                transition: all 0.3s ease-in-out;
            }}
            #getFileBtn {{
                padding: 14px 24px;
                font-size: 16px;
                background: #9c27b0;
                border: none;
                border-radius: 30px;
                color: white;
                cursor: not-allowed;
                opacity: 0.5;
                transition: all 0.3s ease;
            }}
            #getFileBtn.active {{
                cursor: pointer;
                opacity: 1;
                background: linear-gradient(90deg, #8e24aa, #7b1fa2);
                animation: pulse 1s infinite;
            }}
            @keyframes pulse {{
                0% {{ transform: scale(1); }}
                50% {{ transform: scale(1.05); }}
                100% {{ transform: scale(1); }}
            }}
            footer {{
                position: fixed;
                bottom: 15px;
                font-size: 14px;
                color: #666;
                text-align: center;
                width: 100%;
            }}
        </style>
    </head>
    <body>
        <h1>DSxSilent Telegram File Bot</h1>
        <div class="timer-container">
            <div class="circle" id="timer">10</div>
        </div>
        <button id="getFileBtn" disabled onclick="window.location.href='{telegram_url}'">Get File</button>
        <footer>This website is made by Sanchit</footer>

        <script>
            let seconds = 10;
            const timer = document.getElementById("timer");
            const button = document.getElementById("getFileBtn");
            const circle = document.querySelector(".circle");

            const interval = setInterval(() => {{
                seconds--;
                if (seconds >= 0) {{
                    timer.textContent = seconds;
                    let angle = (10 - seconds) * 36;
                    circle.style.background = `conic-gradient(#3f51b5 ${angle}deg, #ccc ${angle}deg)`;
                }}
                if (seconds <= 0) {{
                    clearInterval(interval);
                    timer.textContent = "✔";
                    button.disabled = false;
                    button.classList.add("active");
                }}
            }}, 1000);
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
