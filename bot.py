import discord
from discord.ext import commands
import asyncio
import shutil
import os

from comandos import (
    iniciar_banco,
    TicketView
)

TOKEN = "SEU_TOKEN_AQUI"  # ⚠️ Troque pelo seu TOKEN real

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)


# ------------------------------
# Eventos principais
# ------------------------------
@bot.event
async def on_ready():
    iniciar_banco()
    bot.add_view(TicketView())
    print(f"✅ Bot online como {bot.user}")

@bot.event
async def on_disconnect():
    try:
        shutil.copy("coins.db", "coins_backup.db")
        print("🔄 Backup salvo em coins_backup.db")
    except Exception as e:
        print(f"Erro ao salvar backup: {e}")


# ------------------------------
# Importa comandos
# ------------------------------
import comandos


# ------------------------------
# Iniciar Bot
# ------------------------------
bot.run(TOKEN)
