# Deklarasi Class
class Siswa:
    # Atribut Class (sama untuk semua objek)
    sekolah = "SMK PGRI 35 Solokanjeruk"

    # Konstruktor (__init__)
    def __init__(self, nama, nis, kelas):
        self.nama = nama
        self.nis = nis
        self.kelas = kelas

    # Method untuk menampilkan profil siswa
    def tampilkan_profil_siswa(self):
        print(f"Nama Siswa : {self.nama}")
        print(f"NIS        : {self.nis}")
        print(f"Kelas      : {self.kelas}")
        print(f"Sekolah    : {Siswa.sekolah}")

# Membuat beberapa objek siswa
s1 = Siswa("Imas Julia nengsih", 112233, "XI RPL 3")

# Menampilkan profil masing-masing siswa
s1.tampilkan_profil_siswa()