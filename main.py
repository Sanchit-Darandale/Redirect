from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
import random

app = FastAPI()

BOTS = [
    "Silent_File_Store_6_Bot",
    "Silent_File_Store_1_Bot",
    "Silent_File_Store_3_Bot"
]

last_bot = None  # Global variable to store the last selected bot

def get_random_bot():
    global last_bot
    available_bots = [b for b in BOTS if b != last_bot]
    bot = random.choice(available_bots)
    last_bot = bot
    return bot
    
@app.get("/")
def dash():
    return "Moye Moye!"

@app.get("/server/{code}", response_class=HTMLResponse)
async def show_redirect_page(code: str):
    bot = get_random_bot()
    telegram_url = f"https://t.me/{bot}?start={code}"
    return RedirectResponse(url=telegram_url)

@app.get("/advance/{code}", response_class=HTMLResponse)
async def show_advance_page(code: str):
    bot = get_random_bot()
    telegram_url = f"https://t.me/{bot}?start={code}"
    html_content = f"""
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>DSxSilent File Store System</title>
    <style>
        :root {{
            --bg-light: #f3f8ff;
            --bg-dark: #1e1e2f;
            --card-light: #ffffff;
            --card-dark: #2c2c3a;
            --text-light: #222;
            --text-dark: #eee;
            --primary: #3f51b5;
            --accent: #ab47bc;
            --timer: #90caf9;
            --timer-bg: #e0e0e0;
        }}

        [data-theme="light"] {{
            background: var(--bg-light);
            color: var(--text-light);
        }}

        [data-theme="dark"] {{
            background: var(--bg-dark);
            color: var(--text-dark);
        }}

        body {{
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            transition: background 0.3s ease, color 0.3s ease;
        }}

        .container {{
            width: 75%;
            max-width: 480px;
            padding: 1.5rem;
            border-radius: 16px;
            background: var(--card-light);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
            text-align: center;
            position: relative;
            transition: background 0.3s ease;
        }}

        [data-theme="dark"] .container {{
            background: var(--card-dark);
        }}

        .header {{
            position: absolute;
            top: 12px;
            left: 16px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .header img {{
            width: 36px;
            height: 36px;
            border-radius: 50%;
        }}

        .toggle {{
            position: absolute;
            top: 14px;
            right: 16px;
            cursor: pointer;
            font-size: 14px;
            padding: 6px 12px;
            border-radius: 20px;
            background: var(--accent);
            color: white;
            border: none;
            transition: background 0.3s;
        }}

        h1 {{
            margin-top: 50px;
            font-size: 1.5rem;
            color: var(--primary);
        }}

        .timer-container {{
            margin: 24px auto;
            width: 150px;
            height: 150px;
            position: relative;
        }}

        .circle {{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            background: conic-gradient(var(--timer) 0deg, var(--timer-bg) 0deg);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: bold;
            color: var(--primary);
            transition: background 0.3s;
            position: relative;
        }}

        .emoji {{
            position: absolute;
            font-size: 2rem;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            animation: pop 1s ease;
            display: none;
        }}

        @keyframes pop {{
            0% {{ transform: scale(0) translate(-50%, -50%); opacity: 0; }}
            50% {{ transform: scale(1.4) translate(-50%, -50%); opacity: 1; }}
            100% {{ transform: scale(1) translate(-50%, -50%); opacity: 1; }}
        }}

        #getFileBtn {{
            width: 100%;
            padding: 14px;
            font-size: 1rem;
            background: var(--accent);
            border: none;
            border-radius: 30px;
            color: white;
            opacity: 0.6;
            cursor: not-allowed;
            transition: all 0.3s ease;
        }}

        #getFileBtn.active {{
            opacity: 1;
            cursor: pointer;
            animation: pulse 1s infinite;
        }}

        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}

        footer {{
            margin-top: 20px;
            font-size: 0.85rem;
            color: #777;
        }}

        @media (max-width: 480px) {{
            h1 {{ font-size: 1.25rem; }}
            .circle {{ width: 120px; height: 120px; font-size: 1.5rem; }}
            .timer-container {{ width: 120px; height: 120px; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <span>Silent Ghost ⚡</span>
        </div>
        <button class="toggle" id="toggleBtn" onclick="toggleTheme()">🖤 Dark Mode</button>

        <h1>DSxSilent File Bot</h1>

        <div class="timer-container">
            <div class="circle" id="timer">10</div>
            <div class="emoji" id="emoji">✓</div>
        </div>

        <button id="getFileBtn">Get Telegram File</button>
        <footer>Made with ❤️ by Sanchit</footer>
    </div>

    <script>
        let seconds = 10;
        const timer = document.getElementById("timer");
        const button = document.getElementById("getFileBtn");
        const circle = document.querySelector(".circle");
        const emoji = document.getElementById("emoji"); 
        const telegramUrl = '{telegram_url}';
    
        const interval = setInterval(() => {{
            seconds--;
            if (seconds >= 0) {{
                timer.textContent = seconds;
                let angle = (10 - seconds) * 36;
                circle.style.background = `conic-gradient(var(--timer) ${{angle}}deg, var(--timer-bg) ${{angle}}deg)`;
            }}
            if (seconds <= 0) {{
                clearInterval(interval);
                timer.textContent = "✓";
                emoji.style.display = "block";
                button.disabled = false;
                button.classList.add("active");
                button.onclick = () => window.location.href = telegramUrl;
            }}
        }}, 1000);

        function toggleTheme() {{
            const html = document.documentElement;
            const btn = document.getElementById("toggleBtn");
            const currentTheme = html.getAttribute("data-theme");
            if (currentTheme === "light") {{
                html.setAttribute("data-theme", "dark");
                btn.textContent = "🤍 Light Mode";
            }} else {{
                html.setAttribute("data-theme", "light");
                btn.textContent = "🖤 Dark Mode";
            }}
        }}
    </script>
</body>
</html>
"""
    return HTMLResponse(content=html_content)
