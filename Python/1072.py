N = int(input())
inside = 0
outside = 0

for _ in range(N) :
    X = int(input())

    if (X >= 10 and X <= 20) :
        inside += 1
    else :
        outside += 1

print(f"{inside} in")
print(f"{outside} out")