FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(farenheit):
    temp = (farenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temp

def convert_to_farenheit(celsius):
    temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temp

temperature = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Farenheit? (C/F):")

if (not temperature.isdigit()):
    print("Invalid temperature. Please enter a numeric value.")
else:
    if unit == "C":
        converted_temperature = convert_to_farenheit(float(temperature))
        print(f"{temperature}°C is {converted_temperature}°F")
    elif unit == "F":
        converted_temperature = convert_to_celsius(float(temperature))
        print(f"{temperature}°F is {converted_temperature}°C")
    else:
        print("Invalid unit.")
