def menu():
    print ("Menu Pilihan")
    print ("1. Segitiga")
    print ("2. Lingkaran")
    print ("3. Trapesium")
    print ("4. Jajargenjang")
    print ("5. Bola")
    print ("6. Kerucut")

def segitiga ():
                t = input("Masukkan tinggi segitiga : ")
                a = input("Masukkan alas segitiga : ")
                l = int(a) * int(t) * 1/2
                print (" Jadi luas segitiga adalah : ", l) 
                print ("Terima Kasih")

def lingkaran () :
                r = input("Masukkan jari - jari lingkaran : ")
                l = 3.14 * r * r
                print (" Jadi luas lingkaran adalah : "), l
                print ("Terima Kasih")

def trapesium () :
                t = input("Masukkan tinggi : ")
                j = input("Masukkan jumlah sisi sejajar : ")
                l = t * j / 2
                print (" Jadi luas trapesium adalah : "), l
                print ("Terima Kasih")

def jajargenjang () :
                t = input("Masukkan tinggi segitiga : ")
                a = input("Masukkan alas segitiga : ")
                l = a * t
                print (" Jadi luas jajargenjang adalah : "), l
                print ("Terima Kasih")

def bola () :
                r = input("Masukkan jari - jari : ")
                l = 4 * 3.14 * r * r
                print (" Jadi luas bola adalah : "), l
                print ("Terima Kasih")

def kerucut () :
                t = input("Masukkan tinggi segitiganya : ")
                r = input("Masukkan jari - jari alasnya : ")
                l = ( 3.14 *r ) * ( t * r )
                print (" Jadi luas kerucut adalah : "), l
                print ("Terima Kasih")

#Program Utama
print ("Selamat Datang di Program Untuk MenghitungLuas")
print ("-----------------------------------------------")
menu()
pilih = int(input("Masukkan pilihan : "))

if pilih == 1:
    segitiga()
elif pilih == 2:
    lingkaran()
elif pilih == 3:
    trapesium()
elif pilih == 4:
    jajargenjang()
elif pilih == 5:
    bola()
elif pilih == 6:
    kerucut()
else :
    print ("Ngantuk mas broooo")