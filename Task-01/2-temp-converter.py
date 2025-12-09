def farenheit_to_celcius(temp_f):
    return (temp_f - 32) * 5 / 9


def celcius_to_farenheit(temp_c):
    return (temp_c * 9 / 5) + 32


temp_f = float(input("Enter temparature in FarenHeight: "))
converted_in_celcius = farenheit_to_celcius(temp_f)
print(f"Converted Into Celcius : {converted_in_celcius:.2f}\n")

temp_c = float(input("Enter temparature into Celcius: "))
converted_in_farenheit = celcius_to_farenheit(temp_c)
print(f"Converted into Farenheit: {converted_in_farenheit:.2f}\n")
