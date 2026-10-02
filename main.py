import os
import discord
import logging
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

@bot.event
async def setup_hook() -> None:
    synced = await bot.tree.sync()
    print(f"Zsynchronizowano {len(synced)} slash commands.")

@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user}")



@bot.tree.command(name="mikoshi", description="Tells which user called the command.")
async def mikoshi(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(interaction.user.mention)

bot.run(TOKEN, log_handler=handler)
