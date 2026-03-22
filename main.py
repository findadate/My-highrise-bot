import asyncio
import os
from highrise.__main__ import main

if __name__ == "__main__":
    # Bot ki location (bot.py file mein MyBot class)
    definitions = [
        "bot:MyBot", 
    ]
    
    # Environment variables check karne ke liye (sirf confirmation ke liye)
    token = os.environ.get("API_TOKEN")
    room = os.environ.get("ROOM_ID")
    
    if not token or not room:
        print("Error: API_TOKEN ya ROOM_ID nahi mila!")
    else:
        print("Bot start ho raha hai...")
        # Nayi library ke mutabiq sirf definitions bhejna hai
        asyncio.run(main(definitions))
      
