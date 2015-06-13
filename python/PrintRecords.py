#!/usr/bin/env python

for i in range (1, 7):
  for j in range (1, 31):
    print 'record(ao, \"$(P){$(M)}Temperature-$(BUS):T', i*1000 + j, '\")',
    print '{',
    print '  field (DESC, "Temperature in Keithley buffer")',
    print '}'
