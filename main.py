import asyncio
import os
from highrise.__main__ import main

if __name__ == "__main__":
    # Nayi library ke liye sirf module path chahiye hota hai
    # Iska matlab hai: bot.py file ke andar MyBot class
    definitions = ["bot:MyBot"]
    
    # Render se variables uthana
    token = os.environ.get("API_TOKEN")
    room = os.environ.get("ROOM_ID")
    
    if not token or not room:
        print("Error: API_TOKEN ya ROOM_ID Render settings mein nahi mila!")
    else:
        print("Bot online aa raha hai...")
        # Direct run karna bina variables andar daale
        # Library khud environment se API_TOKEN aur ROOM_ID utha legi
        asyncio.run(main(definitions))
      
