import random
from fractions import Fraction

def level_17():
    total_mhs = random.randint(10, 25) * 6
    ikut_esport = total_mhs // 2
    ikut_psm = total_mhs // 3
    ikut_keduanya = random.randint(1, min(ikut_esport, ikut_psm) // 3)

    answer = ikut_esport + ikut_psm - ikut_keduanya
    print(f"17. Kelas Sintara memiliki {total_mhs} mahasiswa. Setengahnya ikut UKM E-Sport,\n"
          f"    sepertiganya ikut UKM PSM, dan {ikut_keduanya} orang ikut keduanya.\n"
          f"    Berapa total mahasiswa yang ikut paling sedikit salah satu UKM?")
    return answer

def level_18():
    harga_buku_asli = random.randint(3, 8) * 1000
    harga_pensil_asli = random.randint(2, 6) * 500
    jml_buku = random.randint(2, 5)
    jml_pensil = random.randint(2, 6)
    total_harga = (jml_buku * harga_buku_asli) + (jml_pensil * harga_pensil_asli)
    total_str = f"{total_harga:,}".replace(",", ".")
    buku_str = f"{harga_buku_asli:,}".replace(",", ".")

    answer = (total_harga - (jml_buku * harga_buku_asli)) / jml_pensil
    answer = f"{int(answer):,}".replace(",", ".")
    print(f"18. Sebuah toko menjual {jml_buku} buku tulis dan {jml_pensil} pensil dengan harga total Rp{total_str}.\n"
          f"    Jika harga sebuah buku tulis Rp{buku_str}, berapakah harga satu pensil?")
    return answer

def level_19():
    x = random.randint(3, 9)
    a = random.randint(2, 4)
    b = random.randint(1, 9)
    op_str = random.choice(["+", "-"])
    
    if op_str == "+":
        y = (a * x) + b
    else:
        y = (a * x) - b

    answer = (x + y) * (x - y)
    print(f"19. Jika x={x} dan y={a}x {op_str} {b}, hitung nilai dari (x+y) * (x-y).")
    return answer

def level_20():
    wa = random.choice([8, 12, 24])
    wb = random.choice([6, 8, 12])
    w_buka = random.randint(2, 4)

    laju_a = Fraction(1, wa)
    laju_b = Fraction(1, wb)
    laju_gabungan = laju_a + laju_b

    answer = laju_gabungan * w_buka
    print(f"20. Tangki air terisi penuh dalam {wa} jam oleh kran A, dan {wb} jam oleh kran B.\n"
          f"    Jika dibuka bersama selama {w_buka} jam, berapa bagian tangki yang terisi?")
    return answer