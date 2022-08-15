import discord
import os
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(('help','Help')):
        msg1 = 'Hey Dude, Here are bot commands for you !!! {0.author.mention}'.format(message)
        await message.channel.send('==================================')
        await message.channel.send(msg1)
        await message.channel.send('==================================')
        await message.channel.send('Bot Commands :-\n1)  help\n2) hi\n3) !activate\n4) !code Your_Code')
        await message.channel.send('==================================')
  
    if message.content.startswith(('!activate','!Activate')):
        response = requests.get("https://redeem-the-code.herokuapp.com")
        await message.channel.send('==================================')
        await message.channel.send('Bot Activated..!!!')
        await message.channel.send('==================================')
  
    if message.content.startswith(('hi','Hi','Hii','hii')):
        msg1 = 'Hey Dude, Welcome Here !!! {0.author.mention}'.format(message)
        await message.channel.send('==================================')
        await message.channel.send(msg1)
        await message.channel.send('==================================')

    if message.content.startswith(('!code','!Code')):
        l=str(message.content)
        li=l.split()
        if(len(li)==1):
          await message.channel.send("No Code Entered...!!!")
        else:
          response = requests.get("https://redeem-the-code.herokuapp.com/redeem/"+li[1])
          await message.channel.send('==================================')
          await message.channel.send('Code :- {}, Added For Redeemption'.format(li[1]))
          await message.channel.send('==================================')
          await message.channel.send('Please Wait For a Minute Untill You Enter Another...!!!')
          await message.channel.send('==================================')

            
from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "Hello. I am alive!"


def run():
    app.run(debug=True)


def keep_alive():
    t = Thread(target=run)
    t.start()
            
keep_alive()
client.run(os.getenv('TOKEN'))
