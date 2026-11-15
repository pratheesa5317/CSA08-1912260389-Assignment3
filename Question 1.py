import random

readings = [random.randint(0, 100) for i in range(365)]

weekly_totals = []

for i in range(0, 365, 7):
    weekly_totals.append(sum(readings[i:i+7]))

print("Weekly Totals:", weekly_totals)

print("Maximum Rainfall:", max(readings))
print("Minimum Rainfall:", min(readings))

moving_average = []

for i in range(len(readings)-6):
    moving_average.append(sum(readings[i:i+7])/7)

print("Moving Average:", moving_average)

dry_days = []

for i in range(len(readings)):
    if readings[i] == 0:
        dry_days.append(i+1)

print("Dry Days:", dry_days)

total = sum(readings[:7])
running_average = [total/7]

for i in range(7, len(readings)):
    total = total + readings[i] - readings[i-7]
    running_average.append(total/7)

print("Running Average:", running_average)
