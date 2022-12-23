from discord import ApplicationContext, Color, Embed
from discord.ext import commands
from discord.ext.commands import Cog, Context, slash_command

from bot.bot import Bot


class Shutdown(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot

    @slash_command(name="shutdown", description="Shutdown the bot.")
    @commands.is_owner()
    async def _command(self, ctx: ApplicationContext) -> None:
        await self.bot.update_server_status(False)

        embed = Embed(
            description=f"Bot is shutting down :apple:!",
            color=Color.from_rgb(47, 49, 54),
        )
        if isinstance(ctx, ApplicationContext):
            await ctx.respond(embed=embed)
        elif isinstance(ctx, Context):
            await ctx.send(embed=embed)

        await self.bot.close()


def setup(bot: Bot) -> None:
    bot.add_cog(Shutdown(bot))
