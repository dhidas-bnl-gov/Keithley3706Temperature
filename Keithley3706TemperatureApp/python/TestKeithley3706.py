#!/usr/bin/python

import socket
import time

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect( ('192.168.1.10', 5025) )




while True:
  
  cs.send(  ' readSlot6.run() ' )
  cs.send(  ' \n ')

  data = cs.recv(4096)
  print data,
  data = cs.recv(4096)
  print data,

  time.sleep(3)


cs.close()
