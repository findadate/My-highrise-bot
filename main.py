import streamlit as st
import asyncio
import threading
import os
from highrise.__main__ import main

st.title("🤖 Highrise Bot Dashboard")

def start_bot_thread(token, room):
    # Secrets ko environment variables mein set karna zaroori hai
    os.environ["API_TOKEN"] = token
    os.environ["ROOM_ID"] = room
    
    definitions = ["bot:MyBot"]
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main(definitions))
    except Exception as e:
        print(f"Bot Error: {e}")

# Streamlit secrets se data uthana
if "API_TOKEN" in st.secrets and "ROOM_ID" in st.secrets:
    token = st.secrets["API_TOKEN"]
    room = st.secrets["ROOM_ID"]
    
    if "bot_started" not in st.session_state:
        st.info("Connecting to Highrise room...")
        thread = threading.Thread(target=start_bot_thread, args=(token, room), daemon=True)
        thread.start()
        st.session_state.bot_started = True
        st.success("Bot process initiated! Check your room.")
else:
    st.error("Secrets missing! Please add API_TOKEN and ROOM_ID in Advanced Settings.")

st.write("Logs checking ke liye niche 'Manage app' par click karein.")
