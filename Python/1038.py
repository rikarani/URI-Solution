X,Y = input().split()

if (int(X) == 1) :
    harga = 4.00 * int(Y)
    print(f"Total: R$ {'{0:.2f}'.format(harga)}")
elif (int(X) == 2) :
    harga = 4.50 * int(Y)
    print(f"Total: R$ {'{0:.2f}'.format(harga)}")
elif (int(X) == 3) :
    harga = 5.00 * int(Y)
    print(f"Total: R$ {'{0:.2f}'.format(harga)}")
elif (int(X) == 4) :
    harga = 2.00 * int(Y)
    print(f"Total: R$ {'{0:.2f}'.format(harga)}")
else :
    harga = 1.50 * int(Y)
    print(f"Total: R$ {'{0:.2f}'.format(harga)}")