import streamlit as st
import asyncio
import os
import threading
from highrise import BaseBot
from highrise.__main__ import main

# Aapka Data (Seedha yahan set kar diya hai)
TOKEN = "e0e463181e9c0a828c53c5ac24348b03dbcd1c5a0a8c3f5bc9efc36bddb901dc"
ROOM = "68e27f6e9796e3239f1cd493"

class Bot(BaseBot):
    async def on_start(self, session_metadata):
        st.success("✅ BOT IS ONLINE!")

st.title("🤖 Highrise Bot Fixer")

def launch():
    os.environ["API_TOKEN"] = TOKEN
    os.environ["ROOM_ID"] = ROOM
    # Bot ko start karne ka sahi tarika
    asyncio.run(main(["main:Bot"]))

if st.button("🚀 ACTIVATE"):
    st.info("Connecting... 1 minute wait karein.")
    threading.Thread(target=launch, daemon=True).start()
