import discord
import os


client = discord.Client()


@client.event
async def on_message(message):
    if message.content.startswith("///와"):
        await message.channel.send("샌즈")
    if message.content.startswith("///언더태일"):
        await message.channel.send("아시는구나!")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
