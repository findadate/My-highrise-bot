import sys
# Sabse pehle pkg_resources ka error theek karne ke liye:
try:
    import setuptools.archive_util
except ImportError:
    import os
    # Ye line error ko rokne ke liye "dummy" resources banati hai
    sys.modules['pkg_resources'] = type('module', (), {'get_distribution': lambda x: None})

import asyncio
import os
from highrise.__main__ import main

if __name__ == "__main__":
    # Bot definition jo naye version ke liye zaroori hai
    definitions = ["bot:MyBot"]
    
    token = os.environ.get("API_TOKEN")
    room = os.environ.get("ROOM_ID")
    
    if not token or not room:
        print("Variables missing in Render settings!")
    else:
        print("Bot start ho raha hai...")
        # Render ke environment se library khud token uthayegi
        asyncio.run(main(definitions))
      
