from highrise import BaseBot, WelcomeEvent

class MyBot(BaseBot):
    async def on_start(self, session_metadata):
        print("Bot is online!")

    async def on_chat(self, user, message):
        if message == "!hello":
            await self.highrise.chat(f"Hello {user.username}!")
          
