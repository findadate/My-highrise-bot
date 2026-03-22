import streamlit as st
import asyncio
import os
import threading
from highrise import BaseBot
from highrise.__main__ import main

# --- YE AAPKA BOT CODE HAI ---
class MyBot(BaseBot):
    async def on_start(self, session_metadata):
        print("Bot is online and ready!")
    
    async def on_chat(self, user, message):
        if message.lower() == "!hello":
            await self.highrise.chat(f"Hello {user.username}!")

# --- YE STREAMLIT KA SYSTEM HAI ---
st.title("🤖 Highrise Bot Control")

def run_bot():
    token = st.secrets.get("API_TOKEN")
    room = st.secrets.get("ROOM_ID")
    
    if token and room:
        os.environ["API_TOKEN"] = token
        os.environ["ROOM_ID"] = room
        # Humne class ka naam MyBot rakha hai
        definitions = ["main:MyBot"] 
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(main(definitions))
        except Exception as e:
            st.error(f"Error: {e}")

if st.button("🚀 Start My Bot"):
    st.info("Trying to connect... Please wait 30 seconds.")
    threading.Thread(target=run_bot, daemon=True).start()
    st.success("Connection process started! Check your room.")
