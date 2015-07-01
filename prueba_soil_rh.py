from sensors import *
from time import sleep

while True:
    m = mcp3008.readadc(5)
    print "Moisture level: {:>5} ".format(m)
    sleep(.5)

