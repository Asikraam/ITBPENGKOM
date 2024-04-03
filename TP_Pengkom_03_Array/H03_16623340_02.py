#NIM/Nama: 16623340/Aswal Ikraam Aritonang
#Tanggal: 3 April 2024
#Deskripsi : Program untuk Program menentukan letak nilai x ke N dari kumpulan data

banyak_data=int(input("Masukkan nilai banyak data: "))

data=[0 for i in range(banyak_data)]

for i in range (banyak_data):
    data[i]=int(input(f"Masukkan data ke-{i+1}: "))

nilai_x=int(input("Masukkan nilai yang dicari: "))
n=int(input("Masukkan nilai N: "))

nilai=0
for _ in data:
    nilai+=1

posisi=0
i=0
while i< nilai:
    if data[i]==nilai_x:
        posisi+=1
        if posisi==n:
            print(f"Nilai {nilai_x} ke-{n} berada pada indeks {i}.")
    i +=1
