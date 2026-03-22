from highrise import BaseBot, User, Position

class MyBot(BaseBot):
    async def on_chat(self, user: User, message: str) -> None:
        if message.lower().startswith("!hello"):
            await self.highrise.chat(f"Namaste {user.username}! 🙏")
        if message.lower() == "!dance":
            await self.highrise.send_emote("dance-tiktok8", user.id)
          
