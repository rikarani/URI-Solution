jam1, menit1, jam2, menit2 = map(int, input().split())

diff = ((jam2 * 60) + menit2) - ((jam1 * 60) + menit1)

if diff <= 0 :
    diff += 24 * 60

jam = diff // 60
menit = diff % 60

print(f"O JOGO DUROU {jam} HORA(S) E {menit} MINUTO(S)")