import copy
import sys

rows, cols = 3, 4

bad = [[0] * cols] * rows
bad[0][1] = 7

good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7

print("Bad:", bad)
print("Good:", good)

print("Same Row:", bad[0] is bad[1])
print("Different Row:", good[0] is good[1])

stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T Nagar"
}

print(stops[(13.0418, 80.2341)])

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99

print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)

values = list(range(1000000))
tuple_values = tuple(values)

print("List Memory:", sys.getsizeof(values))
print("Tuple Memory:", sys.getsizeof(tuple_values))
