from discord.ext import tasks, commands
import core.vars
## WARNING: This file is the DEFINITION of unstable... wear protection while within 20ft of the object
## And I forgot I don't see errors in discord tasks... greeeeeat.
# This is gonna take a bit, placing this version inside its own branch.
class SaveLoad(commands.Cog):
    debug = True

    def __init__(self, bot):
        print("SaveLoad: Initialized")
        self.bot = bot
        self.load.start() #not actually sure if placing two async definitions will make discord mad at me
        self.eventload.start()

    def cog_unload(self):
        self.load.cancel()
        self.eventload.cancel()

    #ported old code to new cog system, will be modifying and fixing issues.
    #check to see if I can run this code either in init or something else without calling a loop.
    #doing this just feels clunky
    @tasks.loop(seconds=1,count=1)
    async def load(self):
        currentdate
        if(core.vars.debug == True and self.debug == True):
            print("SaveLoad: Message Successful")
        dir = os.getcwd()
        with open(dir+"/Data/Global/Temp/timevars.json") as file:
            self.data = json.load(file)
            for item in self.data['times']:
                try:
                    self.currentdate = item['currentdate']
                    print("SaveLoad: Date loaded successfully: "+self.currentdate)
                except:
                    print("SaveLoad: Failed to load date")
        #using currentdate will break things, as this stores a direct timestamp... I was dumb.
        #right now this condition has a 60 second window to be true. Fun!
        if(core.vars.currentdate == self.currentdate):
            #definitely better way to do this using ordinary lists... working on that ASAP, see cogs.events.py - line 40
            for item in self.data['times']:
                core.vars.total=int(item['total'])
                core.vars.a1=int(item['00:00'])
                core.vars.a2=int(item['00:30'])
                core.vars.a3=int(item['01:00'])
                core.vars.a4=int(item['01:30'])
                core.vars.a5=int(item['02:00'])
                core.vars.a6=int(item['02:30'])
                core.vars.a7=int(item['03:00'])
                core.vars.a8=int(item['03:30'])
                core.vars.a9=int(item['04:00'])
                core.vars.a10=int(item['04:30'])
                core.vars.a11=int(item['05:00'])
                core.vars.a12=int(item['05:30'])
                core.vars.a13=int(item['06:00'])
                core.vars.a14=int(item['06:30'])
                core.vars.a15=int(item['07:00'])
                core.vars.a16=int(item['07:30'])
                core.vars.a17=int(item['08:00'])
                core.vars.a18=int(item['08:30'])
                core.vars.a19=int(item['09:00'])
                core.vars.a20=int(item['09:30'])
                core.vars.a21=int(item['10:00'])
                core.vars.a22=int(item['10:30'])
                core.vars.a23=int(item['11:00'])
                core.vars.a24=int(item['11:30'])
                core.vars.a25=int(item['12:00'])
                core.vars.a26=int(item['12:30'])
                core.vars.a27=int(item['13:00'])
                core.vars.a28=int(item['13:30'])
                core.vars.a29=int(item['14:00'])
                core.vars.a30=int(item['14:30'])
                core.vars.a31=int(item['15:00'])
                core.vars.a32=int(item['15:30'])
                core.vars.a33=int(item['16:00'])
                core.vars.a34=int(item['16:30'])
                core.vars.a35=int(item['17:00'])
                core.vars.a36=int(item['17:30'])
                core.vars.a37=int(item['18:00'])
                core.vars.a38=int(item['18:30'])
                core.vars.a39=int(item['19:00'])
                core.vars.a40=int(item['19:30'])
                core.vars.a41=int(item['20:00'])
                core.vars.a42=int(item['20:30'])
                core.vars.a43=int(item['21:00'])
                core.vars.a44=int(item['21:30'])
                core.vars.a45=int(item['22:00'])
                core.vars.a46=int(item['22:30'])
                core.vars.a47=int(item['23:00'])
                core.vars.a48=int(item['23:30'])
                print("SaveLoad: Dates matched, loaded data")
            if(core.vars.currentdate != self.currentdate):
                self.currentdate = core.vars.currentdate
                print("SaveLoad: Dates did not match, did not load data")

    @tasks.loop(hours=4)
    async def eventload(self):
        eventdata = core.vars.eventdata
        try:
            with open("events.cfg") as file:
                eventdata = []
                for line in file:
                    eventdata.append(line.rstrip("\n"))
            print("SaveLoad: Loaded 'events.cfg'")
        except IOError:
            file = open("events.cfg", "w+")
            eventdata = []
            print("SaveLoad: Created 'events.cfg' file")

def setup(bot):
    bot.add_cog(SaveLoad(bot))
