#NIM/Nama : 16623340/Aswal Ikraam Aritonang
#Tanggal : 3 April 2024
#Deskripsi : Program mengisi ulang bilangan pada indeks tertentu dengan bilangan terbesar dari indeks tetangganya dan bilangan itu sendiri





from re import A


elemen=int(input("Masukkan banyaknya elemen: "))
data = [0 for i in range(elemen)]
for i in range(elemen):
    data[i]= int(input(f"Masukkan bilangan ke -{i+1}: "))
print("Kondisi awal :", data)

akhir=[0 for i in range(elemen)]
for i in range(elemen):
    if i == 0:
        if data[i] >= data[i+1]:
            akhir[i] = data[i]
        else:
            akhir[i] = data[i+1]
    elif i == elemen - 1:
        if data[i] >= data[i-1]:
            akhir[i] = data[i]
        else:
            akhir[i] = data[i-1]
    else:
        max = data[i]
        if data[i-1] > max:
            max = data[i-1]
        if data[i+1] > max:
            max = data[i+1]
        akhir[i] = max

print("Kondisi akhir :", akhir)
