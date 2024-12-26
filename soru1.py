bakiye=500
soru=input("Cikis icin 4, para cekmek icin 1, para yatirmak icin 2, bakiye sorgulama icin 3'e basiniz: ")
while soru==1:
    cekme=int(input("Cekmek istediginiz miktari giriniz: "))
    print("Para cekme basarili! Mevcut bakiye: {}".format(bakiye-cekme))
    bakiye=bakiye-=cekme
    print(soru)
while soru==2:
    yatirma=int(input("Yatirmak istediginiz miktari giriniz: "))
    print("Para yatirma basarili! Mevcut bakiye: {}".format(bakiye+yatirma))
    bakiye=bakiye+=yatirma
    print(soru)
while soru==3:
    print("Mevcut bakiye: {}".format(bakiye))
    print(soru)
while soru==4:
    print("Sistemden cikildi.")