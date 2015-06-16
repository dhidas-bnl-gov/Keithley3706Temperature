#!/usr/bin/python

import socket
import time

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect( ('192.168.1.10', 5025) )




while True:
  
  cs.send(  ' buf6.clear() ' )
  cs.send(  ' scan.reset() ')
  cs.send(  ' scan.create("slot6") ')
  cs.send(  ' scan.execute(buf6) ')
  cs.send(  ' printbuffer(1,1,buf6.timestamps) ')
  cs.send(  ' printbuffer(1,20,buf6) ' )
  cs.send(  ' buf6.clear() ')
  cs.send(  ' \n ')

  data = cs.recv(4096)
  print data
  data = cs.recv(4096)
  print data

  time.sleep(3)


cs.close()
