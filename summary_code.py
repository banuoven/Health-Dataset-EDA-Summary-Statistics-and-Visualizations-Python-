import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def veriyi_oku(dosya_adi):
    veri = pd.read_excel(dosya_adi, engine='openpyxl')
    return veri

def bubble_sort(veri):
    n = 0
    for _ in veri:
        n += 1

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if veri[j] > veri[j + 1]:
                veri[j], veri[j + 1] = veri[j + 1], veri[j]
    return veri


def min(veri):
    min_deger = veri[0]
    for deger in veri[1:]:
        if deger < min_deger:
            min_deger = deger
    return min_deger


def max(veri):
    max_deger = veri[0]
    for deger in veri[1:]:
        if deger > max_deger:
            max_deger = deger
    return max_deger


def aykiri_degerleri_tespit_et(veri, degisken):
    veri_sirali = bubble_sort(veri[degisken].tolist())
    n = 0
    for _ in veri_sirali:
        n += 1

    q1_indeks = (n + 1) * 0.25
    if q1_indeks.is_integer():
        Q1 = veri_sirali[int(q1_indeks) - 1]
    else:
        Q1 = (veri_sirali[int(q1_indeks) - 1] + veri_sirali[int(q1_indeks)]) / 2

    q3_indeks = (n + 1) * 0.75
    if q3_indeks.is_integer():
        Q3 = veri_sirali[int(q3_indeks) - 1]
    else:
        Q3 = (veri_sirali[int(q3_indeks) - 1] + veri_sirali[int(q3_indeks)]) / 2

    IQR = Q3 - Q1
    alt_sinir = Q1 - 1.5 * IQR
    ust_sinir = Q3 + 1.5 * IQR

    aykiri_degerler = veri[(veri[degisken] < alt_sinir) | (veri[degisken] > ust_sinir)]

    return aykiri_degerler, Q1, Q3


def kutu_cizimi(veri, degisken):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=veri, x=degisken)
    plt.title(f'{degisken} Değişkeni İçin Kutu Çizimi')
    plt.show()


def merkezsel_olcumler(veri, degisken, aykiri_degerler, Q1, Q3):
    veri_gecerli = veri[~veri[degisken].isin(aykiri_degerler[degisken])]

    toplam = 0
    n = 0
    for deger in veri_gecerli[degisken]:
        toplam += deger
        n += 1
    ortalama = toplam / n


    veri_sirali = bubble_sort(veri_gecerli[degisken].tolist())
    n = 0
    for _ in veri_sirali:
        n += 1
    if n % 2 == 1:
        ortanca = veri_sirali[n // 2]
    else:
        ortanca = (veri_sirali[(n // 2) - 1] + veri_sirali[n // 2]) / 2


    frekanslar = {}
    for deger in veri_gecerli[degisken]:
        if deger in frekanslar:
            frekanslar[deger] += 1
        else:
            frekanslar[deger] = 1
    max_frekans = 0
    mod = None
    for deger, frekans in frekanslar.items():
        if frekans > max_frekans:
            max_frekans = frekans
            mod = deger

    min_deger = veri_gecerli[degisken].min()

    max_deger = veri_gecerli[degisken].max()

    degisim_araligi = max_deger - min_deger

    toplam_mutlak_fark = 0
    n = 0
    for deger in veri_gecerli[degisken]:
        toplam_mutlak_fark += abs(deger - ortalama)
        n += 1
    ortalama_mutlak_sapma = toplam_mutlak_fark / n


    n = 0
    for _ in veri_gecerli[degisken]:
        n += 1

    toplam = 0
    for deger in veri_gecerli[degisken]:
        toplam += deger
    ortalama = toplam / n

    toplam_kare_fark = 0
    for deger in veri_gecerli[degisken]:
        fark = deger - ortalama
        toplam_kare_fark += fark * fark

    varyans = toplam_kare_fark / (n - 1)
    n = 0
    for _ in veri_gecerli[degisken]:
        n += 1
    toplam = 0
    for deger in veri_gecerli[degisken]:
        toplam += deger
    ortalama = toplam / n

    toplam_kare_fark = 0
    for deger in veri_gecerli[degisken]:
        fark = deger - ortalama
        toplam_kare_fark += fark * fark

    varyans = toplam_kare_fark / (n - 1)

    standart_sapma = varyans ** 0.5

    cikti_katsayisi = standart_sapma / ortalama

    ceyrekler_acikligi = Q3 - Q1

    return {
        "Ortalama": ortalama,
        "Ortanca": ortanca,
        "Mod": mod,
        "Değişim Aralığı": degisim_araligi,
        "Ortalama Mutlak Sapma": ortalama_mutlak_sapma,
        "Varyans": varyans,
        "Standart Sapma": standart_sapma,
        "Değişim Katsayısı": cikti_katsayisi,
        "Çeyrekler Açıklığı": ceyrekler_acikligi
    }

def sonuclari_dosyaya_yaz(sonuclar, dosya_adi):
    with open(dosya_adi, 'w', encoding='utf-8') as f:
        for col, sonuc in sonuclar.items():
            f.write(f"Veri Kumesi: {col}\n")
            f.write(f"Aritmetik Ortalama: {sonuc['Ortalama']}\n")
            f.write(f"Medyan: {sonuc['Ortanca']}\n")
            f.write(f"Mod: {sonuc['Mod']}\n")
            f.write(f"Degisim Araligi: {sonuc['Değişim Aralığı']}\n")
            f.write(f"Varyans: {sonuc['Varyans']}\n")
            f.write(f"Standart Sapma: {sonuc['Standart Sapma']}\n")
            f.write(f"Degisim Katsayisi: {sonuc['Değişim Katsayısı']}\n")
            f.write(f"Ceyrekler Acikligi: {sonuc['Çeyrekler Açıklığı']}\n")
            f.write(f"Ortalama Mutlak Sapma: {sonuc['Ortalama Mutlak Sapma']}\n")
            f.write("\n")



def main(dosya_adi):
    veri = veriyi_oku(dosya_adi)

    sonuclar = {}

    for degisken in veri.select_dtypes(include=[np.number]).columns:
        print(f"{degisken} Değişkeni İçin İşlemler Başlatılıyor...")

        aykiri_degerler, Q1, Q3 = aykiri_degerleri_tespit_et(veri, degisken)

        kutu_cizimi(veri, degisken)

        olcumler = merkezsel_olcumler(veri, degisken, aykiri_degerler, Q1, Q3)

        sonuclar[degisken] = olcumler

        if not aykiri_degerler.empty:
            print(f"{degisken} Aykırı Değerler: \n{aykiri_degerler}\n")
        else:
            print(f"{degisken} için aykırı değer yok.\n")

        print(f"{degisken} Değişkeni İçin Merkezi Eğilim ve Dağılım Ölçümleri:")
        for key, value in olcumler.items():
            print(f"  {key}: {value}")

        print()

    sonuclari_dosyaya_yaz(sonuclar, "sonuc.txt")
    print("Sonuçlar 'sonuc.txt' dosyasına yazıldı.")


dosya_adi = 'veriSeti.xlsx'
main(dosya_adi)