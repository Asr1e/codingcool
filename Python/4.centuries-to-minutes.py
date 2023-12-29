def convert_CenturiesToMinutes(centuries):
    MIN = round(centuries*52594560, 2)
    return MIN

Centuries = input("enter centuries here: ")
min = convert_CenturiesToMinutes(float(Centuries))
print(f"\noutput: {min} minutes")