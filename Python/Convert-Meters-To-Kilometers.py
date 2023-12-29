def convert_MetersToKilometers(meters):
    KM = round(meters*1000, 2) #uses Pythons built-in/already existing round() functi>
    return KM

Meters = input("enter meters here: ")
km = convert_MetersToKilometers(float(Meters))
#call the converting function with inpu>
print(f"\noutput:{km}km")