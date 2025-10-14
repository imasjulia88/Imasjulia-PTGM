# Program Kalkulator Sederhana
print("=== Kalkulator Sederhana ===")

# Perulangan utama agar bisa menghitung berulang kali
while True:
    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (×)")
    print("4. Pembagian (÷)")
    print("5. Keluar")

    # Input pilihan operasi
    pilihan = int(input("Masukkan pilihan (1/2/3/4/5): "))

    # Percabangan berdasarkan pilihan
    if pilihan == 5:
        print("Terima kasih telah menggunakan kalkulator. Sampai jumpa!")
        break  # keluar dari perulangan

    # Input dua angka
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == 1:
        hasil = angka1 + angka2
        print(f"Hasil penjumlahan: {hasil}")
    elif pilihan == 2:
        hasil = angka1 - angka2
        print(f"Hasil pengurangan: {hasil}")
    elif pilihan == 3:
        hasil = angka1 * angka2
        print(f"Hasil perkalian: {hasil}")
    elif pilihan == 4:
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"Hasil pembagian: {hasil}")
        else:
            print("Error: Tidak bisa membagi dengan nol!")
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")