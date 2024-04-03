#NIM/Nama : 16623340/Aswal Ikraam Aritonang 
#Tanggal  : 3 April 2024
#Deskripsi : Program mengubah karakter pengganti spasi menjadi spasi kembali



panjang = int(input("Masukkan panjang pesan: "))
pesan = str(input("Masukkan pesan Tuan Kill: "))
penggantispasi = str(input("Masukkan karakter pengganti spasi: ")) #karakter pengganti spasi


gantispasi = ""


for karakter in pesan:
    if karakter == penggantispasi:
        gantispasi += " "
    elif karakter!=penggantispasi:
        gantispasi += karakter

print(f"Pesan Tuan Kill:",gantispasi)