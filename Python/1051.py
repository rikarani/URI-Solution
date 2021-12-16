N = float(input())

if (N >= 0 and N <= 2000) :
    print("Isento")
elif (N >= 2000.01 and N <= 3000) :
    N -= 2000

    tax = N * 0.08
    print(f"R$ {'{0:.2f}'.format(tax)}")
elif (N >= 3000.01 and N <= 4500) :
    N -= 3000

    tax = N * .18 + 80

    print(f"R$ {'{0:.2f}'.format(tax)}")
else :
    N -= 4500

    tax = N * .28 + 350

    print(f"R$ {'{0:.2f}'.format(tax)}")