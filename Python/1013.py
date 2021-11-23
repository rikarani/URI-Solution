a = int(input())
b = int(input())
c = int(input())

MajorAB = (a + b + abs(a - b)) / 2
MajorFix = (MajorAB + c + abs(MajorAB - c)) / 2

print(f"{'{0:.0f}'.format(MajorFix)} eh o maior")