
print("1. Volume Kubus")
print("2. Luas Permukaan Kubus")
print("3. Volume Balok")
print("4. Luas Permukaan Balok")
print("5. Volume Limas")
print("6. Luas Permukaan Limas")
print("7. Volume Prisma Segitiga")
print("8. Luas Permukaan Prisma Segitiga")

pilihan = input("Pilih Menu : ")
if pilihan == "1" :
    print("Volume Kubus")
    sisi = float(input("Masukkan Sisi : "))
    volume = float(sisi) ** 3
    print("Hasil Volume pada Kubus adalah", volume, "cm³")
if pilihan == "2" :
    print("Luas Permukaan Kubus")
    sisi = float(input("Masukkan Sisi Kubus : "))
    luas_permukaan = 6 * float(sisi) ** 2
    print("Luas Permukaan Kubus adalah", luas_permukaan, "cm²")
if pilihan == "3" :
    print("Volume Balok")
    panjang = float(input("Masukkan Panjang Balok : "))
    lebar = float(input("Masukkan Lebar Balok : "))
    tinggi = float(input("Masukkan Tinggi Balok : "))
    volume = float(panjang) * float(lebar) * float(tinggi)
    print("Volume pada Balok adalah", volume, "cm³")
if pilihan == "4" :
    print("Luas Permukaan Balok")
    panjang = float(input("Masukkan Panjang Balok : "))
    lebar = float(input("Masukkan Lebar Balok : "))
    tinggi = float(input("Masukkan Tinggi Balok : "))
    volume = float(panjang) * float(lebar) * float(tinggi)
    luas_permukaan = 2 * ((float(panjang) * float(lebar)) + (float(panjang) * float(tinggi)) + (float(lebar) + float(tinggi)))
    print("Luas Permukaan pada Balok adalah", luas_permukaan, "cm")  
if pilihan == "5" :
    print("Volume Limas Segitiga")
    panjang_alas = float(input("Masukkan panjang pada alas : "))
    tinggi_alas = float(input("Masukkan tinggi pada alas : "))
    tinggi_limas = float(input("Masukkan tinggi Limas : "))
    luas_alas = float(panjang_alas) * float(tinggi_alas) / 2
    volume = float(luas_alas) * float(tinggi_limas) / 3
    print("Volume pada Limas adalah", volume, "cm³")
if pilihan == "6" :
    print("Luas Permukaan Limas")
    
if pilihan == "7" :
    print("Luas Permukaan Limas")

if pilihan == "8" :
    print("Luas Permukaan Limas")
    

