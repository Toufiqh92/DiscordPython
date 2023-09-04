import discord
import openai 
import random
from dotenv import env
import os
from discord.ext import commands

load_dotenv()
# enviormental variables

openai.api_key = os.getenv("openai.api_key")
TOKEN = os.getenv("TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="", intents=intents)

# async def on_message(ctx):
#     msg = await ctx.wait_for("message")
#     msg_content = msg.content.lower()

@bot.event
async def on_ready():
    print("HELLO IM READYY")


@bot.command()
async def leg(ctx):
    await ctx.send("@here GET ON LEAGUE")


@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention} welcome to my server")


@bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    await channel.send(f"{member.mention} You will be missed")

    # Need To Fix




# Creates a direct message with a user that is mentioned and sends them this exact message in this string 
# This is very versatile and you are able to manipulate this to sent alot more things

@bot.command()
async def Udm(ctx, member: discord.User):
    await member.send("This is a test, If im texting you then my code worked")


@bot.command()
async def Jake(ctx, *, message):
    # Calling the OpenAI API with only the user's message in the 'messages' parameter
    Who_am_I = "You are a helpful ChatBot Named Jake and you work for StateFarm. Never refer to yourself as a chatbot you will act like a human in any circumstances."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": Who_am_I},
            {"role": "user", "content": message},
        ],
    )

    await ctx.send(response["choices"][0]["message"]["content"])


bot.run(TOKEN)