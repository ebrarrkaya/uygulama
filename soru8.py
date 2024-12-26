elma=50
portakal=30
muz=20
while True:
    print("Elma stoku: {}".format(elma))
    print("Portakal stoku: {}".format(portakal))
    print("Muz stoku: {}".format(muz))
    sec = input("Lütfen satın almak istediğiniz ürünü giriniz (Elma, Portakal, Muz). Çıkmak için 'x' tuşuna basın: ")

    if sec=='x':
        print("Çıkılıyor...")
        break
    
    if sec== 'Elma':
        es=int(input("Satın almak istediğiniz elma sayısını giriniz: "))
        if es <= elma:
            elma-=es 
            print("Yeni Elma stoku: {}".format(elma))
        else:
            print("Yetersiz stok! Elma stok miktarı: {}".format(elma))

    elif sec=='Portakal':
        es=int(input("Satın almak istediğiniz portakal sayısını giriniz: "))
        if es<=portakal:
            portakal-=es 
            print("Yeni Portakal stoku: {}".format(portakal))
        else:
            print("Yetersiz stok! Portakal stok miktarı: {}".format(portakal))

    elif sec=='Muz':
        es=int(input("Satın almak istediğiniz muz sayısını giriniz: "))
        if es<=muz:
            muz-=es
            print("Yeni Muz stoku: {}".format(muz))
        else:
            print("Yetersiz stok! Muz stok miktarı: {}".format(muz))

    else:
        print("Geçersiz ürün seçimi! Lütfen Elma, Portakal veya Muz giriniz.")
