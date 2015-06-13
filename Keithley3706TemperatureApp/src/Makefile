TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

#LIBRARY_IOC += Keithley3706TemperatureSupport


# Compile and add the code to the support library
#Keithley3706TemperatureSupport_SRCS += xxxRecord.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application.
#Keithley3706TemperatureSupport_SRCS += dbSubExample.c

#Keithley3706TemperatureSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC = Keithley3706Temperature
# Keithley3706Temperature.dbd will be created and installed
#DBDINC += Keithley3706Temperature
DBD += Keithley3706Temperature.dbd

# Keithley3706Temperature.dbd will be made up from these files:
Keithley3706Temperature_DBD += base.dbd
Keithley3706Temperature_DBD += stream.dbd
Keithley3706Temperature_DBD += asyn.dbd
Keithley3706Temperature_DBD += drvAsynIPPort.dbd

# Keithley3706Temperature_registerRecordDeviceDriver.cpp derives from Keithley3706Temperature.dbd
Keithley3706Temperature_SRCS += Keithley3706Temperature_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
Keithley3706Temperature_SRCS_DEFAULT += Keithley3706TemperatureMain.cpp
Keithley3706Temperature_SRCS_vxWorks += -nil-

# Link in the code from the support library
#Keithley3706Temperature_LIBS += Keithley3706TemperatureSupport
Keithley3706Temperature_LIBS += stream
Keithley3706Temperature_LIBS += asyn


# Finally link to the EPICS Base libraries
#Keithley3706Temperature_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

