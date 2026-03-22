import asyncio
import os
from highrise.__main__ import main

if __name__ == "__main__":
    # Render ke environment variables se data uthana
    room_id = os.environ.get("ROOM_ID")
    api_token = os.environ.get("API_TOKEN")
    
    # Bot ki location (bot.py file mein MyBot class)
    definitions = [
        "bot:MyBot", 
    ]
    
    if not room_id or not api_token:
        print("Error: API_TOKEN ya ROOM_ID nahi mila!")
    else:
        print("Bot online aa raha hai...")
        # Bot ko sahi variables ke saath run karna
        asyncio.run(main(definitions, api_token, room_id))
      
