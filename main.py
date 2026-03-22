import streamlit as st
import asyncio
import os
import threading
from highrise import BaseBot, User, Position
from highrise.__main__ import main

# --- YE AAPKA BOT HAI (Directly inside main.py) ---
class MyBot(BaseBot):
    async def on_start(self, session_metadata):
        print("✅ BOT IS ONLINE!")
        # Bot aate hi dance karega
        await self.highrise.send_emote("emote-dance-tiktok")

    async def on_user_join(self, user: User, position: Position):
        # Naye bande ko welcome message aur wave
        await self.highrise.chat(f"Welcome to the room, {user.username}! ❤️")
        await self.highrise.send_emote("emote-hello", user.id)

    async def on_chat(self, user: User, message: str):
        if message.lower() == "!hello":
            await self.highrise.chat(f"Hi {user.username}! I am your bot.")

# --- STREAMLIT CONTROL PANEL ---
st.set_page_config(page_title="Highrise Bot")
st.title("🤖 My Highrise Bot")

def start_bot_now():
    # Secrets se token/room lena
    token = st.secrets.get("API_TOKEN")
    room = st.secrets.get("ROOM_ID")
    
    if token and room:
        os.environ["API_TOKEN"] = token
        os.environ["ROOM_ID"] = room
        # "main:MyBot" ka matlab hai isi file mein MyBot class dhoondo
        definitions = ["main:MyBot"] 
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(main(definitions))
        except Exception as e:
            print(f"Error: {e}")

# Agar bot pehle se nahi chal raha toh start karein
if "running" not in st.session_state:
    st.info("Starting bot... Please check your room in 1 minute.")
    threading.Thread(target=start_bot_now, daemon=True).start()
    st.session_state.running = True

st.success("Bot process is active!")
st.write("Ab aap Highrise room mein jaiye, bot wahan aapka intezaar kar raha hoga.")
