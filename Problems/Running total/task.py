a = [int(s) for s in input()]

print([sum(a[:i + 1]) for i in range(len(a))])