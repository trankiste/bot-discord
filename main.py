import aiohttp
import discord
from discord.ext import commands
import random

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/')

reponses_quoi = [
    "ok QUOICOUBEH",
    "feur",
    "QUOICOUBAKA UwU",
]

reponses_ratio = [
    "gros flop rions :joy_cat:",
    "ok flopito :call_me:",
    "pas nécessaire le ratio enfin bref..",
]


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(message):
    if 'quoi' in message.content and bot.user.id != message.author.id:
        print("quoi détecté !")
        reponse = random.choice(reponses_quoi)
        await message.channel.send(f"{message.author.mention} {reponse}")

    elif 'ratio' in message.content and bot.user.id != message.author.id:
        print("ratio détecté !")
        reponse = random.choice(reponses_ratio)
        await message.channel.send(f"{message.author.mention} {reponse}")
    await bot.process_commands(message)

API_KEY='GAn1Jt3SDDJik1pXpxnfnZ2KvlCRGVVm'
@bot.command()
async def meteo(ctx, ville):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_KEY}&q={ville}") as response:
            data = await response.json()
            location_key = data[0]["Key"]
            city_name = data[0]["LocalizedName"]
        async with session.get(f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={API_KEY}&details=true") as response:
            data = await response.json()
            temperature = data[0]["Temperature"]["Metric"]["Value"]
            weather_text = data[0]["WeatherText"]
            wind_speed = data[0]["Wind"]["Speed"]["Metric"]["Value"]
            wind_direction = data[0]["Wind"]["Direction"]["Localized"]
            humidity = data[0]["RelativeHumidity"]
    await ctx.send(f"```Météo actuelle pour {city_name}:\n🌡️Température: {temperature}°C\n🌤️Conditions: {weather_text}\n🌬️Vitesse du vent: {wind_speed} km/h\n🧭Direction du vent: {wind_direction}\n💧Humidité: {humidity}%```")



@bot.command()
async def hello(ctx):
    await ctx.send(ctx.author.mention + " hello!")


bot.run('MTA4MzM3NDExNDEyMDY3MTI3NA.GrRDr3.0kV8TUM3GEYL6PH8lB7vnn5nOLuSoH2hAL6TLw')
