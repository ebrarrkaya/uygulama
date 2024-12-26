butce = int(input("Lütfen bütçe belirleyiniz: "))
while butce > 0:
    kategori = input("Alışveriş kategorisini giriniz: ")
    miktar = int(input("Harcanacak miktarı giriniz: "))
    
    if miktar > butce:
        print("Harcamalarınız bütçenizi aşıyor! Kalan bütçe: {}".format(butce))
        # Eğer harcama bütçeyi aşıyorsa, kullanıcıyı tekrar alışveriş yapmaya davet ediyoruz
        continue
    
    butce -= miktar
    print("{} kategorisinde {} kadar harcama yapıldı. Kalan miktar: {}".format(kategori, miktar, butce))

# Bütçe tükenirse, son mesaj
if butce <= 0:
    print("Bütçeniz tükenmiştir.")
