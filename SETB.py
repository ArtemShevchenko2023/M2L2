import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='^', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'*Привет! Я экологический бот! Меня зовут {bot.user}!*')
@bot.command()
async def info(ctx):
    infa = ("Я бот для экологии! Создан для подростковой целевой аудитории. Подсказываю как помочь экологии в современном мире. Все мои команды начинаются со знака ^. Например eco hello.")
    await ctx.send(f"*{infa}*")
@bot.command()
async def material(ctx):
    await ctx.send("*Некоторые материалы разлагаются 2 недели - например пищевые и бумажные отходы, но другие от 1-2 миллионов лет - например стекло и батарейки. Во избежание этого надо сдавать материалы на переработку, если нельзя сдать материал то используйте его повторно!*")
@bot.command()
async def youcan(ctx):
    can = random.randint(1, 3)
    if can == 1:
        await ctx.send("*Например ты можешь стать волонтёром для экологии или же просто сходить разочек на экологические работы!*")
    if can == 2:
        await ctx.send("*Можешь бросать мусор в урну! Если тебе скажут что это кринжово: не обращай внимания! Экология важнее мнения других людей!*")
    if can == 3:
        await ctx.send("*Можешь поделиться мной с твоими друзьями! Они смогут узнать об экологии чуть-чуть больше и решить: будут ли они заботиться об экологии или нет. Ссылка для распостранения: https://discord.com/api/oauth2/authorize?client_id=1104363361254256700&permissions=8&scope=bot *")
@bot.command()
async def stat(ctx):
    await ctx.send("*В России ко 2 половине 2010-х накоплено 30 млрд тонн мусора! Но сейчас уже начали понимать глобальную проблему мусора и разрабатывается решение!*")
@bot.command()
async def helpe(ctx):
    helping = ("^hello\n^info\n^material\n^youcan\n^stat\n^helpe")
    await ctx.send(f"*Мои команды:\n{helping}*")

bot.run("")