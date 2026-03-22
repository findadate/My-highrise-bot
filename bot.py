from highrise import BaseBot, User, Position

class MyBot(BaseBot):
    async def on_chat(self, user: User, message: str) -> None:
        if message.lower().startswith("!hello"):
            await self.highrise.chat(f"Namaste {user.username}! Main aapka Highrise bot hoon.")
        
        if message.lower() == "!dance":
            # Bot dance karega
            await self.highrise.send_emote("dance-tiktok8")

    async def on_user_join(self, user: User, position: Position) -> None:
        # Jab koi room join karega toh bot welcome karega
        await self.highrise.chat(f"Welcome to the room dear🥀, {user.username}!")
      
