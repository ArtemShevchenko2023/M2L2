import discord
from discord.ext import commands
from SETLogic import *
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
    infa = ("Я один из ЭКО ботов! Создан для подростковой целевой аудитории. Подсказываю как помочь экологии в современном мире. Все мои команды начинаются со знака ^. Например ^hello.")
    await ctx.send(f'*{infa}*')
@bot.command()
async def material(ctx):
    await ctx.send("*Некоторые материалы разлагаются 2 недели - например пищевые и бумажные отходы, но другие от 1-2 миллионов лет - например стекло и батарейки. Во избежание этого надо сдавать материалы на переработку, если нельзя сдать материал то используйте его повторно!*")
@bot.command()
async def youcan(ctx):
    await ctx.send(f'{canyou()}')
@bot.command()
async def stat(ctx):
    await ctx.send("*В России ко 2 половине 2010-х было накоплено 30 млрд тонн мусора! Но сейчас уже начали понимать эту проблему и разрабатывать решение. Ты тоже можешь помочь экологии, а я и Интернет подскажем как и зачем.*")
@bot.command()
async def helpe(ctx):
    helping = ("Приветствие: ^hello\nИнформация с маленькой интсрукцией обо мне: ^info\nО переработке материалов: ^material\nО том как ты можешь помочь экологии: ^youcan\nКоличество тонн мусора в России: ^stat\nМои команды: ^helpe\nЭкология на дороге: ^road")
    await ctx.send(f'*Мои команды:\n{helping}*')
@bot.command()
async def road(ctx):
    await ctx.send(f'{inroad()}')

bot.run("Секретный токен")
