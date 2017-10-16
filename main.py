#!/usr/bin/env python3
import os
import asyncio
import discord
from discord.ext import commands
from music import Music
from rp import RP

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'),
                   description='Omega is a friendly Borg cube.')


@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))


def main():
    # Configure the client with the Discord token in the environment.
    token = os.environ["DISCORD_TOKEN"]

    register_features()

    bot.run(token)


def register_features():
    # Music player
    bot.add_cog(Music(bot))
    # RP
    bot.add_cog(RP(bot))


if __name__ == "__main__":
    main()
