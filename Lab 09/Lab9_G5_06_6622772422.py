c = int(input("Input temperature in degree Celcius: "))

def CelsiusToFahrenheit(c):
    f = ((c*9)/5)+32
    print("The degree in Farenheit is %.2f" % f)

CelsiusToFahrenheit(c)