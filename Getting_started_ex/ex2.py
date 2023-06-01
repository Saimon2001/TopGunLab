#Getting started with Python
#ex2
F = float(input("Please enter a temperature in Fahrenheit>"))

def to_celcius(fare:float):
    return round((fare-32)/1.8)

print(f"El valor en Celcuis es: {to_celcius(F)}°C")