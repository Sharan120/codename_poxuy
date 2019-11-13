import discord
import random
import json
import os
import sys
from itertools import cycle
from discord.ext import commands, tasks
import asyncio
import ast
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import datetime, time
TOKEN = 'NjM3MDA5OTEyNTg4OTI3MDE3.Xch75Q.KpvCq1SeCNOQssY3JLuv_nWlA44'
bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

status = cycle(['Сделано Sharan\'ом', 'В разработке!', 'Сделано на discord.py!'])
@bot.event
async def on_ready():
    change_status.start()
    await bot.change_presence(status=discord.Status.online)  #("Бот включен! Для просмотра комманд напишите !help 😳")
    print("Бот запущен! тыблядьлох говнокод сделалъ")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embederror = discord.Embed(
            title = '⚠ Ошибка!',
            description = 'Не были введены нужные аргументы!',
            colour = discord.Colour.red()
        )

        embederror.set_footer(text='тоесть вы не ввели текст в комманду')

        await ctx.send(embed=embederror)

    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        embederrorperm = discord.Embed(
            title = '⚠ Ошибка!',
            description = 'У вас нету прав на использования этой комманды!',
            colour = discord.Colour.red()
        )
        embederrorperm.set_footer(text='извини, я немогу предать своих юзеров.')

        await ctx.send(embed=embederrorperm)        

@bot.command()  # разрешаем передавать агрументы
async def hack(ctx, arg):
    "Херня а не комманда если честно. "
    embed = discord.Embed(
        title = 'HACKERMAN СНОВА В ДЕЛЕ!!!!',
        description = f'Взлом {arg}!',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='а теперь спи спокойно >:D')

    await ctx.send(embed=embed)
@bot.command()
async def pis(ctx):
    "???? "
    embd = discord.Embed(
        title = '😳😳😳😳',
        description = 'pispispis' + 'pispispis',
        colour = discord.Colour.blue()
    )

    embd.set_footer(text='pis')

    await ctx.send(embed=embd)

def is_is_me(ctx):
    return ctx.author.id == 221608240713039872

@bot.command()
async def ping(ctx):
    "Измеряет задержку! "
    eembeardd = discord.Embed(
        title = 'Отбил падла! 🏓',
        description = f'Задержка составляет: {round(bot.latency * 1000)}ms',
        colour = discord.Colour.gold()
    )

    eembeardd.set_footer(text='автор долбаеб')

    await ctx.send(embed=eembeardd)

@bot.command(name="8ball")
async def _8ball(ctx, *, question):
    "Магический шар. "
    responses = [
        'Возможно',
        'Нет',
        'Скорее всего да.',
        'Наверное да?',
        'Скорее всего нет.',
        'Даже не надейся.',
        'Даже не знаю...',
        'Да, точно да!',
        'Наверное нет?',
        'Мои источники говорят нет.',
        'Мои источники говорят да!',
        'Очень странно, попробуй еще раз.',
        'Нуууууу, дааа???',
        'Эм?.......',
        'Попробуй еще раз позже.',
        'Да, 100%!'

    ]

    embeeeeeeed = discord.Embed(
        title = '🎱 Ииииии?',
        description = f'Вопрос: {question}\nОтвет: {random.choice(responses)}',
        colour = discord.Colour.light_grey()
    )

    embeeeeeeed.set_footer(text='Вот это я даю, да?')

    await ctx.send(embed=embeeeeeeed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, arg):
    "Удаления сообщений. "
    await ctx.channel.purge(limit=int(arg))

    embeeeeeeeaeaeeed = discord.Embed(
        title = '✅ Готово!',
        description = f'Было удалено {arg} сообщений!',
        colour = discord.Colour.gold()
    )

    embeeeeeeeaeaeeed.set_footer(text=f'{arg} сообщений карл!')

    msg = await ctx.send(embed=embeeeeeeeaeaeeed)
    await msg.delete(delay=5)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    "Выгоняет участника из сервера. "
    await member.kick(reason=reason)

    embasdasdaeaeeed = discord.Embed(
        title = '✅ Готово!',
        description = f'{member} был только что кикнут!',
        colour = discord.Colour.red()
    )

    embasdasdaeaeeed.set_footer(text=f'{member} ты нитуда полез. ну зачем?')

    await ctx.send(embed=embasdasdaeaeeed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    "Мощный инструмент! "
    await member.ban(reason=reason)

    embadsdseaeeed = discord.Embed(
        title = '✅ Готово!',
        description = f'{member} был только что забанен!',
        colour = discord.Colour.red()
    )

    embadsdseaeeed.set_footer(text=f'{member} ты нитуда полез. ну зачем?')

    embadsdseaeeed.set_author(name=member, )

    await ctx.send(embed=embadsdseaeeed)

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


@bot.command()
@commands.check(is_is_me)
async def eval_fn(ctx, *, cmd):
    "Evalutes input. "    

    fn_name = "_eval_expr"

    cmd = cmd.strip("` ")

    # add a layer of indentation
    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

    # wrap in async def body
    body = f"async def {fn_name}():\n{cmd}"

    parsed = ast.parse(body)
    body = parsed.body[0].body

    insert_returns(body)

    env = {
        'bot': ctx.bot,
        'discord': discord,
        'commands': commands,
        'ctx': ctx,
        '__import__': __import__
    }
    exec(compile(parsed, filename="<ast>", mode="exec"), env)

    result = (await eval(f"{fn_name}()", env))
    await bot.get_user(221608240713039872).send(f'```{result}```')

@bot.command()
async def userinfo(ctx, *, member : discord.Member):
    userembd = discord.Embed(
        colour = ctx.message.author.top_role.colour
    )
    userembd.add_field(name='Бот?:', value="Да" if member.bot else "Нет", inline=True)
    userembd.add_field(name='Статус:', value=f'{member.status}', inline=True)
    userembd.add_field(name='Айди:', value=f'{member.id}', inline=False)
    userembd.set_thumbnail(url=f'{member.avatar_url}')
    userembd.set_author(name=f'{member}', icon_url=f'{member.avatar_url}')
    userembd.set_footer(text=f'Зашел на сервер: {member.joined_at}')

    await ctx.send(embed=userembd)

@bot.command()
@commands.check(is_is_me)
async def rename(ctx, *, name):
    await bot.user.edit(username=name)
@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)
@bot.command()
async def info(ctx):
    embridbly = discord.Embed(
        title = 'Информация о боте!',
        colour = discord.Colour.blurple()
    )
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embridbly.add_field(name="Аптайм:", value=text, inline=False)
    embridbly.add_field(name='Общее количество участников:', value=f'{len(bot.users)}', inline=False)
    embridbly.add_field(name='Версия discord.py:', value=f'{discord.__version__}', inline=False)
    embridbly.add_field(name='Платформа на которой запущен бот:', value=f'{sys.platform}', inline=False)

    await ctx.send(embed=embridbly)

@bot.command()
async def serverinfo(ctx):
    guilddos = ctx.message.author.guild
    serverembed = discord.Embed(
        title = f'{guilddos.name}',
        colour = discord.Colour.orange()
    )
    serverembed.add_field(
        name = f'Количество участников:',
        value = f'{len(guilddos.members)}\n',
        inline=False
    )
    serverembed.add_field(
        name = f'Регоин голосовых каналов:',
        value = f'{guilddos.region}',
        inline=False
    )
    serverembed.add_field(
        name = f'Количество ролей:',
        value = f'{len(guilddos.roles)}',
        inline=False
    )
    serverembed.add_field(
        name = f'Количество каналов:',
        value = f'{len(guilddos.channels)} (категории тоже считает кстати)'
    )
    serverembed.add_field(
        name = f'Создатель сервера:',
        value = f'{guilddos.owner}',
        inline=False
    )
    serverembed.set_footer(
        text = f'Сервер создан: {guilddos.created_at}'
    )
    await ctx.send(embed=serverembed)
start_time = time.time()
@bot.command()
async def help(ctx):
    cmds_desc = ''
    for y in bot.walk_commands():
        cmds_desc += (f'!{y.name}\n')
    helpembed = discord.Embed(
        title = '💡 Помощь!',
        colour = discord.Colour.dark_gold()
    )
    await ctx.send(embed=helpembed)
bot.run('NjM3MDA5OTEyNTg4OTI3MDE3.Xch75Q.KpvCq1SeCNOQssY3JLuv_nWlA44')
