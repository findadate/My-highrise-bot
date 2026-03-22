import streamlit as st
import asyncio
import os
import threading
import sys
from highrise import BaseBot, User, Position
from highrise.__main__ import main

# --- AAPKA BOT ENGINE ---
class MyBot(BaseBot):
    async def on_start(self, session_metadata):
        st.success("🎉 BOT SUCCESSFULLY JOINED THE ROOM!")
        print("Bot is in!")
        await self.highrise.send_emote("emote-dance-tiktok")

    async def on_user_join(self, user: User, position: Position):
        await self.highrise.chat(f"Welcome {user.username}! ❤️")

# --- STREAMLIT DASHBOARD ---
st.title("🚀 Highrise Bot: Final Launch")

# 1. Check Secrets
token = st.secrets.get("API_TOKEN")
room = st.secrets.get("ROOM_ID")

if not token or not room:
    st.error("❌ Secrets missing! Please add API_TOKEN and ROOM_ID in Settings.")
else:
    st.info(f"Checking Connection for Room: {room}")

def start_bot():
    os.environ["API_TOKEN"] = token
    os.environ["ROOM_ID"] = room
    # 'main:MyBot' ka matlab isi file ka bot use karo
    definitions = ["main:MyBot"]
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main(definitions))
    except Exception as e:
        st.error(f"⚠️ Highrise Error: {e}")

# Button to Start
if st.button("🔥 ACTIVATE BOT NOW"):
    st.warning("Connecting... Please check your Highrise Room in 30 seconds.")
    threading.Thread(target=start_bot, daemon=True).start()
