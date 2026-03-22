from highrise import BaseBot

class MyBot(BaseBot):
    async def on_start(self, session_metadata):
        print("Bot is online and ready!")

    async def on_chat(self, user, message):
        if message.lower() == "!hello":
            await self.highrise.chat(f"Hello {user.username}!")
          
