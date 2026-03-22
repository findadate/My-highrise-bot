import streamlit as st
import asyncio
import os
import threading
from highrise.__main__ import main

st.title("🤖 Highrise Bot Dashboard")

# Bot ko alag thread mein chalane ka function
def start_bot_thread():
    definitions = ["bot:MyBot"]
    # Naya event loop banana zaroori hai
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main(definitions))
    except Exception as e:
        print(f"Bot Error: {e}")

# Streamlit UI
if "bot_started" not in st.session_state:
    st.session_state.bot_started = False

if st.button("Start Bot") or not st.session_state.bot_started:
    thread = threading.Thread(target=start_bot_thread, daemon=True)
    thread.start()
    st.session_state.bot_started = True
    st.success("Bot process initiated in background!")

st.info("Check your Highrise room to see if the bot is online.")
