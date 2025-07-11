# weather_model_v3.py
# Read values of a, b, c, and t from a file

with open('weatherinput.txt', 'r') as file:
    a = float(file.readline())
    b = float(file.readline())
    c = float(file.readline())
    t = float(file.readline())

T = a * t ** 2 + b * t + c
print("Temperature at time", t, "is:", T)
