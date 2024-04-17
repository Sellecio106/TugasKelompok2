import math

def hitung_keliling_bola(jari_jari):
    return 2 * math.pi * jari_jari
def hitung_luas_bola(jari_jari):
    return 4 * math.pi * (jari_jari ** 2)
def hitung_volume_bola(jari_jari):
    return (4/3) * math.pi * (jari_jari ** 3)
def hitung_keliling_kubus(sisi):
    return 12 * sisi
def hitung_luas_kubus(sisi):
    return 6 * (sisi ** 2)
def hitung_volume_kubus(sisi):
    return sisi ** 3
def hitung_keliling_balok(p, l, t):
    return 4 * (p + l + t)
def hitung_luas_balok(p, l, t):
    return 2 * ((p * l) + (l * t) + (p * t))
def hitung_volume_balok(p, l, t):
    return p * l * t

def home():
    print("Selamat datang di web rumus")
    print("Pilihlah Bangun Ruang untuk di hitung : ")
    print("a) bola")
    print("b) kubus")
    print("c) Balok")

    pilihan_utama = input("Masukkan Pilihan (a/b/c) : ")
    
    if pilihan_utama == "a" :
        print("Pilihlah Jenis Perhitungan : ")
        print("1. Keliling")
        print("2. Luas")
        print("3. Volume")
        pilihan_perhitungan = int(input("Masukkan Pilihan (1/2/3) : "))

        if pilihan_perhitungan == 1 :
            print("hitungan keliling")
            jari_jari = float(input("Masukkan jari-jari bola :  "))
            print("keliling bola", hitung_keliling_bola(jari_jari))
        elif pilihan_perhitungan == 2 :
            print("hitungan Luas")
            jari_jari = float(input("Masukkan jari-jari bola : "))
            print("Luas Bola", hitung_luas_bola(jari_jari))
        elif pilihan_perhitungan == 3 :
            print("hitungan volume")
            jari_jari = float(input("Masukkan jari-jari bola : "))
            print("Keliling Bola", hitung_volume_bola(jari_jari))
        else : 
            print("tidak valid")
    elif pilihan_utama == "b" : 
        print(input("Masukkan Jenis Perhitungan : "))
        print("1. Keliling")
        print("2. Luas")
        print("3. Volume")
        pilihan_perhitungan = int(input("Masukkan Pilihan (1/2/3) : "))

        if pilihan_perhitungan == 1 :
            print("hitungan keliling")
            sisi = float(input("Masukkan sisi kubus : "))
            print("Keliling Kubus", hitung_keliling_kubus(sisi))
        elif pilihan_perhitungan == 2 :
            print("hitungan Luas")
            sisi = float(input("Masukkan sisi Kubus : "))
            print("Luas Kubus",hitung_luas_kubus(sisi))
        elif pilihan_perhitungan == 3 :
            print("hitungan volume")
            sisi = float(input("Masukkan sisi Kubus : "))
            print("Volume Kubus", hitung_volume_kubus(sisi))
        else :
            print("tidak valid")
    elif pilihan_utama == "c":
        print(input("Masukkan Jenis Perhitungan : "))
        print("1. Keliling")
        print("2. Luas")
        print("3. Volume")
        pilihan_perhitungan = int(input("Masukkan Pilihan (1/2/3)"))

        if pilihan_perhitungan == 1 :
            print("hitungan keliling")
            p = float(input("Masukkan panjang : "))
            l = float(input("Masukkan lebar : "))
            t = float(input("Masukkan tinggi : "))
            print("Keliling Balok", hitung_keliling_balok(p, l, t))
        elif pilihan_perhitungan == 2 : 
            print("hitungan Luas")
            p = float(input("Masukkan Panjang : "))
            l = float(input("Masukkan Lebar : "))
            t = float(input("Masukkan tinggi : "))
            print("Luas Balok", hitung_luas_balok(p, l, t))
        elif pilihan_perhitungan == 3 : 
            print("hitungan volume")
            p = float(input("Masukkan panjang : "))
            l = float(input("Masukkan lebar : "))
            t = float(input("Masukkan tinggi : "))
            print("Volume Balok", hitung_volume_balok(p, l, t))
        else : 
            print("tidak valid")
    else : 
        print("Pilihan tidak valid")
        
if __name__ == "__main__" : 
    home()
