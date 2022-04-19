from ast import alias
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
import random
import os
from asyncio import sleep
import math
import discord
import asyncio
from discord import utils
from discord.utils import get
import json
import requests
import datetime

bot = discord.ext.commands.Bot(command_prefix=":")
bot.remove_command('help')

#status
@bot.event
async def on_ready():
    DiscordComponents(bot)
    print("Bot has started!")
    await bot.change_presence( status = discord.Status.idle, activity = discord.Game(':хелп'))

@bot.command()
async def майнкрафт(ctx):
    text = """
**ip: stayhome.mclan.ru**
**v: 1.16.5**
``Сервер на 2 категории, выживание и политический мир``
``На который вы сможете зайди прямо сейчас🚗``
"""
    await ctx.send(
        embed=discord.Embed(description = text, color = 0xFF0000),
            components=[
                Button(style=ButtonStyle.URL, label="сайт", url="https://sites.google.com/view/stayhome11")
            ]
        )

@bot.command()
async def инвайт(ctx):
    text = """
≪━─━─━─━─━─━─━─━─◈━─━─━─━──━─━─━─━≫
**Для использования бота вам нужно сделать роли с точными названиями как показано ниже!**
≪━─━─━─━─━─━─━─━─◈━─━─━─━──━─━─━─━≫
**Muted-** `роль, для мута, должна быть настроена под каналы!`
**»ЗАМ-АДМИН«-** `роль, которая имеет доступ к командам модерации!`
≪━─━─━─━─━─━─━─━─◈━─━─━─━──━─━─━─━≫
**・୨💖୧・invite・** https://discord.com/api/oauth2/authorize?client_id=954822415916105758&permissions=8&scope=bot
≪━─━─━─━─━─━─━─━─◈━─━─━─━──━─━─━─━≫
"""
    await ctx.send(
        embed=discord.Embed(description = text, color = 0xFF0000),
            components=[
                Button(style=ButtonStyle.URL, label="далее", url="https://discord.com/api/oauth2/authorize?client_id=950363818188505098&permissions=8&scope=bot")
            ]
        )

    responce = await bot.wait_for("button_click")
    if responce.channel == ctx.channel:
        if responce.component.label == "далее":
            await responce.respond(content="Бот №2"),
            emb = discord.Embed(description = '**coming soon...**', color = 0xFF0000)
            await ctx.send(embed = emb)
        else:
            await responce.respond(
                embed=discord.Embed(title="пожалуйста нажмите на далее", color = 0xFF0000)
            )
	

@bot.command()
async def помощь(ctx):
    await ctx.send(
        embed=discord.Embed(description = "Получить помощь от администрации", color = 0xFF0000),
            components=[
                Button(style=ButtonStyle.red, label="получить", emoji="🌹")
            ]
        )

    responce = await bot.wait_for("button_click")
    if responce.channel == ctx.channel:
        if responce.component.label == "получить":
            await responce.respond(content="Ваш канал для связи с администрацией создан! Просмотрите чуть выше, его название 0001💖"),
            await ctx.guild.create_text_channel('╭・୨💖୧・0001')
        else:
            await responce.respond(
                embed=discord.Embed(title="Не получилось связаться с администрацией!💖")
            )	
	
@bot.command()
async def плакать(ctx, member: discord.Member):
    emb = discord.Embed(description = f'{ctx.author.name} **плачет из-за** {member.name}😭', color = 0xFF0000)
    await ctx.send(embed = emb)
    await ctx.send(random.choice(['https://media2.giphy.com/media/VSvRlGiwV6ZxK/giphy.gif', 'https://c.tenor.com/FgETH4kGKRgAAAAM/rin-sad.gif', 'https://c.tenor.com/nYR1I7VED_IAAAAM/gayixiangs.gif', 'https://media2.giphy.com/media/OuKTQaitZH8Y/giphy.gif', 'https://media3.giphy.com/media/mvRwcoCJ9kGTS/giphy.gif']))
	
@bot.command()
async def обнять(ctx, member: discord.Member):
    emb = discord.Embed(description = f'{ctx.author.name} **обнимает** {member.name}💖', color = 0xFF0000)
    await ctx.send(embed = emb)
    await ctx.send(random.choice(['https://c.tenor.com/u2JORiln0sUAAAAd/hug.gif', 'https://c.tenor.com/xgVPw2QK5n8AAAAC/sakura-quest-anime.gif', 'https://c.tenor.com/lzKyZchfMzAAAAAC/anime-hug.gif', 'https://c.tenor.com/n0qIE_8B0JcAAAAC/gif-abrazo.gif', 'https://c.tenor.com/-3I0yCd6L6AAAAAC/anime-hug-anime.gif']))
	
@bot.command()
async def стесняться(ctx, member: discord.Member):
    emb = discord.Embed(description = f'{ctx.author.name} **стесняеться перед ** {member.name}😭', color = 0xFF0000)
    await ctx.send(embed = emb)
    await ctx.send(random.choice(['https://c.tenor.com/A3BsH5TMakYAAAAC/anime-shy.gif', 'https://c.tenor.com/PYOlVtPLnwoAAAAC/the-quintessential-quintuplets.gif', 'https://c.tenor.com/T51BLj_Cj8cAAAAC/blush.gif', 'https://c.tenor.com/qYS0n4QWxd4AAAAC/blush-anime.gif', 'https://c.tenor.com/d3AEjdxSfawAAAAC/anime-blush.gif']))
	
@bot.command()
async def прыгать(ctx, member: discord.Member):
    emb = discord.Embed(description = f'{ctx.author.name} **пригает перед** {member.name}😭', color = 0xFF0000)
    await ctx.send(embed = emb)
    await ctx.send(random.choice(['https://c.tenor.com/ytcXdxCBwyQAAAAd/noriko-gunbuster.gif', 'https://c.tenor.com/-s6Xm8JDtmQAAAAC/hug-jump.gif', 'https://c.tenor.com/HUZwox1jlc4AAAAd/kuchiki-rukia.gif', 'https://c.tenor.com/GQGixfnQJ84AAAAC/animes-anime.gif', 'https://c.tenor.com/mL_keJcBwCIAAAAC/fangirl-excited.gif']))	
	
@bot.command()
async def радоваться(ctx, member: discord.Member):
    emb = discord.Embed(description = f'{ctx.author.name} **радуеться из-за** {member.name}😭', color = 0xFF0000)
    await ctx.send(embed = emb)
    await ctx.send(random.choice(['https://c.tenor.com/l4Yc9wuIAwIAAAAC/anime-girl.gif', 'https://c.tenor.com/wJLU6k53L6MAAAAC/anime-yay.gif', 'https://c.tenor.com/kiw3AxGnfSgAAAAC/anime-smile-anime-cute-boy.gif', 'https://c.tenor.com/nBWlYPbKxzwAAAAC/anime-happy.gif', 'https://c.tenor.com/DVbymBMiCtoAAAAd/omg-happy.gif']))	

#pred
@bot.command()
@commands.has_any_role("»ЗАМ-АДМИН«")
async def пред(ctx, member: discord.Member, *, arg):
	author = ctx.message.author
	await member.send(f'**Предупреждение:** ``' + arg + '.``')	

#ban
@bot.command()
@commands.has_any_role("»ЗАМ-АДМИН«")
async def бан(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)

    await member.ban(reason=reason)
    await ctx.send(
        f'{ member.mention } был забанен на сервере, из-за нарушений правил!🌸')

#unban
@bot.command()
@commands.has_permissions(administrator=True)
async def разбан(ctx, *, member):
    await ctx.channel.purge(limit=1)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        await ctx.send(f'{user.mention} был разбанен на сервере🌸')
        return

#kick
@bot.command()
@commands.has_any_role("»ЗАМ-АДМИН«")
async def кик(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)

    await member.kick(reason=reason)
    await ctx.send(
        f'{ member.mention } был кикнут из сервера, из-за нарушений правил!🌸')
#mute
@bot.command()
@commands.has_any_role("»ЗАМ-АДМИН«")
async def мут(ctx,member:discord.Member):
    await ctx.channel.purge(limit = 1)
    mute = discord.utils.get(ctx.message.guild.roles,name = 'muted')
    await member.add_roles(mute)
    emb = discord.Embed(description = f'Участнику сервера { member.mention} был выдан мут!🌸', color=0xFF00FF)
    await ctx.send(embed=emb)

#unmute
@bot.command()
@commands.has_any_role("»ЗАМ-АДМИН«")
async def размут(ctx,member:discord.Member):
    await ctx.channel.purge(limit = 1)
    mute = discord.utils.get(ctx.message.guild.roles,name = 'muted')
    await member.remove_roles(mute)
    emb = discord.Embed(description = f'{ member.mention} снова может писать в чат!🌸', color=0xFF00FF)
    await ctx.send(embed=emb)
  
#say
@bot.command(aliases=['глобал'])
@commands.has_any_role("»ЗАМ-АДМИН«")
async def сай(ctx, *, text):
        emb = discord.Embed(description = text, color = 0xFF0000)
        await ctx.send(embed=emb)

#ben
@bot.command(aliases=['бен'])
async def бэн(ctx):
    emb = discord.Embed(description=random.choice(['**HO ho ho...**', '**Yes**', '**No**']),color=0xFF0000)
    emb.set_thumbnail(url='http://gameraft.ru/wp-content/uploads/2017/10/govoryashhiy-ben-177x149.jpg')
    await ctx.send(embed=emb)

#coin
@bot.command(aliases=['монетка'])
async def коин(ctx):
    emb = discord.Embed(title='🪙COIN🪙',
                        description=random.choice([
                            '**Монетка упала, и выпала РЕШКА**',
                            '**Монетка упала, и выпал ОРЁЛ**'
                        ]),
                        color=0xFF0000)
    await ctx.send(embed=emb)


#clear
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def очистка(ctx, amount=100000):
    await ctx.channel.purge(limit=amount)

#help
@bot.command()
async def хелп(ctx):
    text = """
🔧**УТИЛИТЫ**
``:инфо`` ``:инвайт`` ``:помощь`` ``майнкрафт``

⚙️**МОДЕРАЦИЯ**
``:бан`` ``:разбан`` ``:кик`` ``:мут`` ``:размут`` ``:очистка``
``:пред`` ``:сай``

🎮**ИГРЫ**
``:бен`` ``:монетка``

🌹**РП - RolePLay**
``:плакать`` ``:обнять`` ``:стесняться`` ``:прыгать`` ``:радоваться``

🔞**NSFW**
``:анал`` ``:хентай`` ``:пизда`` ``:минет`` ``:куни`` ``:конча``

"""
    emb = discord.Embed(title='🌸Команды бота:',
                        description=text,
                        color=0xFF0000)
    emb.set_thumbnail(
        url=
        'https://cdn.discordapp.com/avatars/954822415916105758/ade201c222ffe4d091ebe456f8bf01db.webp'
    )
    await ctx.send(embed=emb)

#nsfw
def fetch(url):
	s = json.loads(requests.get(url).text)
	return s["url"]

#anal
@bot.command(aliases=['анал'])
async def anal(ctx):
    if ctx.channel.is_nsfw():
        a = fetch('https://nekos.life/api/v2/img/anal')
        emb = discord.Embed(color = 0xFF0000)
        emb.set_image(url=a)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(description = '🌸Извините, это не nsfw-канал, чтоб просмотреть данную команду перейдите в <#956944736311214230> 🌸',color = 0xFF0000)
        await ctx.send(embed=emb)

#hentai
@bot.command(aliases=['хентай'])
async def hentai(ctx):
    if ctx.channel.is_nsfw():
        h1 = fetch('https://nekos.life/api/v2/img/hentai')
        h2 = fetch('https://nekos.life/api/v2/img/Random_hentai_gif')
        h = [h1, h2]
        emb = discord.Embed(color = 0xFF0000)
        emb.set_image(url=random.choice(h))
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(description = '🌸Извините, это не nsfw-канал, чтоб просмотреть данную команду перейдите в <#956944736311214230> 🌸',color = 0xFF0000)
        await ctx.send(embed=emb)

#pussy
@bot.command(aliases=['пизда', 'киска'])
async def pussy(ctx):
    if ctx.channel.is_nsfw():
        p1 = fetch('https://nekos.life/api/v2/img/pussy')
        p2 = fetch('https://nekos.life/api/v2/img/pussy_jpg')
        p = [p1, p2]
        emb = discord.Embed(color = 0xFF0000)
        emb.set_image(url=random.choice(p))
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(description = '🌸Извините, это не nsfw-канал, чтоб просмотреть данную команду перейдите в <#956944736311214230> 🌸',color = 0xFF00FF)
        await ctx.send(embed=emb)

#bj
@bot.command(aliases=['bj', 'минет'])
async def minet(ctx):
    if ctx.channel.is_nsfw():
        b = fetch('https://nekos.life/api/v2/img/bj')
        emb = discord.Embed(color = 0xFF0000)
        emb.set_image(url=b)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(description = '🌸Извините, это не nsfw-канал, чтоб просмотреть данную команду перейдите в <#956944736311214230> 🌸',color = 0xFF0000)
        await ctx.send(embed=emb)

#kuni
@bot.command(aliases=['куни'])
async def kuni(ctx):
    if ctx.channel.is_nsfw():
        c = fetch('https://nekos.life/api/v2/img/kuni')
        emb = discord.Embed(color = 0xFF0000)
        emb.set_image(url=c)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(description = '🌸Извините, это не nsfw-канал, чтоб просмотреть данную команду перейдите в <#956944736311214230> 🌸',color = 0xFF0000)
        await ctx.send(embed=emb)

#cum
@bot.command(aliases=['сперма', 'конча', 'кам'])
async def cum(ctx):
    if ctx.channel.is_nsfw():
        c = fetch('https://nekos.life/api/v2/img/cum')
        emb = discord.Embed(color = 0xFF0000)
        emb.set_image(url=c)
        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(description = '🌸Извините, это не nsfw-канал, чтоб просмотреть данную команду перейдите в <#956944736311214230> 🌸',color = 0xFF0000)
        await ctx.send(embed=emb)

class Event(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

@bot.command()
async def инфо(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    roles = [role for role in member.roles if role != ctx.guild.default_role]
    embed = discord.Embed( title = f"Информация о {member.name}💫",color = 0xFF0000)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Ник:", value=member.display_name, inline=True)
    embed.add_field(name="Все роли:", value="".join(role.mention for role in roles), inline=True)
    embed.add_field(name="Лучшая роль:", value=member.top_role.mention, inline=True)
    embed.add_field(name="Аккаунт создан:", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"), inline=True)
    embed.add_field(name="Появился на сервер:", value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"), inline=True)
    await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Event(boy))
    
bot.run('OTU0ODIyNDE1OTE2MTA1NzU4.YjYtqw.gZqw2UxSkox_JCDVSB8gvVvQ9No')
