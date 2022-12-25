from discord import ApplicationContext, Color, Embed
from discord.ext.commands import Cog, Context, slash_command

from bot.bot import Bot
from bot.constants import EMOJI


class Ping(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot

    @slash_command(name="ping", description="Get latency of bot.")
    async def _command(self, ctx: ApplicationContext) -> None:
        latency = round(self.bot.latency * 1000)

        embed = Embed(
            description=f"**Pong**! {latency}ms {EMOJI.LATENCY}",
            color=Color.from_rgb(47, 49, 54),
        )

        if isinstance(ctx, ApplicationContext):
            await ctx.respond(embed=embed)
        elif isinstance(ctx, Context):
            await ctx.send(embed=embed)


def setup(bot: Bot) -> None:
    bot.add_cog(Ping(bot))
