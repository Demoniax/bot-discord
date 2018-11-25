import discord
import asyncio
from random import *
from time import *

##secret values##
id = "515990450545492050"
token = "NTE1OTkwNDUwNTQ1NDkyMDUw.DttJWw.rbTIv3KSruqB0AVwA4c-tsoBNXY"

bot = discord.Client()


description = '''Bot Python'''
help = "```markdown\nUn problème ? Je suis la pour vous aider !\n\n Voici la liste des commandes disponible :\n- ?ping\n- ?who\n```"
liste_pfc = ["Pierre", "Feuilles", "Ciseaux"]
win = "Tu as gagné ! :smiley:"
loose = "Tu as perdu ! :smiley:"
equal = "Aucun gagnant ! :smiley:"


@bot.event
async def on_ready():
    print('------')
    print('Connecté en tant que :',bot.user.name)
    print('ID :',bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content == "?help":
        msg = await bot.send_message(message.channel, help)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "?pfc pierre":
        x = 3
        i = 0
        while i < 3:
            msg = await bot.send_message(message.channel, x)
            x -= 1
            i += 1
        p = "Pierre"
        f = "Feuilles"
        c = "Ciseaux"
        ia_choice = str(choice(liste_pfc))
        if ia_choice == p:
            result = await bot.send_message(message.channel, ia_choice)
            end = await bot.send_message(message.channel, equal)
        elif ia_choice == f:
            result = await bot.send_message(message.channel, ia_choice)
            end = await bot.send_message(message.channel, loose)
        elif ia_choice == c:
            result = await bot.send_message(message.channel, ia_choice)
            end = await bot.send_message(message.channel, win)




bot.run(token)

