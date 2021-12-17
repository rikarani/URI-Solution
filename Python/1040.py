N1, N2, N3, N4 = list(map(float, input().split()))
exam = 0.0
final_media = 0.0

media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10
print(f"Media: {'{0:.1f}'.format(media)}")

if media >= 7.0 :
    print("Aluno aprovado.")
elif media < 5.0 :
    print("Aluno reprovado.")
elif media >= 5.0 and media <= 6.9 :
    print("Aluno em exame.")

    exam = float(input())
    print(f"Nota do exame: {'{0:.1f}'.format(exam)}")

    final_media = (media + exam) / 2

    if final_media >= 5.0 :
        print("Aluno aprovado.")
    else :
        print("Aluno reprovado.")

    print(f"Media final: {'{0:.1f}'.format(final_media)}")
