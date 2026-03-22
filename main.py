import asyncio
import os
from highrise.__main__ import main
from bot import MyBot  # Humne yahan direct bot ko import kiya hai

if __name__ == "__main__":
    # Bot definition ko object ke roop mein dena
    class BotDefinition:
        def __init__(self, bot_class, room_id, api_token):
            self.bot_class = bot_class
            self.room_id = room_id
            self.api_token = api_token

    room_id = os.environ.get("ROOM_ID")
    api_token = os.environ.get("API_TOKEN")
    
    if not room_id or not api_token:
        print("Error: API_TOKEN ya ROOM_ID missing hai!")
    else:
        # Naya structure jo library ko chahiye
        definitions = [BotDefinition(MyBot, room_id, api_token)]
        print("Bot online aa raha hai...")
        asyncio.run(main(definitions))
      
