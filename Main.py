import asyncio
import os
from highrise.__main__ import main, BotDefinition
from bot import MyBot

if __name__ == "__main__":
    room_id = os.environ.get("ROOM_ID")
    api_token = os.environ.get("API_TOKEN")
    definitions = [BotDefinition(MyBot(), room_id, api_token)]
    asyncio.run(main(definitions))
  
