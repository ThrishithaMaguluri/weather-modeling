# weather_model_v1.py
# Quadratic model: T(t) = a*t^2 + b*t + c

a = 1.2
b = -3.4
c = 20.0
t = 5  # fixed time

# Calculate temperature
T = a * t ** 2 + b * t + c
print("Temperature at time", t, "is:", T)
