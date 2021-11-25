A,B = map(int,input().split())

if (A < B) :
    waktu = B - A
else :
    waktu = (B + 24) - A

print(f"O JOGO DUROU {waktu} HORA(S)")