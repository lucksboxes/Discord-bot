import discord
import os


client = discord.Client()


@client.event
async def on_message(message):
    if message.content.startswith("///와"):
        await message.channel.send("샌즈")
    if message.content.startswith("///언더태일"):
        await message.channel.send("아시는구나!")


client.run("NzQ1NjE4NTA3Njg5MDk5NDA0.Xz0ZWQ.HTxDinrnxSDmRUV-de5hjwZsjWs")
