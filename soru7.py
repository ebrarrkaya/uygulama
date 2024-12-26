kurslar = []
while True:
    kurs_adı = input("Kurs adını giriniz (Çıkmak için 'x' tuşuna basınız): ")
    if kurs_adı == 'x':
        break
    ders_sayisi = int(input("Ders sayısını giriniz: "))
    katilimci_sayisi = int(input("Katilimci sayısını giriniz: "))
    kurslar = kurslar + ["Kurs Adı: {}, Ders Sayısı: {}, Katılımcı Sayısı: {}".format(kurs_adı,ders_sayisi,katilimci_sayisi)]
print("Kayıtlı Kurslar:")
for kurs in kurslar:
    print(kurs)
