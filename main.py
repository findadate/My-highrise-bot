import streamlit as st
import asyncio
import os
from highrise.__main__ import main

st.title("Highrise Bot Dashboard")
st.write("Bot is running...")

async def run_bot():
    definitions = ["bot:MyBot"]
    # Streamlit ke secrets se token uthayega
    await main(definitions)

if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except Exception as e:
        st.error(f"Error: {e}")
      
