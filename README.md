# Keithley3706Temperature

This package is an interface for the Keithley 3706 hardware device used to read temperature sensors (typically 4-wire pt100 RTDs).  Other type cards in different slots should be easily accomadeted by updating the protocols/Keithley3706Temperature.proto and Keithley3706TemperatureApp/Db/Keithley3706Temperature.db files.  It relies on the StreamDevice package for communication.

There are python scripts in python/ to configure and test the hardware.  The configuration is written to the non-volatile memory and set as bootable so the device should boot into a configured state ready for readout.
  ConfigureKeithley3706.py - For the hardware configuration you wish
  TestKeithley3706.py      - For testing that the readout is correct

The device can easily be included into another ioc or run as its own ioc.

Limitations:
  Only one IOC should connect to the Keithley3706 device.  The device does not allow multiple socket connections.  Do not attempt to have two different IOCs connect to it.

  However, since this uses AsynIP multiple records in the same IOC are allowed and can be loaded as such:
    dbLoadRecords("db/Keithley3706Temperature.db","SYS=S1, DEV=D1, BUS=K1, SLOT=1")
    dbLoadRecords("db/Keithley3706Temperature.db","SYS=S1, DEV=D2, BUS=K1, SLOT=2")
    dbLoadRecords("db/Keithley3706Temperature.db","SYS=S2, DEV=D1, BUS=K1, SLOT=3")

Setup:
  The typical setup in a .cmd file is as follows:
 
    ## EPICS needs to know where to look for the Keithley3706Temperature.proto file 
    epicsEnvSet ("STREAM_PROTOCOL_PATH", "${TOP}/protocols")

    ## Register all support components
    dbLoadDatabase "dbd/Keithley3706Temperature.dbd"
    Keithley3706Temperature_registerRecordDeviceDriver pdbbase

    ## You need to configure in AsnyIPPort for handing off
    drvAsynIPPortConfigure ("K1", "192.168.1.10:5025")

    ## Load records for a BUS and SLOT you are interested.  The SYS and DEV are only names
    ## Currently names are in NSLS2 format, but this can be modified to however you like
    ## Format: $(SYS){$(DEV)-$(BUS)S$(SLOT)}T01
    dbLoadRecords("db/Keithley3706Temperature.db","SYS=S1, DEV=D1, BUS=K1, SLOT=6")

Compilation:
  This follows the EPICS standard.
  To compile: make
  To clean:   make clean uninstall

To run:
  cd iocBoot/iocKeithley3706Temperature/
  ../../bin/linux-x86_64/Keithley3706Temperature st.cmd

