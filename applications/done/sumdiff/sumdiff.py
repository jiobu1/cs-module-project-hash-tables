"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

sums = {}
diffs = {}

# for x in set(q):
#     for y in set(q)
#     function[x] = f(x)

# print(function)


for i in range(0, len(q)):
    for j in range(0, len(q)):
        sums[f'f({q[i]}) + f({q[j]})'] = f(q[i]) + f(q[j])
        diffs[f'f({q[i]}) - f({q[j]})'] = f(q[i]) - f(q[j])

print(sums)
print(diffs)

for i in sums:
    for j in diffs:
        if diffs[j] == sums[i]:
            print(f"{i} = {j} = {sums[i]}")

