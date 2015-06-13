#!../../bin/linux-x86_64/Keithley3706Temperature


< envPaths

cd ${TOP}

epicsEnvSet("SYS", "SR:C99-ID:G1")
epicsEnvSet("DEV", "IVU88:1")

epicsEnvSet ("STREAM_PROTOCOL_PATH", "${TOP}/protocols")

## Register all support components
dbLoadDatabase "dbd/Keithley3706Temperature.dbd"
Keithley3706Temperature_registerRecordDeviceDriver pdbbase


drvAsynIPPortConfigure ("KTEMP1", "192.168.1.10:5025")
dbLoadRecords("db/Keithley3706Temperature.db","SYS=$(SYS), DEV=$(DEV), BUS=KTEMP1, SLOT=6")
dbLoadRecords("db/Keithley3706Temperature.db","SYS=BLAH, DEV=$(DEV), BUS=KTEMP1, SLOT=6")


cd ${TOP}/iocBoot/${IOC}
iocInit

