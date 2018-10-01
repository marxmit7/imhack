import discord
import asyncio
from cleverwrap import CleverWrap

cw = CleverWrap("API-KEY")
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    
    if message.content.startswith('!clever_reset'):
        cw.reset()
	await client.send_message(message.channel, 'Sucessfuly reset.')

    elif message.content.startswith('!clever'):
        param = message.content[7:]
	if len(param) > 0:
            await client.send_message(message.channel, cw.say(param))
        else:
            await client.send_message(message.channel, 'Use !clever <message>')

client.run('token')
