import streamlit as st
import asyncio
import os
import threading
from highrise import BaseBot
from highrise.__main__ import main

# Aapka Data
TOKEN = "e0e463181e9c0a828c53c5ac24348b03dbcd1c5a0a8c3f5bc9efc36bddb901dc"
ROOM = "68e27f6e9796e3239f1cd493"

class Bot(BaseBot):
    async def on_start(self, session_metadata):
        st.success("✅ BOT ROOM MEIN HAI!")

st.title("🤖 SuperBot Launcher")

def run():
    os.environ["API_TOKEN"] = TOKEN
    os.environ["ROOM_ID"] = ROOM
    # Isse aapka bot connect hoga
    asyncio.run(main(["main:Bot"]))

if st.button("🚀 ACTIVATE"):
    st.info("Connecting... 1 minute wait karein.")
    threading.Thread(target=run, daemon=True).start()