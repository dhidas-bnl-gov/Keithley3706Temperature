#!/usr/bin/python

import socket
import time

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect( ('192.168.1.10', 5025) )


cs.send(  ' reset() ')
cs.send(  ' dmm.func = "temperature" ')
cs.send(  ' dmm.reset("active") ')
cs.send(  ' dmm.transducer = dmm.TEMP_FOURRTD ')
cs.send(  ' dmm.fourrtd = dmm.RTD_PT100 ')
cs.send(  ' dmm.configure.set("TemperaturePT100") ')
#cs.send(  ' dmm.setconfig("slot1", "TemperaturePT100") ')
#cs.send(  ' dmm.setconfig("slot2", "TemperaturePT100") ')
#cs.send(  ' dmm.setconfig("slot3", "TemperaturePT100") ')
#cs.send(  ' dmm.setconfig("slot4", "TemperaturePT100") ')
#cs.send(  ' dmm.setconfig("slot5", "TemperaturePT100") ')
cs.send(  ' dmm.setconfig("slot6", "TemperaturePT100") ')
cs.send(  ' buf1 = dmm.makebuffer(200) ')
cs.send(  ' buf1.collecttimestamps = 1 ')
cs.send(  ' buf2 = dmm.makebuffer(200) ')
cs.send(  ' buf2.collecttimestamps = 1 ')
cs.send(  ' buf3 = dmm.makebuffer(200) ')
cs.send(  ' buf3.collecttimestamps = 1 ')
cs.send(  ' buf4 = dmm.makebuffer(200) ')
cs.send(  ' buf4.collecttimestamps = 1 ')
cs.send(  ' buf5 = dmm.makebuffer(200) ')
cs.send(  ' buf5.collecttimestamps = 1 ')
cs.send(  ' buf6 = dmm.makebuffer(200) ')
cs.send(  ' buf6.collecttimestamps = 1 ')

cs.send(  '\n' )
data = cs.recv(512)
print data

cs.close()
