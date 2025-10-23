class karyawan :
    def __init__(self, nama, jabatan, gaji : int) :
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji
    
    def tampilkan_info(self) :
        return f"Nama : {self.nama}\n Jabatan = {self.jabatan}\n Gaji = {self.gaji}"
    
    def naikkan_gaji(self, tambah : int) :
        self.gaji += tambah
    
try :
    nama = input("Isikan Nama :")
    jabatan = input("Isikan Jabatan :")
    gaji = int(input("Isikan Gaji :"))

    karyawan1 = karyawan(nama = nama, gaji = gaji, jabatan = jabatan)
    print(karyawan1.tampilkan_info())
    print("GAJI AWAL")
    print(karyawan1.tampilkan_info())
    print("GAJI SETELAH DITAMBAH")
    karyawan1.naikkan_gaji(200000)
    print(karyawan1.gaji)

except ValueError :
    print("Nilai gaji harus berupa angka")