# Fungsi kalkulator sederhana
def kalkulator():
    print("Kalkulator Sederhana")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    # Input pilihan operasi
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    # Input angka
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    # Percabangan untuk menentukan operasi
    if pilihan == '1':
        hasil = angka1 + angka2
        print(f"Hasil Penjumlahan: {hasil}")
    elif pilihan == '2':
        hasil = angka1 - angka2
        print(f"Hasil Pengurangan: {hasil}")
    elif pilihan == '3':
        hasil = angka1 * angka2
        print(f"Hasil Perkalian: {hasil}")
    elif pilihan == '4':
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"Hasil Pembagian: {hasil}")
        else:
            print("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan fungsi kalkulator
kalkulator()