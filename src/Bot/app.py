import discord

from discord.ext import commands

from logger import SingletonLogger
from Database.database import DatabaseHandler
from Config.config import (OWNER_ID, PREFIX,)

class App(commands.Bot):
    """
        Used to run all discord-related commands, such as sending or fetching messages.
    """
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = super().__init__(command_prefix=PREFIX, intents=intents, help_command=None, owner_id=OWNER_ID)
        
        self.logger = SingletonLogger().get_logger()
        self.database = DatabaseHandler()

    async def setup_hook(self) -> None:
        from Bot.Cogs.deepseek_cog import DeepseekCog
        
        self.logger.info("Initialising cogs.")
        await self.add_cog(DeepseekCog(bot=self, database=self.database, logger=self.logger))
        self.logger.info("Finished initialising cogs.")

        self.database.create_db()
        self.logger.info("Database created.")
            
        
                
        
        
                
                
        