
import asyncio  # 임포트할 모듈 임포트

import discord

from discord.ext import commands

from discord.ext.commands import bot


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("bot starting..")  # 봇 시작이라고 뜨게하기
    game = discord.Game("python bot")  # 게임에서 python bot 하는중... 이라고 표시
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("///와"):  # 만약 내가 !안녕이라고 보냈다면,
        await message.channel.send("샌즈")  # 봇이 안녕하세요 라고 대답
    if message.content.startswith("///언더태일"):  # 만약 내가 !잘가 이라고 보냈다면,
        await message.channel.send("아시는구나!") #봇이 빠이빠이 라고 대답


client.run("NzQ1NjE4NTA3Njg5MDk5NDA0.Xz0ZWQ.HTxDinrnxSDmRUV-de5hjwZsjWs")  # 여러분들의 토큰값
[출처] 디스코드 봇 만들기 3편(화)|작성자 구름의 이늡