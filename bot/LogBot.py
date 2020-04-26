import discord
import logging
import yaml
import aiohttp
import asyncio
from urllib.request import Request, urlopen
#logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()
token = yaml.safe_load(open('token.yml'))


played_games=[]
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    try:
        n = len(message.attachments[0].filename)
        filenametest = message.attachments[0].filename[n-3:n]
        
        if filenametest == "txt":
            url = message.attachments[0].url
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            lines = urlopen(req)
            for line in lines:
                output=line.decode('utf-8')
                
                if(output[61:74]=="yuzu Version:"):
                    end_index=str(output).find("| HEAD")
                    yuzu_version = output[74:end_index]
                elif(output[61:70]=="Host CPU:"):
                    cpu = output[70:]
                elif(output[61:69]=="Host OS:"):
                    os = output[69:]
                elif(output[94:101]=="Vulkan:"):
                    renderer="Vulkan"
                    print(renderer)
                elif(output[106:117]=="GL_VERSION:"):
                    renderer="OpenGl"
                    print(renderer)
                elif(output[106:117]=="GL_VERSION:"):
                    renderer="OpenGl"
                    print(renderer)
                elif(output[59:72]=="Booting game:"):
                    played_games.append(str(output[91:]).replace("\r\n",""))
                    
            
                
        else:
            return
    except IndexError:
        pass

client.run(token["token"])
