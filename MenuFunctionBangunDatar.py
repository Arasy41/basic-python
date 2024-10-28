def bangundatar():
    print("1. Luas Persegi Panjang")
    print("2. Keliling Persegi Panjang")
    print("3. Panjang Persegi Panjang")
    print("4. Lebar Persegi Panjang")
    print("5. Luas Segitiga")
    print("6. Keliling Segitiga")
    print("7. Alas Segitiga")
    print("8. Tinggi Segitiga")
    print("9. End Program")


bangundatar()
pilihan = input("Pilih Menu: ")
while pilihan !="9" :
    if pilihan == "1" :
       print("Luas Persegi Panjang")
       panjang = input("Masukkan panjang : ")
       lebar = input("Masukkan lebar : ")
       luas = float(panjang) * float(lebar)
       print("Luas persegi panjang adalah", luas, "cm")
    if pilihan == "2" :
       print("Keliling Persegi Panjang")
       panjang = input("Masukkan panjang : " )
       lebar = input("Masukkan lebar: ")
       keliling = 2 * (float(panjang) + float(lebar))
       print ("Keliling persegi panjang adalah", keliling,"cm")
    if pilihan == "3" :
       print("Panjang Persegi Panjang")
       luas = float(input("Masukkan Nilai Luas : "))
       lebar = float(input("Masukkan Lebar : "))
       panjang = float(luas) / float(lebar) 
       print(" Panjang Persegi Panjang adalah", panjang, "cm")
    if pilihan == "4" :
       print("Lebar Persegi Panjang") 
       luas = float(input("Masukkan Nilai Luas : "))
       panjang = float(input("Masukkan Panjang : "))
       lebar = float(luas) / float(panjang)
       print("Lebar Persegi Panjang adalah", lebar, "cm")
    if pilihan == "5" :
       print("Luas Segitiga")
       alas = float(input("Masukkan Alas : "))
       tinggi = float(input("Masukkan Tinggi : "))
       luas = float(alas) * float(tinggi) /2
       print("Luas Segitiga adalah", luas, "cm")
    if pilihan == "6" :
       print("Keliling Segitiga")
       Sisi_1 = float(input("Masukkan sisi ke 1 : ")) 
       Sisi_2 = float(input("Masukkan sisi ke 2 : "))
       Sisi_3 = float(input("Masukkan sisi ke 3 : "))
       keliling = float(Sisi_1) + float(Sisi_2) + float(Sisi_3)
       print("Keliling Segitiga adalah", keliling, "cm")
    if pilihan == "7" :
       print("Alas Segitiga")
       luas = float(input("Masukkan Luas Segitiga : "))
       tinggi = float(input("Masukkan Tinggi Segitiga : "))
       alas = float(luas) / float(tinggi) * 2
       print("Alas Segitiga adalah", alas, "cm")
    if pilihan == "8" :
       print("Tinggi Segitiga")
       luas = float(input("Masukkan Luas Segitiga : "))
       alas = float(input("Masukkan Alas Segitiga : "))
       tinggi = float(luas) / float(alas) * 2
       print("Tinggi Segitiga adalah", tinggi, "cm")

    print()
    bangundatar()
    pilihan = (input("Masukkan pilihan: "))
print("Terimakasih telah menggunakan program kami")