import discord
import openai
import random
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY") 
TOKEN = os.getenv("TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents) 
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f"🎉 Welcome {member.mention} to the server!")

@bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f"😢 {member.mention} has left the server.")

@bot.command()
async def leg(ctx):
    await ctx.send("@here GET ON LEAGUE 🕹️")


@bot.command()
async def udm(ctx, member: discord.User):
    """Sends a test DM to the mentioned user"""
    try:
        await member.send("📩 This is a test! If you got this, my code works ✅")
        await ctx.send(f"✅ Sent a DM to {member.mention}")
    except discord.Forbidden:
        await ctx.send("⚠️ I can't send DMs to that user.")


@bot.command()
async def jake(ctx, *, message):
    """Talk to Jake, the helpful assistant from StateFarm"""
    Who_am_I = (
        "You are Jake from StateFarm. "
        "Always act like a helpful, friendly human—not a chatbot."
    )

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": Who_am_I},
                {"role": "user", "content": message},
            ],
        )

        reply = response.choices[0].message.content.strip()
        await ctx.send(reply)

    except Exception as e:
        await ctx.send(f"⚠️ Error: {e}")


# Run Bot 

if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ No Discord TOKEN found. Check your .env file.")
