readings = [3, 5, 60, 7, -55, 9, 4, 2, 10, 6]

valid = []

for temp in readings:
    if -50 <= temp <= 50:
        valid.append(temp)

fahrenheit = []

for temp in valid:
    fahrenheit.append((temp * 9/5) + 32)

valid_comp = [
    temp for temp in readings
    if -50 <= temp <= 50
]

valid_filter = list(
    filter(lambda x: -50 <= x <= 50, readings)
)

fahrenheit_map = list(
    map(lambda x: (x * 9/5) + 32, valid)
)

alarms = [
    (i+1, temp)
    for i, temp in enumerate(readings)
    if -50 <= temp <= 50 and (temp < 2 or temp > 8)
]

temp_dict = {
    i+1: temp for i, temp in enumerate(valid)
}

unique_temps = {temp for temp in valid}

print("Valid Celsius:", valid)
print("Fahrenheit:", fahrenheit)
print("List Comprehension:", valid_comp)
print("Filter Result:", valid_filter)
print("Map Result:", fahrenheit_map)
print("Alarm Minutes:", alarms)
print("Dictionary:", temp_dict)
print("Unique Temperatures:", unique_temps)
