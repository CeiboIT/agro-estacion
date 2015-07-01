import mcp3008

def read_rh_soil():
    m = mcp3008.readadc(5)
    return m
    

