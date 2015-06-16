#!/usr/bin/env python

for i in range (1, 7):
  for j in range (1, 31):
    print '     \"%($(sys,undefined){$(dev,undefined)}Temperature-$(BUS):T)', i*1000+j,' \",'
