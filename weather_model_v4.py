# weather_model_v4.py
# Read multiple sets of a, b, c, t from a file

with open('weather_input_multiple.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    a, b, c, t = map(float, line.strip().split())
    T = a * t ** 2 + b * t + c
    print(f"For a={a}, b={b}, c={c}, t={t} → Temperature: {T}")
