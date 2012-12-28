import android as a
droid = a.Android()
d = droid
d.batteryStartMonitoring()

Health = {1: "Unknown", 2: "Good", 3: "Overheat", 4: "Dead", 5: "Over Voltage", 6: "Failure"}
Plug = {-1: "Unknown", 0: "Unplugged", 1: "AC Charger", 2: "USB Port"}
Status = {1: "Unknown", 2: "Charging", 3: "Discharging", 4: "Not Charging", 5: "Full"}

d.eventWaitFor("battery")
d.eventClearBuffer()

print("    ::Full Battery Data::  \n\n", d.readBatteryData().result)
print("\n\n    ::Now In Plain English::\n")

print("Your Battery Is Present:          ", d.batteryCheckPresent().result)
print("Your Battery Technology:          ", d.batteryGetTechnology().result)
print("Your Current Battery Voltage:     ", d.batteryGetVoltage().result, "nV")
print("Your Current Battery Temperature: ", d.batteryGetTemperature().result/10.0, "°C")
print("Your Battery Raw Temperature:      %1.0F (°C/10.0)" % (d.batteryGetTemperature().result))

#Battery Plug Type Key:
# -1: "Unknown" 
#  0: "Unplugged" 
#  1: "AC Charger" 
#  2: "USB Port" 

print("Your Current Battery Plug Type:   ", Plug[d.batteryGetPlugType().result])
print("Your Current Battery Level:       ", d.batteryGetLevel().result, "%") 

#Battery Stat Key:
#  1: "Unknown" 
#  2: "Charging" 
#  3: "Discharging"
#  4: "Not Charging"
#  5: "Full" 

print("Your Current Battery Status:      ", Status[d.batteryGetStatus().result]) 

#Battery Health Key:
#  1: "Unknown"
#  2: "Good"
#  3: "Overheat"
#  4: "Dead" 
#  5: "Over Voltage"
#  6: "Failure"

print("Your Current Battery Health:      ", Health[d.batteryGetHealth().result])
print("\nCheck Power Saver Mode:\n    Need to define all processes related to Power Saver Mode\n    then print if Mode is On or Off.")

print()
d.batteryStopMonitoring()
#end
