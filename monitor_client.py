from sensors import *

lx = light_sensor.read_light()

print "Light Level : " + str(lx) + " lx"


tmp_rh = tmp_rh_sensor.read_tmp_rh()

print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(tmp_rh['tmp'], tmp_rh['rh'])
