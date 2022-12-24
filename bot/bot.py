from discord.ext import commands
from discord.ext.commands import Cog

from pathlib import Path
from time import time


class Bot(commands.Bot):
    def __init__(self, command_prefix=..., help_command=..., **options):
        super().__init__(command_prefix, help_command, **options)
        self.load_extensions()
        self.uptime = round(time())

    @Cog.listener()
    async def on_ready(self) -> None:
        print(f"{self.user} ready!")

        status_updated = await self.update_server_status(True)
        if status_updated:
            print("Discord server status channel updated.")
        else:
            print("Failed to update discord server status channel")

    def load_extensions(self, names: list = None) -> None:
        """Load extensions from the bot

        Parameters
        -----------
        name: :class: 'list'
            The list of names of extensions that need to be loaded, None = all.
        """

        path = Path("bot/exts/")
        errors = []
        for extension in path.glob("**/*.py"):
            extension = str(extension).replace("/", ".")[:-3]
            if names and extension not in names:
                continue
            try:
                self.load_extension(extension, store=False)
            except Exception as e:
                errors.append(e)
        print(errors)
        return errors

    def reload_extensions(self, names: list = None) -> None:
        """Reload extensions from the bot

        Parameters
        -----------
        name: :class: 'list'
            The list of names of extensions that need to be reloaded, None = all.
        """

        path = Path("bot/exts/")
        errors = []
        for extension in path.glob("**/*.py"):
            extension = str(extension).replace("/", ".")[:-3]
            if names and extension not in names:
                continue
            try:
                self.reload_extension(extension)
            except Exception as e:
                errors.append(e)
        print(errors)
        return errors

    def unload_extensions(self, names: list = None) -> None:
        """Unload extensions from the bot

        Parameters
        -----------
        name: :class: 'list'
            The list of names of extensions that need to be unloaded, None = all.
        """

        path = Path("bot/exts/")
        errors = []
        for extension in path.glob("**/*.py"):
            extension = str(extension).replace("/", ".")[:-3]
            if names and extension not in names:
                continue
            try:
                self.unload_extension(extension)
            except Exception as e:
                errors.append(e)
        print(errors)
        return errors

    async def update_server_status(self, status: bool = True) -> bool:
        """Change name of status channel in discord server

        Parameters
        -----------
        status: :class: 'bool'
            The status of bot, True for online and False for offline.
        """

        status_channel = self.get_channel(
            self.CONSTANTS["CHANNEL_CONSTANTS"]["STATUS_CHANNEL"]
        )

        if status and status_channel:
            await status_channel.edit(name="🍏 Online")
        else:
            await status_channel.edit(name="🍎 Offline")

        return True
