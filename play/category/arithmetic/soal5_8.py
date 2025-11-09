import random

#Ade

def soal_5():
    #pola soal : (a - b) x (c + d)

    a = random.randint(1, 20)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    soal = f"({a} - {b}) x ({c} + {d}) = ..."
    jawaban = int((a - b) * (c + d))

    print (soal)
    return jawaban

def soal_6():
    #pola soal : (a + b) x c(d + e)

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(2, 5)  # Menghindari perkalian dengan 0 atau 1
    d = random.randint(1, 10)
    e = random.randint(1, 10)
    
    soal = f"({a} + {b}) x {c}({d} + {e}) = ..."
    jawaban = (a + b) * c * (d + e)

    print (soal)
    return jawaban

def soal_7():
    #pola soal : x^2 - y^2

    # 'x' lebih besar dari 'y' supaya hasilnya positif
    x = random.randint(2, 12) 
    y = random.randint(1, x - 1) 
    
    soal = f"Jika x={x} dan y={y}, nilai dari (x² - y²) adalah ..."
    jawaban = (x**2) - (y**2)

    print (soal)
    return jawaban

def soal_8():
    #pola soal : a / b * c
    a = random.randint(10, 100)
    b = random.randint(1, 10)  # Menghindari pembagian dengan 0
    c = random.randint(1, 10)

    soal = f"{a} / {b} * {c} = ..."
    jawaban = (a / b) * c

    print (soal)
    return jawaban

