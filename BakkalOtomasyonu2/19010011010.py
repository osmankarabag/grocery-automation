import time
print("********************",end=" ")
print("BAKKAL OTOMASYONU",end=" ")
print("********************")
print("")
liste = ["no", "ad_soyad", "telefon_no", "email", "evadres", "borc"]
u_liste = ["barkod","u_ismi","u_alis","u_satis","u_kar"]
barkodlar = []
kisi = dict()
urun = dict()
uzunluk = 0
u_uzunluk = 0
key = []
u_key = []
numara = 0
u_numara = 0
kisi_isimleri = []
urun_isimleri = []
v_giris = []
u_giris = []
satis_no = 1
barkod = dict()
adet_sayisi = 1
toplam_fiyat = 0
islem = 0
veresiye = []
pesin = []
tahsilat = []
borc = []
kar = 0
p_toplam = 0
v_toplam = 0
t_toplam = 0
b_toplam = 0

def sozlukcevir(): # bu fonksiyonda veresiye bilgi dosyasına kaydettiğim kişilerin bilgilerini kişi sözlüğüne aktarıyorum
    global liste
    global key
    bilgi = dict()
    bilgiler_al = []
    temp = None
    global kisi
    global uzunluk
    global kisi_isimleri
    global numara
    global v_giris

    with open("Veresiye bilgi 19010011010.txt","r") as bilgiler:
        kisiler = bilgiler.readlines()
        uzunluk = len(kisiler)

        for j in range(0,len(kisiler)):
            temp = kisiler[j].split()
            bilgiler_al.append(temp[0])

        x = 0

        for i in range(0,len(kisiler)):

            bilgi[liste[x]] = bilgiler_al[i]

            if x == 0: # bu if bloğunda
                numara = bilgiler_al[i]
                key.append(numara)
                v_giris.append(numara)

            x += 1
            if x == 6:
                kisi[numara] = bilgi.copy()
                x = 0
        for s in kisi.keys():
            kisi_isimleri.append(kisi[s][liste[1]])



def urun_sozlukcevir():
    global u_liste
    global u_key
    bilgi = dict()
    bilgiler_al = []
    temp = None
    global urun
    global urun_isimleri
    global u_numara
    global u_giris

    with open("Ürün bilgi 19010011010.txt","r") as bilgiler:
        urunler = bilgiler.readlines()
        uzunluk = len(urunler)

        for j in range(0, len(urunler)):
            temp = urunler[j].split()
            bilgiler_al.append(temp[0])
        x = 0

        for i in range(0,len(urunler)):
            bilgi[u_liste[x]] = bilgiler_al[i]

            if x == 0:
                u_numara = bilgiler_al[i]
                u_key.append(u_numara)
                u_giris.append(u_numara)
            x += 1
            if x == 5:
                urun[u_numara] = bilgi.copy()
                x = 0
        for c in urun.keys():
            urun_isimleri.append(urun[c][u_liste[1]])


def dosyala():
    global kisi
    global liste
    liste1 = ["cari numarasi", "adi soyadi", "telefon numrasi", "e maili", "ev adresi", "borcu"]

    for p in kisi.keys():# bu if bloğunda dosyaya int bir karakter giremediğimiz için int karakterleri str'ye çeviriyoruz
        kisi[p]["no"] = str(kisi[p]["no"])
        kisi[p]["borc"] = str(kisi[p]["borc"])

    with open("Veresiye kayıt 19010011010.txt","a") as veresiye_kayit: # bu dosya listelemek için kulladığım dosya
        for no in kisi.keys():
            veresiye_kayit.write( no + " " + "nolu kisinin bilgileri" + " " + "=>" + "\n" + "\n")

            for a in range(0, len(liste)):
                veresiye_kayit.write("Kişinin" + " " + liste1[a] + " " + "=>" + " " + kisi[no][liste[a]] + "\n")
            veresiye_kayit.write("*********************************" + "\n")

    with open("Veresiye bilgi 19010011010.txt","a") as bilgi:# bu dosya bilgileri tuttuğum dosya
        for no1 in kisi.keys():
            for i in range(0, 6):
                bilgi.write(kisi[no1][liste[i]] + " " + "\n")

def urun_dosyala():
    global urun
    global u_liste

    liste1 = ["barkod numarasi","ismi","alis fiyati","satis fiyati","kari"]

    for p in urun.keys():
        urun[p]["barkod"] = str(urun[p]["barkod"])
        urun[p]["u_alis"] = str(urun[p]["u_alis"])
        urun[p]["u_satis"] = str(urun[p]["u_satis"])
        urun[p]["u_kar"] = str(urun[p]["u_kar"])

    with open("Ürün kayıt 19010011010.txt","a") as urun_kayit:# bu dosya listelemek için kulladığım dosya
        for no in urun.keys():
            urun_kayit.write(( no + " " + "nolu urunun bilgileri" + " " + "=>" + "\n" + "\n"))

            for a in range(0, 5):
                urun_kayit.write("Kisinin" + " " + liste1[a] + " " + "=>" + " " + urun[no][u_liste[a]] + "\n")
            urun_kayit.write("*********************************" + "\n")

    with open("Ürün bilgi 19010011010.txt","a") as bilgi: # bu dosya bilgileri tuttuğum dosya
        for no1 in urun.keys():
            for i in range(0, 5):
                bilgi.write(urun[no1][u_liste[i]] + " " + "\n")

def borc_islemleri():
    global liste
    global tahsilat
    global borc

    numara = input("İşlem yapılacak kişinin numarasını giriniz => ")
    print(" ")

    if numara in key:
        kisi[numara][liste[5]] = float(kisi[numara][liste[5]])

        print("{} kişinin borcu => {}".format(kisi[numara][liste[0]], kisi[numara][liste[5]]))
        print("\nTahsilat işlemi için => 1")
        print("Borç eklemek için => 2")
        secim = 0

        while True:
            try:
                secim = int(input("\nİstediğiniz işlemi seçin => "))
            except ValueError:
                print("Sayı harici bir karakter giremezsiniz")
                continue
            break

        if secim == 1:
            cıkarma = 0
            while True:
                try:
                    cıkarma = float(input("\nTahsilat miktarını girin => "))
                except ValueError:
                    print("Sayı harici bir karakter giremezsiniz")
                    continue
                break
            kisi[numara][liste[5]] = kisi[numara][liste[5]] - cıkarma
            tahsilat.append(cıkarma)
            print("İşlem gerçekleştirilmiştir")
        if secim == 2:
            ekleme = 0
            while True:
                try:
                    ekleme = float(input("\nEklemek istediğiniz miktarı girin => "))
                except ValueError:
                    print("Sayı harici bir karakter giremezsiniz")
                    continue
                break
            kisi[numara][liste[5]] = kisi[numara][liste[5]] + ekleme
            borc.append(ekleme)
            print("İşlem gerçekleştirilmiştir")
        print("\n\nTekrar işlem yapmak için => 1")
        print("Menüye dönmek için => 2")
        g_secim = 0
        while True:
            try:
                g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
            except ValueError:
                print("Sayı harici bir karakter giremezsiniz")
                continue
            break

        if g_secim == 1:
            print("\n" * 25)
            borc_islemleri()

        elif g_secim == 2:
            print("\n" * 25)
            menu()

        else:
            print("Yanlış secim")
            print("\n" * 25)
            menu()

    else:
        print("Aradığınız cari numara bulunamamaktadır\n")
        print("Kişiyi kaydetmek için => 1")
        print("Tekrar işlem yapmak için => 2")
        print("Menüye dönmek için => 3")
        g_secim = 0
        while True:
            try:
                g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
            except ValueError:
                print("Sayı harici bir karakter giremezsiniz")
                continue
            break

        if g_secim == 1:
            print("\n"*25)
            veresiye_kayit()

        elif g_secim == 2:
            print("\n"*25)
            borc_islemleri()

        elif g_secim == 3:
            print("\n"*25)
            menu()
        else:
            print("Yanlış secim")
            print("\n" * 25)
            menu()

def silme():
    global kisi
    global key
    sil = input("Silmek istediğiniz kişinin cari numarsını giriniz => ")
    del kisi[sil]
    key.remove(sil)
    print("\nKişi bilgileri silinmiştir")
    print("\n\nTekrar silme işlem yapmak için => 1")
    print("Menüye dönmek için => 2")
    g_secim = 0
    while True:
        try:
            g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break

    if g_secim == 1:
        print("\n" * 25)
        silme()

    elif g_secim == 2:
        print("\n" * 25)
        menu()

    else:
        print("Yanlış secim")
        print("\n" * 25)
        menu()

def ara():
    global kisi
    global liste
    global key
    liste1 = ["cari numarası", "adı soyadı", "telefon numrası", "e maili", "ev adresi", "borcu"]


    def bul(secim):
        global kisi
        global liste
        global key
        nonlocal liste1
        global numara
        global kisi_isimleri

        if secim == 1:

            isim = input("Aranıcak kişinin ismini ve soyismini tam bir şekilde girin => ")

            for al in kisi.keys(): # isim ile aramak için
                if kisi[al]["ad_soyad"] == isim:
                    print(" ")
                    for i in range(0, 6):
                        print("Kişinin {} => {}".format(liste1[i], kisi[al][liste[i]]))
                    print("\n\nTekrar aramak için => 1")
                    print("Menüye dönmek için => 2")
                    g_secim = 0
                    while True:
                        try:
                            g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
                        except ValueError:
                            print("Sayı harici bir karakter giremezsiniz")
                            continue
                        break

                    if g_secim == 1:
                        print("\n" * 25)
                        ara()

                    elif g_secim == 2:
                        print("\n" * 25)
                        menu()

                    else:
                        print("Yanlış secim")
                        print("\n" * 25)
                        menu()

            if not isim in kisi_isimleri:
                print("Aradığınız kişi bulunamamıştır")
                print("\n\nTekrar aramak için => 1")
                print("Menüye dönmek için => 2")
                g_secim = 0
                while True:
                    try:
                        g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
                    except ValueError:
                        print("Sayı harici bir karakter giremezsiniz")
                        continue
                    break

                if g_secim == 1:
                    print("\n" * 25)
                    ara()

                elif g_secim == 2:
                    print("\n" * 25)
                    menu()

                else:
                    print("Yanlış secim")
                    print("\n" * 25)
                    menu()


        if secim == 2:# numara ile aramak için
            numara = input("Aranıcak kişinin numarasını giriniz => ")
            print(" ")

            if numara in key:
                for i in range(0, 6):
                    print("Kişinin {} => {}".format(liste1[i], kisi[numara][liste[i]]))
                print("\n\nTekrar aramak için => 1")
                print("Menüye dönmek için => 2")
                g_secim = 0
                while True:
                    try:
                        g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
                    except ValueError:
                        print("Sayı harici bir karakter giremezsiniz")
                        continue
                    break

                if g_secim == 1:
                    print("\n" * 25)
                    ara()

                elif g_secim == 2:
                    print("\n" * 25)
                    menu()

                else:
                    print("Yanlış secim")
                    print("\n" * 25)
                    menu()
            else:
                print("Aradığınız cari numara bulunamamaktadır")
                print("\n\nTekrar aramak için => 1")
                print("Menüye dönmek için => 2")
                g_secim = 0
                while True:
                    try:
                        g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
                    except ValueError:
                        print("Sayı harici bir karakter giremezsiniz")
                        continue
                    break

                if g_secim == 1:
                    print("\n" * 25)
                    ara()

                elif g_secim == 2:
                    print("\n" * 25)
                    menu()

                else:
                    print("Yanlış secim")
                    print("\n" * 25)
                    menu()

    print("Kişiyi ismi ile aramak için => 1")
    print("Kişiyi numara ile aramak için => 2")
    secim = 0

    while True:
        try:
            secim = int(input("\nHangi şekilde aramak istersiniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break
    bul(secim)

def guncelle():
    global kisi
    global kisi_isimleri
    numara = 0
    liste1 = ["cari numarası", "adı soyadı", "telefon numrası", "e maili", "ev adresi", "borcu"]

    numara = input("Bilgilerini güncellemek istediğiniz kişinin cari numarasını girin => ")
    kisi.pop(numara)

    bilgi_al = dict()

    # güncellenencek kisinin bilgilerini silip tekrardan aynı cari numara üzerinden aldım

    no = numara
    bilgi_al["no"] = no

    k_adsoyad = input("Kişinin yeni ismi ve soyismini giriniz => ")
    bilgi_al["ad_soyad"] = k_adsoyad
    kisi_isimleri.append(k_adsoyad)

    k_telefon = 0
    while True:
        try:
            k_telefon = int(input("Kişinin yeni telefon numarasını giriniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break
    k_telefon = str(k_telefon)
    bilgi_al["telefon_no"] = k_telefon


    k_email = input("Kişinin yeni email adresi => ")
    bilgi_al["email"] = k_email


    k_evadres = input("Kişinin yeni ev adresi => ")
    bilgi_al["evadres"] = k_evadres


    k_borc = 0
    while True:
        try:
            k_borc = float(input("Kişinin yeni borcununu giriniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break
    k_borc = string = str(k_borc)
    bilgi_al["borc"] = k_borc


    kisi[numara] = bilgi_al.copy()
    print("\n Kişi bilgileri güncellenmiştir")
    print("\n")
    for i in range(0, 6):
        print("Kişinin {} => {}".format(liste1[i], kisi[numara][liste[i]]))

    print("\n\nTekrar işlem yapmak için => 1")
    print("Menüye dönmek için => 2")
    g_secim = 0
    while True:
        try:
            g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break

    if g_secim == 1:
        print("\n" * 25)
        guncelle()

    elif g_secim == 2:
        print("\n" * 25)
        menu()

    else:
        print("Yanlış secim")
        print("\n" * 25)
        menu()

def giris_kontrol(giris,bolum):# bu fonksiyonda girilen cari numara ve barkod numararsının aynı olmaması için kontrol ettim
    global v_giris
    global u_giris
    giris = str(giris)
    if bolum == 0:

        if giris in v_giris:
            print("Bu cari numara başka birisine aittir yeniden giriniz")
            return 0
        else:
            return 1
    if bolum == 1:

        if giris in u_giris:
            print("Bu barkod numarası başka bir ürüne aittir yeniden giriniz")
            return 0
        else:
            return 1

def veresiye_kayit():
    global kisi
    global key
    global v_giris

    v_sayi = 0
    while True:
        try:
            v_sayi = int(input("Kaydedeceğiniz kişi sayısını giriniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break

    bilgi_al = dict()
    for i in range(1,v_sayi + 1):
        while True:
            k_no = 0
            while True:
                try:
                    k_no = int(input("\n\nKişinin cari numarasınını giriniz => "))
                except ValueError:
                    print("Sayı harici bir karakter giremezsiniz")
                    continue
                break
            kontrol = giris_kontrol(k_no,0)
            if kontrol == 0:
                continue
            if kontrol == 1:
                k_no = str(k_no)
                bilgi_al["no"] = k_no
                key.append(k_no)
                v_giris.append(k_no)
                break

        k_adsoyad = input("Kişinin ismi ve soyismini giriniz => ")
        bilgi_al["ad_soyad"] = k_adsoyad
        kisi_isimleri.append(k_adsoyad)

        k_telefon = 0
        while True:
            try:
                k_telefon = int(input("Kişinin telefon numarasını giriniz => "))
            except ValueError:
                print("Sayı harici bir karakter giremezsiniz")
                continue
            break
        k_telefon = str(k_telefon)
        bilgi_al["telefon_no"] = k_telefon


        k_email = input("Kişinin email adresi => ")
        bilgi_al["email"] = k_email


        k_evadres = input("Kişinin ev adresi => ")
        bilgi_al["evadres"] = k_evadres

        k_borc = 0
        while True:
            try:
                k_borc = float(input("Kişinin borcununu giriniz => "))
            except ValueError:
                print("Sayı harici bir karakter giremezsiniz")
                continue
            break
        k_borc = str(k_borc)
        bilgi_al["borc"] = k_borc

        kisi[k_no] = bilgi_al.copy()
    print("\nKişi kayıt adilmiştir")

    print("\n\nTekrar kaydetmek için => 1")
    print("Menüye dönmek için => 2")
    g_secim = 0
    while True:
        try:
            g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break

    if g_secim == 1:
        print("\n" * 25)
        veresiye_kayit()

    elif g_secim == 2:
        print("\n" * 25)
        menu()

    else:
        print("Yanlış secim")
        print("\n" * 25)
        menu()


def veresiye_listele(): # dosyadan yazdırmayı amaçladım
    dosyala()
    with open("Veresiye kayıt 19010011023.txt","r") as yazdır:
        print(yazdır.read())

    print("\n\nMenüye dönmek için => 1")
    g_secim = 0
    while True:
        try:
            g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break

    if g_secim == 1:
        print("\n" * 25)
        menu()

    else:
        print("Yanlış secim")
        print("\n" * 25)
        menu()

def urun_sil():
    global urun
    global u_key

    sil = input("Silmek istediğiniz ürünün barkod numarsını giriniz => ")
    del urun[sil]
    u_key.remove(sil)

    print("\n Ürün silinmiştir")
    print("\n\nTekrar silme işlemi yapmak için => 1")
    print("Menüye dönmek için => 2")
    g_secim = 0
    while True:
        try:
            g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break

    if g_secim == 1:
        print("\n" * 25)
        urun_sil()

    elif g_secim == 2:
        print("\n" * 25)
        menu()

    else:
        print("Yanlış secim")
        print("\n" * 25)
        menu()

def urun_ara():
    global urun
    global u_key
    liste1 = ["barkod numarası","ismi","alış fiyatı","satış fiyatı","karı"]

    def bul(secim):
        global urun
        global u_liste
        global u_key
        nonlocal liste1
        global u_numara
        global kisi_isimleri

        if secim == 1:
            isim = input("\nAranıcak ürünün ismini girin => ")
            for al in urun.keys():
                if urun[al]["u_ismi"] == isim:
                    print("")
                    for i in range(0,5):
                        print("Ürünün {} => {}".format(liste1[i], urun[al][u_liste[i]]))
                    print("\n\nTekrar aramak için => 1")
                    print("Menüye dönmek için => 2")
                    g_secim = 0
                    while True:
                        try:
                            g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
                        except ValueError:
                            print("Sayı harici bir karakter giremezsiniz")
                            continue
                        break

                    if g_secim == 1:
                        print("\n" * 25)
                        urun_ara()

                    elif g_secim == 2:
                        print("\n" * 25)
                        menu()

                    else:
                        print("Yanlış secim")
                        print("\n" * 25)
                        menu()
            if not isim in kisi_isimleri:
                print("Aradığınız ürün bulunamamıştır")
                print("\n\nTekrar aramak için => 1")
                print("Menüye dönmek için => 2")
                g_secim = 0
                while True:
                    try:
                        g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
                    except ValueError:
                        print("Sayı harici bir karakter giremezsiniz")
                        continue
                    break

                if g_secim == 1:
                    print("\n" * 25)
                    urun_ara()

                elif g_secim == 2:
                    print("\n" * 25)
                    menu()

                else:
                    print("Yanlış secim")
                    print("\n" * 25)
                    menu()

        if secim == 2:
            u_numara = input("\nAranıcak ürünün numarasını giriniz => ")
            print("")

            if u_numara in u_key:
                for i in range(0, 5):
                    print("Ürünün {} => {}".format(liste1[i], urun[u_numara][u_liste[i]]))
                print("\n\nTekrar aramak için => 1")
                print("Menüye dönmek için => 2")
                g_secim = 0
                while True:
                    try:
                        g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
                    except ValueError:
                        print("Sayı harici bir karakter giremezsiniz")
                        continue
                    break

                if g_secim == 1:
                    print("\n" * 25)
                    urun_ara()

                elif g_secim == 2:
                    print("\n" * 25)
                    menu()

                else:
                    print("Yanlış secim")
                    print("\n" * 25)
                    menu()
            else:
                print("Aradığınız barkod numarası bulunamamaktadır")
                print("\n\nTekrar aramak için => 1")
                print("Menüye dönmek için => 2")
                g_secim = 0
                while True:
                    try:
                        g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
                    except ValueError:
                        print("Sayı harici bir karakter giremezsiniz")
                        continue
                    break

                if g_secim == 1:
                    print("\n" * 25)
                    urun_ara()

                elif g_secim == 2:
                    print("\n" * 25)
                    menu()

                else:
                    print("Yanlış secim")
                    print("\n" * 25)
                    menu()

    print("Ürünü ismi ile aramak için => 1")
    print("Ürünü barkod numarası ile aramak için => 2")
    secim = 0

    while True:
        try:
            secim = int(input("\nHangi şekilde aramak istersiniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break

    bul(secim)

def urun_guncelle():
    global urun
    global u_numara
    global urun_isimleri
    global u_liste
    liste1 = ["barkod numarası", "ismi", "alış fiyatı", "satış fiyatı", "karı"]

    numara = input("Bilgilerini güncellemek istediğiniz kişinin cari numarasını girin")

    urun.pop(u_numara)

    bilgi_al = dict()

    barkod = u_numara
    bilgi_al["barkod"] = barkod

    u_ismi = input("\n\nÜrün yeni ismini giriniz => ")
    bilgi_al["u_ismi"] = u_ismi
    urun_isimleri.append(u_ismi)

    u_alis = 0
    while True:
        try:
            u_alis = float(input("Ürünün yeni alış fiyatını giriniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break
    u_alis = str(u_alis)
    bilgi_al["u_alis"] = u_alis

    u_satis = 0
    while True:
        try:
            u_satis = float(input("Ürünün yeni satis fiyatını giriniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break
    u_satis = str(u_satis)
    bilgi_al["u_satis"] = u_satis

    u_alis = float(u_alis)
    u_satis = float(u_satis)

    u_kar = u_satis - u_alis
    u_kar = str(u_kar)
    bilgi_al["u_kar"] = u_kar

    urun[u_numara] = bilgi_al.copy()

    print("Ürün bilgileri güncellenmiştir")

    for i in range(0, 5):
        print("Ürünün {} => {}".format(liste1[i], urun[numara][u_liste[i]]))

    print("\n\nTekrar işlem yapmak için => 1")
    print("Menüye dönmek için => 2")
    g_secim = 0
    while True:
        try:
            g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break

    if g_secim == 1:
        print("\n" * 25)
        urun_guncelle()

    elif g_secim == 2:
        print("\n" * 25)
        menu()

    else:
        print("Yanlış secim")
        print("\n" * 25)
        menu()

def urun_kayıt():
    global urun
    global urun_isimleri
    global u_giris
    global u_key

    u_sayi = 0
    while True:
        try:
            u_sayi = int(input("Kaydedeceğiniz ürün sayısını giriniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break
    bilgi_al = dict()

    for i in range(1, u_sayi + 1):
        while True:
            u_barkod = 0
            while True:
                try:
                    u_barkod = int(input("\n\nÜrünün barkod numarasınını giriniz => "))
                except ValueError:
                    print("Sayı harici bir karakter giremezsiniz")
                    continue
                break
            kontrol = giris_kontrol(u_barkod,1)
            if kontrol == 0:
                continue
            if kontrol == 1:
                u_barkod = str(u_barkod)
                bilgi_al["barkod"] = u_barkod
                u_key.append(u_barkod)
                u_giris.append(u_barkod)
                break

        u_ismi = input("Ürün ismini giriniz => ")
        bilgi_al["u_ismi"] = u_ismi
        urun_isimleri.append(u_ismi)

        u_alis = 0
        while True:
            try:
                u_alis= float(input("Ürünün alış fiyatını giriniz => "))
            except ValueError:
                print("Sayı harici bir karakter giremezsiniz")
                continue
            break
        u_alis = str(u_alis)
        bilgi_al["u_alis"] = u_alis

        u_satis = 0
        while True:
            try:
                u_satis = float(input("Ürünün satis fiyatını giriniz => "))
            except ValueError:
                print("Sayı harici bir karakter giremezsiniz")
                continue
            break
        u_satis = str(u_satis)
        bilgi_al["u_satis"] = u_satis

        u_alis = float(u_alis)
        u_satis = float(u_satis)

        u_kar = u_satis - u_alis
        u_kar = str(u_kar)
        bilgi_al["u_kar"] = u_kar

        urun[u_barkod] = bilgi_al.copy()

    print("Ürün kaydedilişmiştir")

    print("\n\nTekrar ürün kaydetmek için => 1")
    print("Menüye dönmek için => 2")
    g_secim = 0
    while True:
        try:
            g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break

    if g_secim == 1:
        print("\n" * 25)
        urun_kayıt()

    elif g_secim == 2:
        print("\n" * 25)
        menu()

    else:
        print("Yanlış secim")
        print("\n" * 25)
        menu()

def urun_listele():

    with open("Ürün kayıt 19010011023.txt","r") as yazdir:
        print(yazdir.read())

    print("\n\nMenüye dönmek için => 1")
    g_secim = 0
    while True:
        try:
            g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break

    if g_secim == 1:
        print("\n" * 25)
        menu()

    else:
        print("Yanlış secim")
        print("\n" * 25)
        menu()

def rapor(): # bu fonsiyon bakkal sahibinin yaptığı satışı raporlıcak
    global barkodlar
    global veresiye
    global urun
    global barkod
    global pesin
    global kar
    global tahsilat
    global v_toplam
    global p_toplam
    global b_toplam
    global t_toplam

    for a in barkodlar:
        urun[a]["u_kar"] = float(urun[a]["u_kar"])
        adet_kontrol(a)

        kar += (urun[a]["u_kar"] * barkod[a]["adet"])

    for b in pesin:
        p_toplam += b

    for c in veresiye:
        v_toplam += c

    for d in tahsilat:
        t_toplam += d

    for e in borc:
        b_toplam += e

    print("Satis raporu => \n")
    print("Peşin satış miktarı toplamı => {}".format(p_toplam))
    print("Veresiye satış miktarı toplamı => {}".format(v_toplam))
    print("Kar miktarı toplamı => {}".format(kar))
    print("Tahsilat miktarı toplamı => {}".format(t_toplam))
    print("Veresiye miktarı toplamı => {}".format(b_toplam))

    print("\n\nMenüye dönmek için => 1")
    g_secim = 0
    while True:
        try:
            g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
        except ValueError:
            print("Sayı harici bir karakter giremezsiniz")
            continue
        break

    if g_secim == 1:
        print("\n" * 25)
        menu()

    else:
        print("Yanlış secim")
        print("\n" * 25)
        menu()

def adet_kontrol(barkod_gir):# bu fonksiyon satış yapılan ürünün adedini tespit ediyor
    global barkod
    global adet_sayisi

    adet = dict()

    adet["adet"] = 1
    barkod[barkod_gir] = adet.copy()

def adet_arttir(barkod_gir):
    global barkod

    barkod[barkod_gir]["adet"] += 1

def satis():
    global satis_no
    global urun
    global barkodlar
    global u_key
    global barkod
    global u_giris
    global adet_sayisi
    global kisi
    global toplam_fiyat
    global islem
    global veresiye
    global pesin

    if islem == 0:
        print("Satış işlem numarası => {} \n".format(satis_no))

    while True:

        barkod_gir = input("Ürün barkodu giriniz => ")

        if barkod_gir == "" :
            for i in barkod.keys():
                barkod[i]["adet"] = 0
                barkodlar.clear()

            print("\n"*25)
            break

        if barkod_gir == "-1":
            sil = input("Satışını silmek istediğiniz ürünün barkodunu giriniz => ")

            barkodlar.remove(sil)
            del barkod[sil]
            print("\n"*25)
            satis()

        if barkod_gir != "" :
            if not barkod_gir in u_giris:
                print("Girdiğiniz barkod numarası kayıtlı değildir")
                satis()

            urun[barkod_gir]["u_satis"] = float(urun[barkod_gir]["u_satis"])

            if barkod_gir in barkodlar:

                print("\n" * 25)

                adet_arttir(barkod_gir)

                for i in barkodlar:
                    print("Ürün  barkodu {} ismi {}   Adedi {}   Fiyatı {} ".format(urun[i]["barkod"],urun[i]["u_ismi"], barkod[i]["adet"],
                                                                        urun[i]["u_satis"] * barkod[i]["adet"]))
                toplam_fiyat += urun[barkod_gir]["u_satis"]

                islem = 1
                print("\nSatışı bitirmek için enter tuşuna basınız \n")
                print("Satış silmek için => -1\n")
                satis()

            else:
                adet_kontrol(barkod_gir)
                barkodlar.append(barkod_gir)

                print("\n" * 25)
                for i in barkodlar:

                    print("Ürün barkodu {}  ismi {}   Adedi {}   Fiyatı {} ".format(urun[i]["barkod"],urun[i]["u_ismi"], barkod[i]["adet"],
                                                                        urun[i]["u_satis"] * barkod[i]["adet"]))

                toplam_fiyat += urun[barkod_gir]["u_satis"]
                print("Toplam Fiyat => {} ".format(toplam_fiyat))
                print("\nSatışı bitirmek için enter tuşuna basınız \n")
                print("Satış silmek için => -1\n")
                islem = 1
                satis()

    while True:

        print("\nPeşin satış için => 1")
        print("Veresiye satış için => 2")
        print("Satış iptali için => 3")
        secim = 0

        while True:
            try:
                secim = int(input("Satış seçeneği giriniz => "))
            except ValueError:
                print("Sayı harici bir karakter giremezsiniz")
                continue
            break

        if secim == 1:
            satis_no += 1
            pesin.append(toplam_fiyat)
            print("Miktar => {}".format(toplam_fiyat))
            print("İşlem başarıyla gerçekleştirilmiştir")

        if secim == 2:
            satis_no += 1
            v_numara = input("Cari numara giriniz => ")

            kisi[v_numara]["borc"] = float(kisi[v_numara]["borc"])
            kisi[v_numara]["borc"] += toplam_fiyat
            veresiye.append(toplam_fiyat)
            print("Miktar => {}".format(toplam_fiyat))
            print("İşlem başarıyla gerçekleştirilmiştir")

        if secim == 3:

            print("Satış işlemi iptal edilmiştir")
            for i in barkod.keys():
                barkod[i]["adet"] = 0
                barkodlar.clear()


        print("\n\nTekrar satis yapmak için => 1")
        print("Menüye dönmek için => 2")
        g_secim = 0
        while True:
            try:
                g_secim = int(input("\nİstediğiniz işlemi seçiniz => "))
            except ValueError:
                print("Sayı harici bir karakter giremezsiniz")
                continue
            break

        if g_secim == 1:
            print("\n" * 25)
            satis()

        elif g_secim == 2:
            print("\n" * 25)
            menu()

        else:
            print("Yanlış secim")
            print("\n" * 25)
            menu()


def menu():
    while True:
        print("***** Bakkal Otomasyonuna hoşgeldiniz *****")
        print("\n Veresiye işlemleri için => 1")
        print("\n Ürün işlemleri için => 2")
        print("\n Satış işlemleri için => 3")
        print("\n Çıkış için => 4")

        secim = 0
        while True:
            try:
                secim = int(input("\nİstediğiniz işlemi seçin => "))
            except ValueError:
                print("Sayı harici bir karakter giremezsiniz")
                continue
            break
        print("\n" * 25)
        if secim == 1:
            print("Kişi kaydetmek için => 1")
            print("Kişileri listelemek için => 2")
            print("Kişi bilgilerini güncellemek veya değiştirmek için => 3")
            print("Kişi aramak için => 4")
            print("Kişi silmek için => 5")
            print("Borç işlemleri için => 6\n")
            k_secim = 0
            while True:
                try:
                    k_secim = int(input("\nİstediğiniz işlemi seçin => "))
                except ValueError:
                    print("Sayı harici bir karakter giremezsiniz")
                    continue
                break

            if k_secim == 1:
                print("\n" * 25)
                veresiye_kayit()

            elif k_secim == 2:
                print("\n" * 25)
                veresiye_listele()

            elif k_secim == 3:
                print("\n" * 25)
                guncelle()

            elif k_secim == 4:
                print("\n" * 25)
                ara()

            elif k_secim == 5:
                 print("\n"*25)
                 silme()

            elif k_secim == 6:
                print("\n" * 25)
                borc_islemleri()

            else:
                print("Yanlış secim")
                print("\n" * 25)
                menu()

        elif secim == 2:
            print("Ürün kaydetmek için => 1")
            print("Ürünleri listelemek için => 2")
            print("Ürün bilgilerini güncellemek veya değiştirmek için => 3")
            print("Ürün aramak için => 4")
            print("Ürün silmek için => 5\n")
            u_secim = 0
            while True:
                try:
                    u_secim = int(input("\nİstediğiniz işlemi seçin => "))
                except ValueError:
                    print("Sayı harici bir karakter giremezsiniz")
                    continue
                break

            if u_secim == 1:
                print("\n" * 25)
                urun_kayıt()

            elif u_secim == 2:
                print("\n" * 25)
                urun_listele()

            elif u_secim == 3:
                print("\n" * 25)
                urun_guncelle()

            elif u_secim == 4:
                print("\n" * 25)
                urun_ara()

            elif u_secim == 5:
                print("\n"*25)
                urun_sil()

            else:
                print("Yanlış secim")
                print("\n"*25)
                menu()

        elif secim == 3:
            print("Satış yapmak için => 1")
            print("Satış raporu almak için => 2")

            s_secim = 0
            while True:
                try:
                    s_secim = int(input("\nİstediğiniz işlemi seçin => "))
                except ValueError:
                    print("Sayı harici bir karakter giremezsiniz")
                    continue
                break

            if s_secim == 1:
                print("\n" * 25)
                satis()

            elif s_secim == 2:
                rapor()
            else:
                print("Yanlış secim")
                print("\n" * 25)
                menu()

        elif secim == 4:
            dosyala()
            urun_dosyala()
            print(kisi)
            print(urun)
            exit(-1)

        else:
            print("Yanlış secim")
            print("\n" * 25)
            menu()


print("\n")
sozlukcevir()
urun_sozlukcevir()
menu()