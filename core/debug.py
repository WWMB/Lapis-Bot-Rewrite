import core.vars

#higher is more detail
debugLevels = {}
for index, level in enumerate(["none", "error", "info", "detailed", "debug"]):
    debugLevels[level] = index
    debugLevels[index] = level #turn numbers back into text for display

def log(name, message, logLevel=debugLevels["info"], classLevel=debugLevels["info"]):
    if(classLevel <= debugLevels["none"]):
        print("NOPE!")
        return
    if((classLevel >= logLevel) and (core.vars.debugLevel >= logLevel)):
        print("[{name}.{level}]\t{message}".format(name=name,level=debugLevels[logLevel],message=message))