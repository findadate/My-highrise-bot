import asyncio
import os
from highrise.__main__ import main

if __name__ == "__main__":
    room_id = os.environ.get("ROOM_ID")
    api_token = os.environ.get("API_TOKEN")
    definitions = ["bot:MyBot"]
    
    if not room_id or not api_token:
        print("Error: Variables missing!")
    else:
        asyncio.run(main(definitions, api_token, room_id))
      
