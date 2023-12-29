def convert_MetersToKilometers(meters):
    KM = round(meters/1000, 2)
    return KM

Meters = input("enter meters here: ")
km = convert_MetersToKilometers(float(Meters))
print(f"\noutput: {km} km")