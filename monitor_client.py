import time
from sensors import *

def read_sensors():

    lx = light_sensor.read_light()
    print "Nivel de luminosidad: " + str(lx) + "lx"

    tmp_rh = tmp_rh_sensor.read_tmp_rh()
    print 'Temperatura de ambiente: {0:0.1f}*C'.format(tmp_rh['tmp'])
    print 'Humedad de ambiente: {0:0.1f}%'.format(tmp_rh['rh'])

    rh_soil = rh_soil_sensor.read_rh_soil()
    print "Humedad del suelo: {:>5} ".format(rh_soil)


def main():
 
  while True:
    read_sensors()
    time.sleep(4)    
	   
if __name__=="__main__":
   main()
