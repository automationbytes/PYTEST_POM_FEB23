from jproperties import Properties
propfile = Properties()

class PropReader:
   def readProp(Key):
       with open("./Config.properties", "rb") as configfile:
        propfile.load(configfile)
        return propfile.get(Key).data

#
# P = PropReader
# print(P.readProp("url"))