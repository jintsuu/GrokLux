from discord.ext import commands

from Database.database import DatabaseHandler

class OwnerCog(commands.Cog):
    def __init__(self, bot: commands.Bot, database: DatabaseHandler):
        self.bot = bot
        self.database = database
        
    #  These 2 commands make it so that the owner of the bot can always add and remove users from the blacklist.
    @commands.command()
    @commands.is_owner()
    async def fuckyou(self, ctx: commands.Context, id) -> None:
        """Alternative to +blacklist. Instead of permissions this requires the sender to be the owner of the bot.
        Change OWNER_ID in Config.config to your ID."""
        
        if ctx.guild is None:
            await ctx.send('Command must be used in a server.')
            return
        
        try:
            id = int(id)
        except ValueError:
            if len(ctx.message.mentions) == 0:
                await ctx.send('Invalid id...', ephemeral=True)
                return
            
            id = ctx.message.mentions[0].id

        if self.database.fetch_blacklist(id, ctx.guild.id):
            await ctx.send('User is already blacklisted.')
            return
        
        self.database.add_to_blacklist(id, ctx.guild.id)
        self.database.remove_from_gwen_sub(id, ctx.guild.id)
        
        await ctx.send('User added to the Blacklist.')
        
    @commands.command()
    @commands.is_owner()
    async def unfuckyou(self, ctx: commands.Context, user_id) -> None:
        """Alternative to +blremove. Instead of permissions this requires the sender to be the owner of the bot.
        Change OWNER_ID in Config.config to your ID."""
        
        if ctx.guild is None:
            await ctx.send('Command must be used in a server.')
            return
            
        try:
            user_id = int(user_id)
        except ValueError:
            if len(ctx.message.mentions) == 0:
                await ctx.send('Invalid id...', ephemeral=True)
                return

            user_id = ctx.message.mentions[0].id

        if not self.database.fetch_blacklist(user_id, ctx.guild.id):
            await ctx.send('User is not Blacklisted.')
            return
        
        self.database.remove_from_blacklist(user_id, ctx.guild.id)
        await ctx.send('User removed from the Blacklist.')
        
    @commands.command()
    @commands.is_owner()
    async def fuckyouremove(self, ctx: commands.Context, user_id) -> None:
        """Removes a person from GwenSubs. Only usable by Owner."""
        
        if ctx.guild is None:
            await ctx.send('Command must be used in a server.')
            return
            
        try:
            user_id = int(user_id)
        except ValueError:
            if len(ctx.message.mentions) == 0:
                await ctx.send('Invalid id...', ephemeral=True)
                return
            
            user_id = ctx.message.mentions[0].id
        
        if not self.database.fetch_gwen_sub(user_id, ctx.guild.id):
            await ctx.send('User is not subscribed to GwenBot.')
            return
        
        self.database.remove_from_gwen_sub(user_id, ctx.guild.id)
        await ctx.send('User removed from GwenBot subscription.')
        
    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx: commands.Context) -> None:
        await ctx.send("Shutting down!")
        
        await self.bot.close()    
        
    @commands.command()
    @commands.is_owner()
    async def set_questions(self, ctx: commands.Context, amount: int) -> None:
        await ctx.send(f"Setting amount to {amount}.")
        self.database.set_amount(amount)
    
    @set_questions.error
    @unfuckyou.error
    @fuckyou.error
    @fuckyouremove.error
    @shutdown.error
    async def _not_owner(self, ctx: commands.Context, error: Exception) -> None:
        if isinstance(error, commands.CheckFailure):
            await ctx.send('Who do you think you are...')