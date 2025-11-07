total_level_global = 0
nyawa = 5 

def progres_level(kategori, daftar_soal):

    global total_level_global
    global nyawa

    level = 0  
    nyawa = 5  

    print(f"\nKategori: {kategori}")
    print("Soal terdiri dari level 1-20. Jika jawaban salah, nyawa berkurang 1.")
    print(f"Total nyawa: {nyawa}\n")

    while level < len(daftar_soal):
        soal = daftar_soal[level]
        print(f"Level {level+1}: {soal['pertanyaan']}")
        jawaban_user = input("Jawaban Anda: ")

        if jawaban_user.strip() == str(soal['jawaban']):
            print("Benar! Next ke level berikutnya.\n")
            total_level_global += 1
            level += 1
        else:
            nyawa -= 1
            print(f"Salah! Sisa nyawa: {nyawa}\n")
            if nyawa <= 0:
                print("Game Over! Ulang lagi ke level 1.\n")
                level = 0     
                nyawa = 5        