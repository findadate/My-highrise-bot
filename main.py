import asyncio
import os
import sys

# pkg_resources error ko bypass karne ke liye
try:
    import setuptools
except ImportError:
    pass

from highrise.__main__ import main

if __name__ == "__main__":
    token = os.environ.get("API_TOKEN")
    room = os.environ.get("ROOM_ID")
    definitions = ["bot:MyBot"]
    
    if not token or not room:
        print("Error: Variables not found!")
        sys.exit(1)
    
    asyncio.run(main(definitions, token, room))
  
