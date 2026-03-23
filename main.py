import streamlit as st
import os
from highrise.__main__ import main
import asyncio

# Seedha Token aur ID yahan likh dete hain (Sirf test ke liye)
# Ram, agar ye chal gaya toh hum ise baad mein badal denge
os.environ["API_TOKEN"] = "e0e463181e9c0a828c53c5ac24348b03dbcd1c5a0a8c3f5bc9efc36bddb901dc"
os.environ["ROOM_ID"] = "68e27f6e9796e3239f1cd493"

st.write("Bot setup start...")

from highrise import BaseBot
class Bot(BaseBot):
    async def on_start(self, session_metadata):
        print("ONLINE!")

if st.button("RUN"):
    asyncio.run(main(["main:Bot"]))
