import disnake
from disnake.ext import commands
from forms import arrest_form
from buttons import self_role
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Бот запущен как {bot.user}')

@bot.slash_command(name="arrest", description="Заполните бланк ареста.")
async def tags(inter: disnake.AppCmdInter):
    modal = arrest_form.ArrestModal()
    await inter.response.send_modal(modal=modal)


bot.load_extension('buttons.self_role')
bot.run(bot_token)