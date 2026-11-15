ai_elective = {
    "192311001",
    "192311004",
    "192311007",
    "192311009"
}

iot_elective = {
    "192311002",
    "192311004",
    "192311009",
    "192311010"
}

all_students = {
    f"1923110{i:02d}" for i in range(1, 11)
}

both = ai_elective & iot_elective

exactly_one = ai_elective ^ iot_elective

neither = all_students - (ai_elective | iot_elective)

print("Clash:", sorted(both))
print("Exactly One:", sorted(exactly_one))
print("Neither:", sorted(neither))

print("Union:", ai_elective | iot_elective)
print("Intersection:", ai_elective & iot_elective)
print("Difference:", ai_elective - iot_elective)
print("Symmetric Difference:", ai_elective ^ iot_elective)
