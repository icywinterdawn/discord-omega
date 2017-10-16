import discord
from discord.ext import commands

MESSAGES = {
    "scene.start":  "**A scene has started in this channel.**",
    "scene.end":    "**A scene has ended in this channel.**",
    "scene.move":   "**A scene has ended in this channel and continues in $1.**",
}

class RP:
    """RP related commands."""
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def scene(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid scene command passed...')

    @scene.command(pass_context=True, no_pm=True)
    async def start(self, ctx):
        await self.bot.delete_message(ctx.message)
        await self.bot.say(MESSAGES["scene.start"])

    @scene.command(pass_context=True, no_pm=True)
    async def end(self, ctx):
        await self.bot.delete_message(ctx.message)
        await self.bot.say(MESSAGES["scene.end"])

    @scene.command(pass_context=True, no_pm=True)
    async def move(self, ctx, channel: discord.Channel):
        await self.bot.delete_message(ctx.message)
        await self.bot.say(MESSAGES["scene.move"].replace('$1', channel.mention))
