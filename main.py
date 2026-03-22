import streamlit as st
import asyncio
import os
import threading
from highrise import BaseBot, User, Position
from highrise.__main__ import main

# --- AAPKA DATA (Hardcoded for testing) ---
# Ram, agar ye test successful ho jaye toh hum ise baad mein Secrets mein shift kar denge
MY_TOKEN = "e0e463181e9c0a828c53c5ac24348b03dbcd1c5a0a8c3f5bc9efc36bddb901dc"
MY_ROOM_ID = "68e27f6e9796e3239f1cd493"

class Bot(BaseBot):
    async def on_start(self, session_metadata):
        st.write("✨ BOT IS CONNECTED TO HIGHRISE!")
        print("Bot is online!")
        await self.highrise.send_emote("emote-dance-tiktok")

    async def on_user_join(self, user: User, position: Position):
        await self.highrise.chat(f"Welcome {user.username}!")

# --- STREAMLIT INTERFACE ---
st.title("🤖 Highrise Bot Final Launcher")

def run_bot():
    os.environ["API_TOKEN"] = MY_TOKEN
    os.environ["ROOM_ID"] = MY_ROOM_ID
    
    # Ye 'main:Bot' batata hai ki isi file (main.py) ki Bot class use karo
    definitions = ["main:Bot"]
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main(definitions))
    except Exception as e:
        st.error(f"❌ Connection Failed: {e}")

if st.button("🚀 LAUNCH BOT"):
    st.info("Starting connection... Check your Highrise room in 20 seconds.")
    threading.Thread(target=run_bot, daemon=True).start()
