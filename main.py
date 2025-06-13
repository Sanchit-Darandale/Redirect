from fastapi import FastAPI
from threading import Thread
import time
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is alive!"}

def keep_alive():
    while True:
        try:
            print("⏳ Sending keep-alive ping...")
            requests.get("https://dsxfilestore.onrender.com/")
        except Exception as e:
            print("❌ Keep-alive failed:", e)
        time.sleep(900)  # every 15 minutes

@app.on_event("startup")
def start_keep_alive():
    Thread(target=keep_alive, daemon=True).start()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
