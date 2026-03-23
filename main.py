import streamlit as st
import asyncio
import os
import threading
from highrise import BaseBot
from highrise.__main__ import main

class Bot(BaseBot):
    async def on_start(self, session_metadata):
        print("Bot is in the room!")
        st.success("🎉 Bot Online!")

st.title("🤖 SuperBotRam")

def run_bot():
    # Streamlit Secrets se data lena
    os.environ["API_TOKEN"] = st.secrets["API_TOKEN"]
    os.environ["ROOM_ID"] = st.secrets["ROOM_ID"]
    asyncio.run(main(["main:Bot"]))

if st.button("🚀 ACTIVATE"):
    threading.Thread(target=run_bot, daemon=True).start()
    st.info("Bot starting...")
