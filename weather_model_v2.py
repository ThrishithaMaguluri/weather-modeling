# weather_model_v2.py
# User input for a, b, c, and t

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))
t = float(input("Enter time (t): "))

T = a * t ** 2 + b * t + c
print("Temperature at time", t, "is:", T)
