#PYTHON

nilai=int(input("Masukkan nilai N: "))

huruf=1
angka=nilai-1
#PROGRAM
while huruf>0:
    if nilai%angka==0:
        print("benar")
        huruf-=1
    
    else:
        huruf=1
