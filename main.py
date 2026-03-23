import streamlit as st
import asyncio
import os
import threading
from highrise import BaseBot
from highrise.__main__ import main

# Room aur Token (Aapne jo diye wahi hain)
ROOM_ID = "68e27f6e9796e3239f1cd493"
TOKEN = "e0e463181e9c0a828c53c5ac24348b03dbcd1c5a0a8c3f5bc9efc36bddb901dc"

class Bot(BaseBot):
    async def on_start(self, session_metadata):
        print("Bot is in!")
        st.success("✅ BOT CONNECTED!")

st.title("Highrise Bot Launcher")

def start_bot():
    os.environ["API_TOKEN"] = TOKEN
    os.environ["ROOM_ID"] = ROOM_ID
    # Isse bot start hoga
    asyncio.run(main(["main:Bot"]))

if st.button("🚀 ACTIVATE BOT"):
    st.info("Starting...")
    threading.Thread(target=start_bot, daemon=True).start()
