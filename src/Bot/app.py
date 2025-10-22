import discord

from discord.ext import commands

from logger import SingletonLogger
from Database.database import DatabaseHandler
from Config.config import (OWNER_ID, PREFIX,)
from Bot.winrate_fetcher import WinrateFetcher

class App(commands.Bot):
    """
        Used to run all discord-related commands, such as sending or fetching messages.
    """
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None, owner_id=OWNER_ID)
        
        self.logger = SingletonLogger().get_logger()
        self.database = DatabaseHandler()
        self.winrate_fetcher = WinrateFetcher()
    
    async def setup_hook(self) -> None:
        from Bot.Cogs.listener_cog import ListenerCog
        from Bot.Cogs.gwensub_cog import GwensubCog
        from Bot.Cogs.owner_cog import OwnerCog
        from Bot.Cogs.winrate_cog import WinrateCog
        from Bot.Cogs.dm_cog import DMCog
        from Bot.Cogs.commands_cog import CommandsCog
        from Bot.Cogs.leaderboard_cog import LeaderboardCog
        
        self.logger.info("Initialising cogs.")
        await self.bot.add_cog(ListenerCog(self.bot, self.database, self.logger))
        await self.bot.add_cog(GwensubCog(self.bot, self.database, self.logger))
        await self.bot.add_cog(OwnerCog(self.bot, self.database, self.logger))
        await self.bot.add_cog(WinrateCog(self.bot, self.winrate_fetcher, self.logger))
        await self.bot.add_cog(DMCog(self.bot, self.winrate_fetcher))
        await self.bot.add_cog(CommandsCog(self.bot))
        await self.bot.add_cog(LeaderboardCog(self.bot, self.database))
        self.logger.info("Finished initialising cogs.")
            
        
                
        
        
                
                
        