N = int(input())

hours = N // 3600
sisa_N = N % 3600

minutes = sisa_N // 60
sisa_N = sisa_N % 60

seconds = sisa_N 

print(f"{hours}:{minutes}:{seconds}")