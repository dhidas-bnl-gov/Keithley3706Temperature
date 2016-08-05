#!/usr/bin/python

import socket
import time

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect( ('192.168.1.101', 5025) )


# Reset and define the temperature function we want to use.
# Then configure which slots we want to use what temperature functions.
# In principle this can be done channel by channel, or with groupings
# of channels eg '6001,6004', or '6002:6008' for a range

cs.send(  'reset()')
cs.send(  '\n' )
#data = cs.recv(512)
#print data

cs.send(  ' baseConfig = script.new("')
cs.send(  ' dmm.func = \'temperature\'')
cs.send(  ' dmm.reset(\'active\')')
cs.send(  ' dmm.transducer = dmm.TEMP_FOURRTD')
cs.send(  ' dmm.fourrtd = dmm.RTD_PT100')
cs.send(  ' dmm.configure.set(\'TemperaturePT100\')')

cs.send(  ' dmm.func = \'temperature\'')
cs.send(  ' dmm.reset(\'active\')')
cs.send(  ' dmm.transducer = dmm.TEMP_THERMOCOUPLE')
cs.send(  ' dmm.thermocouple = dmm.THERMOCOUPLE_K')
cs.send(  ' dmm.configure.set(\'TemperatureTC\')')



#cs.send(  ' dmm.setconfig(\'slot1\', \'TemperaturePT100\')')
#cs.send(  ' dmm.setconfig(\'1001:1016\', \'TemperaturePT100\')')
#cs.send(  ' dmm.setconfig(\'1017:1020\', \'TemperatureTC\')')
cs.send(  ' dmm.setconfig(\'1017\', \'TemperatureTC\')')
#cs.send(  ' dmm.setconfig(\'slot2\', \'TemperaturePT100\')')
#cs.send(  ' dmm.setconfig(\'slot3\', \'TemperaturePT100\')')
#cs.send(  ' dmm.setconfig(\'slot4\', \'TemperaturePT100\')')
#cs.send(  ' dmm.setconfig(\'slot5\', \'TemperaturePT100\')')
#cs.send(  ' dmm.setconfig(\'slot6\', \'TemperaturePT100\')')


cs.send(  ' buf1 = dmm.makebuffer(200)')
cs.send(  ' buf1.collecttimestamps = 1')
#cs.send(  ' buf2 = dmm.makebuffer(200)')
#cs.send(  ' buf2.collecttimestamps = 1')
#cs.send(  ' buf3 = dmm.makebuffer(200)')
#cs.send(  ' buf3.collecttimestamps = 1')
#cs.send(  ' buf4 = dmm.makebuffer(200)')
#cs.send(  ' buf4.collecttimestamps = 1')
#cs.send(  ' buf5 = dmm.makebuffer(200)')
#cs.send(  ' buf5.collecttimestamps = 1')
#cs.send(  ' buf6 = dmm.makebuffer(200)')
#cs.send(  ' buf6.collecttimestamps = 1'
cs.send( '", "baseConfig")')
cs.send(  ' baseConfig.autorun = "yes"')
cs.send(  ' baseConfig.save()')
cs.send(  '\n' )
#data = cs.recv(512)
#print data

cs.send(  'baseConfig.run()')
cs.send(  '\n' )
#data = cs.recv(512)
#print data


cs.send(  ' readSlot1 = script.new("')
cs.send(  ' buf1.clear()')
cs.send(  ' scan.reset()')
#cs.send(  ' scan.create(\'1001:1018\')')
cs.send(  ' scan.create(\'slot1\')')
cs.send(  ' scan.execute(buf1)')
cs.send(  ' printbuffer(1,1,buf1.timestamps)')
cs.send(  ' printbuffer(1,20,buf1)')
cs.send(  ' buf1.clear()",  "readSlot1")')
cs.send(  '\n' )
#data = cs.recv(512)
#print data
cs.send(  'readSlot1.save()')
cs.send(  '\n' )
#data = cs.recv(512)
#print data



