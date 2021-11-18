x = input().split()
y = input().split()

kode_produk_1, banyaknya_produk_1, harga_produk_1 = x
kode_produk_2, banyaknya_produk_2, harga_produk_2 = y

total_harga = (int(banyaknya_produk_1) * float(harga_produk_1)) + (int(banyaknya_produk_2) * float(harga_produk_2))

print(f"VALOR A PAGAR: R$ {'{0:.2f}'.format(total_harga)}")