import random
import asyncio
from discord import Game
from discord.ext.commands import Bot
import aiohttp
import discord
import requests
BOT_PREFIX = ("?", "!")
TOKEN = "NDM4NDY2MjU1MTQyNTE4Nzg3.DcFBDg.WQiXAtYEEuwRyVKfZtKL21BbpUA"

client = Bot(command_prefix=BOT_PREFIX)



@client.event
async def on_ready():
    await client.change_presence(game=Game(name="!help or ?help"))
    print("Ready when you are")
    print("I am running on: " + client.user.name)
    print("With the ID: " + client.user.id)
    owner = await client.get_user_info("428240615558610954")
    await client.send_message(owner, "Ready!", tts=True)
    for server in client.servers:
        print("_________________________")
        print(server.name)
        print("-------------------------")


@client.command()
async def btc():
    url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```Btc Coin's price is: $" + value +"\n\nBtc Coins rank is:" + rank +"\n\nBtc Coins total supply is:" + supply +"\n\nBtc coins percent change in the past hour is:" + change1 +"\n\nBtc Coins percent change in the past 24 hours is:" + change24 +"\n\nBtc Coins percent change in the past 7 Days is:" + change72 +"\n\nBtc Coins 24 hour volume is:" + vol24+"\n\nBtc Coins symbol is:"+ sym + "```")

    print("BTC EXECUTED")
########################################################################done
@client.command()
async def eth():
    url = 'https://api.coinmarketcap.com/v1/ticker/ethereum/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```Eth Coin's price is: $" + value +"\n\nEth Coins rank is:" + rank +"\n\nEth Coins total supply is:" + supply +"\n\nEth coins percent change in the past hour is:" + change1 +"\n\nEth Coins percent change in the past 24 hours is:" + change24 +"\n\nEth Coins percent change in the past 7 Days is:" + change72 +"\n\nEth Coins 24 hour volume is:" + vol24+"\n\nEth Coins symbol is:"+ sym + "```")

@client.command()
async def ripple():
    url = 'https://api.coinmarketcap.com/v1/ticker/ripple/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```XRP Coin's price is: $" + value +"\n\nXRP Coins rank is:" + rank +"\n\nXRP Coins total supply is:" + supply +"\n\nXRP coins percent change in the past hour is:" + change1 +"\n\nXRP Coins percent change in the past 24 hours is:" + change24 +"\n\nXRP Coins percent change in the past 7 Days is:" + change72 +"\n\nXRP Coins 24 hour volume is:" + vol24+"\n\nXRP Coins symbol is:"+ sym + "```")

    print("XRP EXECUTED")
@client.command()
async def litecoin():
    url = 'https://api.coinmarketcap.com/v1/ticker/litecoin/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("Litecoins price is: $" + value)
    await client.say("Litecoins rank is: " + rank)
    await client.say("Litecoins total supply is: " + supply)
    await client.say("Litecoins percent change in the past hour is: " +change1)
    await client.say("Litecoins percent change in the past 24 hours is:" + change24)
    await client.say("Litecoins percent change in the past 7 days is:" + change72)
    await client.say("Litecoins 24 hour volume is:" + vol24)
    await client.say("Litecoins symbol is: " + sym)
    await client.say("_________________________________________________")
    await client.say("""The original author of Litecoin is: Charlie Lee.
Litecoins inital release was in October of 2011.
Like Bitcoin, litecoin is a peer to peer cryptocurrency and a open source software project realesed under the MIT/X11 license.""")
    print("LITECOIN EXECUTED")
###########done
@client.command()
async def neo():
    url = 'https://api.coinmarketcap.com/v1/ticker/neo/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("Neos price is: $" + value)
    await client.say("Neos rank is: " + rank)
    await client.say("Neos total supply is: " + supply)
    await client.say("Neos percent change in the past hour is: " +change1)
    await client.say("Neos percent change in the past 24 hours is:" + change24)
    await client.say("Neos percent change in the past 7 days is:" + change72)
    await client.say("Neos 24 hour volume is:" + vol24)
    await client.say("Neos symbol is: " + sym)
    await client.say("_________________________________________________")
    print("NEO EXECUTED")
@client.command()
async def eos():
    url = 'https://api.coinmarketcap.com/v1/ticker/EOS/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("EOS'S price is: $" + value)
    await client.say("EOS'S rank is: " + rank)
    await client.say("EOS'S total supply is: " + supply)
    await client.say("EOS'S percent change in the past hour is: " +change1)
    await client.say("EOS'S percent change in the past 24 hours is:" + change24)
    await client.say("EOS'S percent change in the past 7 days is: " + change72)
    await client.say("EOS'S 24 hour volume is: " + vol24)
    await client.say("EOS'S symbol is: " + sym)
    print("EOS EXECUTED")
@client.command()
async def dash():
    url = 'https://api.coinmarketcap.com/v1/ticker/dash/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```Dash Coin's price is: $" + value +"\n\nDash Coins rank is:" + rank +"\n\nDash Coins total supply is:" + supply +"\n\nDash coins percent change in the past hour is:" + change1 +"\n\nDash Coins percent change in the past 24 hours is:" + change24 +"\n\nDash Coins percent change in the past 7 Days is:" + change72 +"\n\nDash Coins 24 hour volume is:" + vol24+"\n\nDash Coins symbol is:"+ sym +"```")
    print("BTCG EXECUTED")
@client.command()
async def zcash():
    url = 'https://api.coinmarketcap.com/v1/ticker/zcash/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```Zcash Coin's price is: $" + value +"\n\nZcash Coins rank is:" + rank +"\n\nZcash Coins total supply is:" + supply +"\n\nZcash coins percent change in the past hour is:" + change1 +"\n\nZcash Coins percent change in the past 24 hours is:" + change24 +"\n\nZcash Coins percent change in the past 7 Days is:" + change72 +"\n\nZcash Coins 24 hour volume is:" + vol24+"\n\nZcash Coins symbol is:"+ sym + "```")
    print("BTCG EXECUTED")
@client.command()
async def metal():
    url = 'https://api.coinmarketcap.com/v1/ticker/metal/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```Metal Coin's price is: $" + value +"\n\nMetal Coins rank is:" + rank +"\n\nMetal Coins total supply is:" + supply +"\n\nMetal coins percent change in the past hour is:" + change1 +"\n\nMetal Coins percent change in the past 24 hours is:" + change24 +"\n\nMetal Coins percent change in the past 7 Days is:" + change72 +"\n\nMetal Coins 24 hour volume is:" + vol24+"\n\nMetal Coins symbol is:"+ sym + "```")
    print("BTCG EXECUTED")
@client.command()
async def trump():
    url = 'https://api.coinmarketcap.com/v1/ticker/trumpcoin/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```Trump Coin's price is: $" + value +"\n\nTrump Coins rank is:" + rank +"\n\nTrump Coins total supply is:" + supply +"\n\nTrump coins percent change in the past hour is:" + change1 +"\n\nTrump Coins percent change in the past 24 hours is:" + change24 +"\n\nTrump Coins percent change in the past 7 Days is:" + change72 +"\n\nTrump Coins 24 hour volume is:" + vol24+"\n\nTrump Coins symbol is:"+ sym + "```")

    print("BTCG EXECUTED")
@client.command()
async def gas():
    url = 'https://api.coinmarketcap.com/v1/ticker/gas/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```GAS Coin's price is: $" + value +"\n\nGAS Coins rank is:" + rank +"\n\nGAS Coins total supply is:" + supply +"\n\nGAS coins percent change in the past hour is:" + change1 +"\n\nGAS Coins percent change in the past 24 hours is:" + change24 +"\n\nGAS Coins percent change in the past 7 Days is:" + change72 +"\n\nGAS Coins 24 hour volume is:" + vol24+"\n\nGAS Coins symbol is:"+ sym + "```")

    print("BTCG EXECUTED")
@client.command()
async def gts():
    url = 'https://api.coinmarketcap.com/v1/ticker/game/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```GTS Coin's price is: $" + value +"\n\nGTS Coins rank is:" + rank +"\n\nGTS Coins total supply is:" + supply +"\n\nGTS coins percent change in the past hour is:" + change1 +"\n\nGTS Coins percent change in the past 24 hours is:" + change24 +"\n\nGTS Coins percent change in the past 7 Days is:" + change72 +"\n\nGTS Coins 24 hour volume is:" + vol24+"\n\nGTS Coins symbol is:"+ sym + "```")

    print("BTCG EXECUTED")
@client.command()
async def salus():
    url = 'https://api.coinmarketcap.com/v1/ticker/salus/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```Salus Coin's price is: $" + value +"\n\nSalus Coins rank is:" + rank +"\n\nSalus Coins total supply is:" + supply +"\n\nSalus coins percent change in the past hour is:" + change1 +"\n\nSalus Coins percent change in the past 24 hours is:" + change24 +"\n\nSalus Coins percent change in the past 7 Days is:" + change72 +"\n\nSalus Coins 24 hour volume is:" + vol24+"\n\nSalus Coins symbol is:"+ sym + "```")

    print("BTCG EXECUTED")
@client.command()
async def btg():
    url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin-gold/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```Bitcoin Golds Coin's price is: $" + value +"\n\nBitcoin Golds Coins rank is:" + rank +"\n\nBitcoin Golds Coins total supply is:" + supply +"\n\nBitcin Golds coins percent change in the past hour is:" + change1 +"\n\nBitcoin Golds Coins percent change in the past 24 hours is:" + change24 +"\n\nBitcoin Gold Coins percent change in the past 7 Days is:" + change72 +"\n\nBitcoin Gold Coins 24 hour volume is:" + vol24+"\n\nBitcoin Gold Coins symbol is:"+ sym + "```")

    print("BTCG EXECUTED")
@client.command()
async def guppy():
    url = 'https://api.coinmarketcap.com/v1/ticker/guppy/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```Guppy Coin's price is: $" + value +"\n\nGuppy Coins rank is:" + rank +"\n\nGuppy Coins total supply is:" + supply +"\n\nGuppy coins percent change in the past hour is:" + change1 +"\n\nGuppy Coins percent change in the past 24 hours is:" + change24 +"\n\nGuppy Coins percent change in the past 7 Days is:" + change72 +"\n\nGuppy Coins 24 hour volume is:" + vol24+"\n\nGuppy Coins symbol is:"+ sym + "```")

    print("GUPPY EXECUTED")
@client.command()
async def nxt():
    url = 'https://api.coinmarketcap.com/v1/ticker/nxt/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```NXT Coin's price is: $" + value +"\n\nNXT Coins rank is:" + rank +"\n\nNXT Coins total supply is:" + supply +"\n\nNXT coins percent change in the past hour is:" + change1 +"\n\nNXT Coins percent change in the past 24 hours is:" + change24 +"\n\nNXT Coins percent change in the past 7 Days is:" + change72 +"\n\nNXT Coins 24 hour volume is:" + vol24+"\n\nNXT Coins symbol is:"+ sym + "```")

    print("NXT EXECUTED")
@client.command()
async def tronix():
    url = 'https://api.coinmarketcap.com/v1/ticker/tronix/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```Tronix Coin's price is: $" + value +"\n\nTronix Coins rank is:" + rank +"\n\nTronix Coins total supply is:" + supply +"\n\nTronix coins percent change in the past hour is:" + change1 +"\n\nTronix Coins percent change in the past 24 hours is:" + change24 +"\n\nTronix Coins percent change in the past 7 Days is:" + change72 +"\n\nTronix Coins 24 hour volume is:" + vol24+"\n\nTronix Coins symbol is:"+ sym + "```")

    print("TRONIX EXECUTED")
@client.command()
async def manna():
    url = 'https://api.coinmarketcap.com/v1/ticker/manna/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```MANNA Coin's price is: $" + value +"\n\nMANNA Coins rank is:" + rank +"\n\nMANNA Coins total supply is:" + supply +"\n\nMANNA coins percent change in the past hour is:" + change1 +"\n\nMANNA Coins percent change in the past 24 hours is:" + change24 +"\n\nMANNA Coins percent change in the past 7 Days is:" + change72 +"\n\nMANNA Coins 24 hour volume is:" + vol24+"\n\nMANNA Coins symbol is:"+ sym + "```")

    print("MANNA EXECUTED")
@client.command()
async def qtum():
    url = 'https://api.coinmarketcap.com/v1/ticker/qtum/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("```QTUM Coin's price is: $" + value +"\n\nQTUM Coins rank is:" + rank +"\n\nQTUM Coins total supply is:" + supply +"\n\nQTUM coins percent change in the past hour is:" + change1 +"\n\nQTUM Coins percent change in the past 24 hours is:" + change24 +"\n\nQTUM Coins percent change in the past 7 Days is:" + change72 +"\n\nQTUM Coins 24 hour volume is:" + vol24+"\n\nQTUM Coins symbol is:"+ sym + "```")

    print("QTUM EXECUTED")

##########################


#print("hi \ngod")

#@client.command()
#async def test():
#    url = 'https://api.coinmarketcap.com/v1/ticker/qtum/'
#    response = requests.get(url)
#    value = response.json()[0]["price_usd"]
#    rank = response.json()[0]["rank"]
#    supply = response.json()[0]["total_supply"]
#    change1 = response.json()[0]["percent_change_1h"]
#    change24 = response.json()[0]["percent_change_24h"]
#   change72 = response.json()[0]["percent_change_7d"]
#    vol24 = response.json()[0]["24h_volume_usd"]
#    sym = response.json()[0]["symbol"]
#    await client.say("```QTUM Coin's price is: $" + value +"\n\nQTUM Coins rank is:" + rank +"\n\nQTUM Coins total supply is:" + supply +"\n\nQTUM coins percent change in the past hour is:" + change1 +"\n\nQTUM Coins percent change in the past 24 hours is:" + change24 +"\n\nQTUM Coins percent change in the past 7 Days is:" + change72 +"\n\nQTUM Coins 24 hour volume is:" + vol24+"\n\nQTUM Coins symbol is:"+ sym + "```")




client.run(TOKEN)