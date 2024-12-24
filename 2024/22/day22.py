import collections
total = 0
sequences = collections.defaultdict(int)
for s in [int(x) for x in open('input.txt','r')]:
    changes = collections.deque(maxlen=4)
    previous = s % 10
    seen = set()
    for _ in range(2000):
        s = (s ^ (64 * s)) % 16777216
        s = (s ^ (s//32)) % 16777216
        s = (s ^ (s * 2048)) % 16777216
        changes.append((s%10)-previous)
        previous = s%10
        if tuple(changes) not in seen:
            seen.add(tuple(changes))
            sequences[tuple(changes)] += previous
    total+=s
print(total)
print(max(sequences.values()))