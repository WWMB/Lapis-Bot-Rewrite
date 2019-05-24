import discord
from discord.ext import commands, tasks
import logging
import os
import core.setup
import core.saveload
import core.vars
import yaml #pyyaml

logging.basicConfig(level=logging.ERROR)

with open(os.path.join(os.getcwd(),'core','values','bot.yaml')) as stream:
    try:
        botYaml = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


core.vars.predefinedChannels = botYaml['channels']

bot = commands.Bot(command_prefix='+', description='Various things Valdrea needs')
cogs = ['cogs.timer', 'cogs.events', 'cogs.saveload']
gsl = core.saveload.Global() #Global saving/loading class
gset = core.setup.Global() #Global setup class

#try:
#    gsl.load()
#    gsl.eventload()
#except IOError:
gset.setup()
#    gsl.load()
#    gsl.eventload()

if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)
#move timer to its own classes in 'core' folder to be called before bot makes connection.
#seems we don't get feedback from async/discord stuff... :c

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    channel = bot.get_channel(core.vars.predefinedChannels['announcements'])
    if(core.vars.debug == False):
        await channel.send("It's Lapis.")

bot.run(os.environ['DISCORDBOTTOKEN'], reconnect=True)
#unless otherwise stated, code written by Fire#4224
