from discord.ext import commands

from Bot.models import Champion
from Bot.winrate_fetcher import WinrateFetcher

from Config.config import OWNER_ID

class WinrateCog(commands.Cog):
    def __init__(self, bot: commands.Bot, winrate_fetcher: WinrateFetcher):
        self.bot = bot
        self.winrate_fetcher = winrate_fetcher
        
    @commands.command(aliases=['winrate'])
    async def wr(self, ctx: commands.Context, champion_name: str, *args: str) -> None:
        champ = Champion(name=champion_name)
        result = self.winrate_fetcher.get_stats(champ, args)
        
        if not result.win_rate:
            await ctx.send(f"Oh no! Seems like Gwen ran into some issues whilst fetching the winrate! <@{OWNER_ID}>")
            return
        
        if result.champ.role:
            if result.champ.elo:
                await ctx.send(f"{result.champ.name} has a {result.win_rate} winrate in {result.champ.elo} in {result.champ.role}{result.final_string}.")
                return
            
            await ctx.send(f"{result.champ.name} has a {result.win_rate} winrate in {result.champ.role}{result.final_string}.")
            return
        
        await ctx.send(f"{result.champ.name} has a {result.win_rate} winrate{result.final_string}.")