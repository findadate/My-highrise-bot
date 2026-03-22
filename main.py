import asyncio
import os
from highrise.__main__ import main
from bot import MyBot

class BotDefinition:
    def __init__(self, bot_class, room_id, api_token):
        self.bot_class = bot_class
        self.room_id = room_id
        self.api_token = api_token

if __name__ == "__main__":
    # Railway se Token aur Room ID uthana
    room_id = os.environ.get("ROOM_ID")
    api_token = os.environ.get("API_TOKEN")
    
    if not room_id or not api_token:
        print("Error: ROOM_ID ya API_TOKEN nahi mila!")
    else:
        definitions = [BotDefinition(MyBot, room_id, api_token)]
        asyncio.run(main(definitions))
      
