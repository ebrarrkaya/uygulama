# Başlangıç stokları
elma = 50
portakal = 30
muz = 20

while True:
    # Başlangıç stoklarını ekrana yazdır
    print("\nElma stoku: {}".format(elma))
    print("Portakal stoku: {}".format(portakal))
    print("Muz stoku: {}".format(muz))

    # Kullanıcıdan ürün seçmesini iste
    sec = input("Lütfen satın almak istediğiniz ürünü giriniz (Elma, Portakal, Muz). Çıkmak için 'x' tuşuna basın: ").lower()

    if sec == 'x':  # Çıkmak için 'x' tuşuna basılacak
        print("Çıkılıyor...")
        break
    
    # Ürün seçimine göre stok miktarını kontrol et ve işlem yap
    if sec == 'elma':
        es = int(input("Satın almak istediğiniz elma sayısını giriniz: "))
        if es <= elma:
            elma -= es  # Stoktan azalt
            print("Yeni Elma stoku: {}".format(elma))
        else:
            print("Yetersiz stok! Elma stok miktarı: {}".format(elma))

    elif sec == 'portakal':
        es = int(input("Satın almak istediğiniz portakal sayısını giriniz: "))
        if es <= portakal:
            portakal -= es  # Stoktan azalt
            print("Yeni Portakal stoku: {}".format(portakal))
        else:
            print("Yetersiz stok! Portakal stok miktarı: {}".format(portakal))

    elif sec == 'muz':
        es = int(input("Satın almak istediğiniz muz sayısını giriniz: "))
        if es <= muz:
            muz -= es  # Stoktan azalt
            print("Yeni Muz stoku: {}".format(muz))
        else:
            print("Yetersiz stok! Muz stok miktarı: {}".format(muz))

    else:
        print("Geçersiz ürün seçimi! Lütfen Elma, Portakal veya Muz giriniz.")
