data_siswa = ["Kautsar", "Afif", "Aufa", "Kevin", "Adam", "Akhtar"]

def Opsi(): 
    print("[1] Tampilkan List Data Siswa")
    print("[2] Tambahkan Data Siswa")
    print("[3] Hapus Salah Satu Siswa")
    print("[4] Ubah Nama Siswa")
    print("[5] Matikan Program")

Opsi()
data = int(input("Pilih Opsi : "))
while data !=5 :
    if data == 1 :
       for x in data_siswa :
          print(x)
    if data == 2 :
       nama_siswa = input("Tambahkan Nama : ")
       data_siswa.append(nama_siswa)
       print(data_siswa)
    if data == 3 :
       data_siswa.remove(input("Pilih salah satu : "))
       print(data_siswa)
    if data == 4 :
       data_siswa.remove(input("Nama Siswa yang Akan di Ganti : "))
       data_siswa.append(input("Masukkan Nama Siswa yang Baru : "))
       print("Data Siswa telah diubah menjadi : ")
       print(data_siswa)
    else : 
       print("Mohon Coba pilih Opsi yang Benar")


    print()
    Opsi()
    data = int(input("Pilih Opsi : "))
    


