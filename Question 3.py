from collections import Counter

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = text.lower().split()

        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts

def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )[:k]

result = frequencies(calls, STOP)

print("Word Frequencies:", result)
print("Top 3 Words:", top(result, 3))

districts = {
    "Tirunelveli": ["seed problem", "water problem"],
    "Chennai": ["fertiliser problem", "seed problem"]
}

print("District Complaints:", districts)

print("Keys:", result.keys())
print("Values:", result.values())
print("Items:", result.items())

counter_result = Counter(
    word
    for text in calls
    for word in text.lower().split()
    if word not in STOP
)

print("Counter Result:", counter_result)
