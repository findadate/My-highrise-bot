import asyncio
import os
from highrise.__main__ import main

if __name__ == "__main__":
    definitions = ["bot:MyBot"]
    
    # Render variables apne aap utha lega
    token = os.environ.get("API_TOKEN")
    room = os.environ.get("ROOM_ID")
    
    if not token or not room:
        print("Variables missing in Render settings!")
    else:
        # Is version mein sirf definitions pass karni hoti hain
        # Token aur Room ID environment variables se library khud leti hai
        asyncio.run(main(definitions))
      
