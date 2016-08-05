#!../../bin/linux-x86_64/Keithley3706Temperature


< envPaths

cd ${TOP}

epicsEnvSet("SYS", "SR:C99-ID:G1")
epicsEnvSet("DEV", "NYX:1")

epicsEnvSet ("STREAM_PROTOCOL_PATH", "${TOP}/protocols")

## Register all support components
dbLoadDatabase "dbd/Keithley3706Temperature.dbd"
Keithley3706Temperature_registerRecordDeviceDriver pdbbase


drvAsynIPPortConfigure ("K1", "192.168.1.101:5025")
dbLoadRecords("db/Keithley3706Temperature.db","SYS=$(SYS), DEV=$(DEV), BUS=K1, SLOT=1")


cd ${TOP}/iocBoot/${IOC}
iocInit

