from discord.ext import tasks, commands
import time
import core.vars
import core.debug as debug

class Events(commands.Cog):
    i = 0 #gives each event a number, helping us identify it in the console (only shows up if debug is true)
    b = 0 #prevents bot from spamming messages, helps bot know when it's sent the announcement message
    timecache = "blank" #stores time value when successful. This way it knows when it's already sent the message.
    debugLevel = debug.debugLevels["debug"]

    def __init__(self, bot):
        self.bot = bot
        self.run.start()

    def cog_unload(self):
        self.run.cancel()

    # 0. Order of operations:
    # 1. Load necessary data into objects, this includes the channel id, the eventdata, and the currentdate
    # 2. Process each line of eventdata loaded. Splits each line into two items stored in a 'temp' list
    # 3. Test each iteration of temp data against the currentdate, if it finds a match send the message.
    @tasks.loop(seconds=5.0)
    async def run(self): #checks if the time matches, and posts an event reminder if so
        self.log("Events: 1b: "+str(self.b), debug.debugLevels["debug"])
        #1.
        channel = self.bot.get_channel(core.vars.predefinedChannels['announcements']) #creates channel object linked to announcement channel.
        currentdate = core.vars.currentdate #currentdate = DAY, TIME
        eventdata = core.saveload.eventdata #list of events loaded from events.cfg in saveload.py
        self.i = 1
        self.log("-------"+str(1)+"-------", debug.debugLevels["debug"])
        #2.
        for data in eventdata: #compares the current time with the event times loaded
            self.i = self.i + 1
            if(self.i > len(eventdata)): #keeps 'i' from exceeding the amount of events
                self.i = 0
            temp = data.split(" - ") #splits each line in events.cfg in half and puts the result in a list
            time = temp[0]
            message = temp[1]
            self.log("Events: Time: "+time, debug.debugLevels["debug"])
            self.log("Events: Message: "+message, debug.debugLevels["debug"])
            self.log("Events: Testing "+time+" against the current time, "+currentdate, debug.debugLevels["debug"])
            #3.
            if(currentdate == time and self.b == 0): #if the time matches the currentdate, send the message if it hasn't already
                self.log("Events: 2b: "+str(self.b), debug.debugLevels["debug"])
                await channel.send(message)
                self.log("Events: Message sent!", debug.debugLevels["info"])
                self.log("-------"+str(self.i)+"-------", debug.debugLevels["debug"])
                self.timecache = time #stores the successful time to the cache
                self.b = 1
            if (currentdate != self.timecache and self.b == 1):
                self.b = 0
            if (currentdate != time and self.b == 0):
                self.log("Events: 3b: "+str(self.b), debug.debugLevels["debug"])
                self.log("Events: Did not match", debug.debugLevels["debug"])
                self.log("-------"+str(self.i)+"-------", debug.debugLevels["debug"])
        self.log("Events: Completed time check. - "+core.vars.currenttime, debug.debugLevels["info"])

    @run.before_loop
    async def before_loop(self): #waits on bot to connect before starting the events code
        self.log('Events: waiting...', debug.debugLevels["detailed"])
        await self.bot.wait_until_ready()
    
    def log(self, message, logLevel=debug.debugLevels["info"]):
        debug.log(name=self.__class__.__name__, message=message, logLevel=logLevel, classLevel=self.debugLevel)
def setup(bot): #required bit of code so discord.py knows where the cog (this thing) is
    bot.add_cog(Events(bot))
