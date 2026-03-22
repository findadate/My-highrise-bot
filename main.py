import streamlit as st
import asyncio
import os
import threading
from highrise import BaseBot
from highrise.__main__ import main

class MyBot(BaseBot):
    async def on_start(self, session_metadata):
        st.write("✅ BOT LOGIN SUCCESSFUL!")
        print("Bot is in the room!")

st.title("🤖 Highrise Bot Debugger")

# Check Secrets
token = st.secrets.get("API_TOKEN")
room = st.secrets.get("ROOM_ID")

if not token or not room:
    st.error("❌ Secrets missing! Please add API_TOKEN and ROOM_ID.")
else:
    st.success(f"Secrets loaded! Room: {room[:5]}...")

def run_bot():
    os.environ["API_TOKEN"] = token
    os.environ["ROOM_ID"] = room
    try:
        asyncio.run(main(["main:MyBot"]))
    except Exception as e:
        st.error(f"⚠️ Connection Error: {e}")

if st.button("🚀 Force Start Bot"):
    threading.Thread(target=run_bot, daemon=True).start()
    st.info("Bot waking up... please wait.")
