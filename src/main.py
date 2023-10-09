import discord, config, random, json
import interactions
from discord.ext import commands, tasks
from discord.ui import Button, View
from discord.utils import get


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.event
async def on_ready():
	print("ready")



@bot.slash_command(description="-")
async def delay(ctx, delay: int = None):
    if not ctx.author.guild_permissions.manage_messages:
        embedVar = discord.Embed(title="Ошибка", description="<:776404508515368972:1045282924905381938> Данная команда недоступна вам.", color=0xF54236)
        await ctx.respond(embed=embedVar, ephemeral=True)

    else:

        if(delay == None):
            embedVar = discord.Embed(title='Команда "/dealy"', description="**Установить задержку на удаление вызваемых эмоций**\n\n**Использование:**\n`/dealy [краткость]`\n├ Время для задержки можно установить в минутах.\n└ Укажите 0 если не хотите удалять сообщение.\n\n**Пример:**\n`/dealy 5`\n┗ Установлена задержка на удаление в пять минут.", color=0x28292c)
            await ctx.respond(embed=embedVar, ephemeral=True)
        else:
            if(delay > 20):
                embedVar = discord.Embed(title="Ошибка", description="<:776404508515368972:1045282924905381938> Максимальное количество минут: 20!", color=0xF54236)
                await ctx.respond(embed=embedVar, ephemeral=True)
            elif(delay == 0):
                embedVar = discord.Embed(title="Успешно!", description=f"<:776404508564914187:1045282922946646029>  Задержка убрана!", color=0x429E4C)
                await ctx.respond(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Успешно!", description=f"<:776404508564914187:1045282922946646029>  Задержка установлина на {delay} минут!", color=0x429E4C)
                await ctx.respond(embed=embedVar)


@bot.slash_command(description="-")
async def help(ctx):
    if not ctx.author.guild_permissions.manage_messages:
        embedVar = discord.Embed(title="Добро пожаловать в помощь бота View", description="> Доступные команды бота:", color=0x28292c)
        embedVar.add_field(name="** **", value="• `/есть`\n• `/петь`\n• `/пить`\n• `/обнять`\n• `/укусить`\n• `/лизнуть`\n• `/злиться`\n• `/тыкнуть`", inline=True)
        embedVar.add_field(name="** **", value="• `/плакать`\n• `/ударить`\n• `/смеяться`\n• `/похлопать`\n• `/наблюдать`\n• `/прижаться`\n• `/поцеловать`\n• `/пощекотать`", inline=True)
        embedVar.add_field(name="** **", value="• `/плакать`\n• `/ударить`\n• `/смеяться`\n• `/похлопать`\n• `/наблюдать`\n• `/прижаться`\n• `/поцеловать`\n• `/пощекотать`", inline=True)
        await ctx.respond(embed=embedVar, ephemeral=True)
    else:
        embedVar = discord.Embed(title="Добро пожаловать в помощь бота View", description="> Доступные команды бота:", color=0x28292c)
        embedVar.add_field(name="** **", value="• `/есть`\n• `/петь`\n• `/пить`\n• `/обнять`\n• `/укусить`\n• `/лизнуть`\n• `/злиться`\n• `/тыкнуть`", inline=True)
        embedVar.add_field(name="** **", value="• `/плакать`\n• `/ударить`\n• `/смеяться`\n• `/похлопать`\n• `/наблюдать`\n• `/прижаться`\n• `/поцеловать`\n• `/пощекотать`", inline=True)
        embedVar.add_field(name="** **", value="• `/плакать`\n• `/ударить`\n• `/смеяться`\n• `/похлопать`\n• `/наблюдать`\n• `/прижаться`\n• `/поцеловать`\n• `/пощекотать`", inline=True)
        embedVar.set_image(url="https://i.postimg.cc/3RrZDHjV/line.png")
        embedVar.set_footer(text='Установленная задежка на удаление: 3 минуты.', icon_url='https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif')
        await ctx.respond(embed=embedVar, ephemeral=True)


@bot.slash_command(description="-")
async def обнять(ctx, member: discord.Member = None):
    user = member

    if(user != None):
        descr, gif = random.choice(list(config.hug.items()))
        user_id = user.id
    else:
        descr, gif = random.choice(list(config.hug_error.items()))
        user_id = ""


    embedVar = discord.Embed(title="", description=descr.replace("{user}", str(user_id)).replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def кушать(ctx):
    descr, gif = random.choice(list(config.eat.items()))
    embedVar = discord.Embed(title="", description=descr.replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def лизнуть(ctx, member: discord.Member):
    user = member

    descr, gif = random.choice(list(config.lick.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{user}", str(user.id)).replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def укусить(ctx, member: discord.Member):
    user = member

    descr, gif = random.choice(list(config.bite.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{user}", str(user.id)).replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def петь(ctx):

    descr, gif = random.choice(list(config.sing.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def злится(ctx):

    descr, gif = random.choice(list(config.agry.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def пить(ctx):

    descr, gif = random.choice(list(config.drink.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def тыкнуть(ctx, member: discord.Member):
    user = member

    descr, gif = random.choice(list(config.poke.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{user}", str(user.id)).replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def плакать(ctx):

    descr, gif = random.choice(list(config.cry.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def похлопать(ctx, member: discord.Member):
    user = member

    descr, gif = random.choice(list(config.pat.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{user}", str(user.id)).replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def ударить(ctx, member: discord.Member):
    user = member

    descr, gif = random.choice(list(config.punch.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{user}", str(user.id)).replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)



@bot.slash_command(description="-")
async def поцеловать(ctx, member: discord.Member):
    user = member

    descr, gif = random.choice(list(config.kiss.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{user}", str(user.id)).replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def наблюдать(ctx, member: discord.Member = None):
    user = member

    if(user != None):
        descr, gif = random.choice(list(config.stare.items()))
        user_id = user.id
    else:
        descr, gif = random.choice(list(config.stare_error.items()))
        user_id = ""

    embedVar = discord.Embed(title="", description=descr.replace("{user}", str(user_id)).replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def пощекотать(ctx, member: discord.Member):
    user = member

    descr, gif = random.choice(list(config.tickle.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{user}", str(user.id)).replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def смеяться(ctx, member: discord.Member = None):
    user = member

    if(user != None):
        descr, gif = random.choice(list(config.laugh.items()))
        user_id = user.id
    else:
        descr, gif = random.choice(list(config.laugh_error.items()))
        user_id = ""

    embedVar = discord.Embed(title="", description=descr.replace("{user}", str(user_id)).replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)


@bot.slash_command(description="-")
async def прижатся(ctx, member: discord.Member):
    user = member

    descr, gif = random.choice(list(config.cuddle.items()))

    embedVar = discord.Embed(title="", description=descr.replace("{user}", str(user.id)).replace("{author}", str(ctx.author.id)))
    embedVar.set_image(url=gif)

    embedVar.set_footer(text='Сообщение автоматически будет удалено через 10 минут . . .',icon_url="https://media.discordapp.net/attachments/889825724616290305/889825771772854303/ezgif-7-29dff6d7a47f.gif")
    await ctx.respond(embed=embedVar, delete_after=600.0)

bot.run(config.token)
