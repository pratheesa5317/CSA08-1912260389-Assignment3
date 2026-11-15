timetable = {
    "T101": {
        "name": "Chennai Express",
        "stations": [
            ("Chennai", "06:00", "06:15"),
            ("Katpadi", "08:00", "08:05"),
            ("Jolarpettai", "10:00", "10:05")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    "T102": {
        "name": "Coimbatore Express",
        "stations": [
            ("Chennai", "07:00", "07:15"),
            ("Salem", "10:00", "10:05"),
            ("Coimbatore", "13:00", "13:10")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },

    "T103": {
        "name": "Pandian Express",
        "stations": [
            ("Chennai", "20:00", "20:15"),
            ("Madurai", "05:00", "05:05"),
            ("Tirunelveli", "08:00", "08:10")
        ],
        "days": {"Monday", "Tuesday", "Friday"}
    },

    "T104": {
        "name": "Vaigai Express",
        "stations": [
            ("Chennai", "13:00", "13:15"),
            ("Villupuram", "15:00", "15:05"),
            ("Madurai", "19:00", "19:10")
        ],
        "days": {"Monday", "Wednesday", "Saturday"}
    },

    "T105": {
        "name": "West Coast Express",
        "stations": [
            ("Chennai", "05:00", "05:15"),
            ("Katpadi", "07:00", "07:05"),
            ("Bangalore", "11:00", "11:10")
        ],
        "days": {"Tuesday", "Thursday", "Sunday"}
    }
}

station = "Chennai"
day = "Monday"

result = []

for train_no, details in timetable.items():
    if day in details["days"]:
        for stop in details["stations"]:
            if stop[0] == station:
                result.append((train_no, details["name"], stop))

result = sorted(result, key=lambda x: x[2][2])

print("Station:", station)
print("Day:", day)

for train in result:
    print(train[0], train[1], "Departure:", train[2][2])

print(
    "Third Station Departure:",
    timetable["T101"]["stations"][2][2]
)

index = {}

for train_no, details in timetable.items():
    for stop in details["stations"]:
        index.setdefault(stop[0], []).append(train_no)

print("Station Index:", index)
print("Trains at Chennai:", index.get("Chennai", []))
