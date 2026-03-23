import streamlit as st
import asyncio
import os
import threading
from highrise import BaseBot, User, Position
from highrise.__main__ import main

class Bot(BaseBot):
    async def on_start(self, session_metadata):
        st.success("🎉 MUBARAK HO! Bot room mein aa gaya hai.")
        await self.highrise.send_emote("emote-dance-tiktok")

    async def on_user_join(self, user: User, position: Position):
        await self.highrise.chat(f"Swagat hai {user.username}!")

st.title("🤖 SuperBotRam Control Panel")

def start_bot():
    # Secrets se data load karna
    os.environ["API_TOKEN"] = st.secrets["API_TOKEN"]
    os.environ["ROOM_ID"] = st.secrets["ROOM_ID"]
    
    definitions = ["main:Bot"]
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main(definitions))
    except Exception as e:
        st.error(f"Error: {e}")

if st.button("🚀 ACTIVATE BOT"):
    st.info("Connecting... 30 seconds wait karein.")
    threading.Thread(target=start_bot, daemon=True).start()

