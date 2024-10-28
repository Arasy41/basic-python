data_siswa = ["Afief", "Atra", "Dewa", "Akbar", "Sahal", "Damar", "Kukuh", "Kevin", "Noah"]

def pilihan() :
      print("[1] Menampilkan Data Siswa")
      print("[2] Tambah data siswa")
      print("[3] Ubah nama siswa")
      print("[4] Hapus siswa")
      print("[5] End Program")

pilihan()
option = int(input("Masukkan pilihan : "))
while option !=5:
      if option == 1:
            print(data_siswa)
      if option == 2:
            siswa_baru = input("Tambahkan Nama Siswa :")
            data_siswa.append(siswa_baru)
            print(data_siswa)
      if option == 3:
            #data_siswa[int(input("Siswa yang ingin di ganti(Pilih angka 0, 1, 2, 3, 4, 5, 6, 7) : "))] = str(input("Ubah nama siswa : "))
            #print(data_siswa)
            absen = int(input("Masukkkan Absen Siswa yang akan diubah : "))
            print("Absen Siswa yang akan di ubah adalah : ", (absen))
            data_siswa[absen] = input("Ubah Nama Siswa : ")
            print(data_siswa) 
      if option == 4:
            data_siswa.remove(input("Siswa yang akan dihapus : "))
            print(data_siswa)
            
      print()
      pilihan()
      option = int(input("Masukkan pilihan: "))

print("Terimakasih telah menggunakan program kami")