from ui_utils import info, line, space, text_left, warning


def chooseCategory():
    while True:
        space()
        text_left("Pilih Kategori Soal:")
        text_left("1. Aljabar Dasar ➗")
        text_left("2. Operasi Berpola 🟰")
        text_left("3. Deret Angka 📏")
        text_left("4. Kembali ke Menu Utama 🔙")
        space()

        choice = input("Pilih opsi (1-4): ")

        if choice == "1":
            info("Kamu memilih kategori Aljabar Dasar.")
            # Tambahkan logika untuk kategori Penjumlahan di sini
        elif choice == "2":
            info("Kamu memilih kategori Operasi Berpola.")
            # Tambahkan logika untuk kategori Pengurangan di sini
        elif choice == "3":
            info("Kamu memilih kategori Deretan Angka.")
            # Tambahkan logika untuk kategori Perkalian di sini
        elif choice == "4":
            info("Kembali ke Menu Utama.")
            line()
            break
        else:
            warning("Opsi tidak valid. Silakan coba lagi.")