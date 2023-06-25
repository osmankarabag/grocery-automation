import csv

ürünler = []

def ürünleri_yükle():
    try:
        with open('ürünler.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                ürünler.append(row)
    except FileNotFoundError:
        print("Ürünler dosyası bulunamadı.")
    except Exception as e:
        print("Ürünleri yüklerken bir hata oluştu:", str(e))

def ürünleri_kaydet(ürünler):
    try:
        with open('ürünler.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in ürünler:
                writer.writerow(row)
    except Exception as e:
        print("Ürünleri kaydederken bir hata oluştu:", str(e))

def ana_menu():
    ürünleri_yükle()

    while True:
        print("\n--- ANA MENÜ ---")
        print("1. Ürün Ekle")
        print("2. Ürün Güncelle")
        print("3. Ürün Ara")
        print("4. Ürün Sil")
        print("5. Veresiye Borç Hesapla")
        print("6. Aylık Geliri Hesapla")
        print("7. Çıkış")

        secim = input("Bir seçenek girin (1-7): ")

        if secim == "1":
            urun_ekle()
        elif secim == "2":
            urun_guncelle()
        elif secim == "3":
            urun_ara()
        elif secim == "4":
            urun_sil()
        elif secim == "5":
            veresiye_borc_hesapla()
        elif secim == "6":
            aylik_gelir_hesapla()
        elif secim == "7":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek!")

    ürünleri_kaydet(ürünler)

def urun_ekle():
    try:
        barkod = input("Ürün Barkod No: ")
        urun_adi = input("Ürün Adı: ")
        musteri_adi = input("Müşteri Adı: ")

        # Ürün ekleme işlemleri
        yeni_urun = [barkod, urun_adi, musteri_adi]
        ürünler.append(yeni_urun)

        print("Ürün başarıyla eklendi!")
    except Exception as e:
        print("Ürün eklerken bir hata oluştu:", str(e))

def urun_guncelle():
    try:
        barkod = input("Güncellenecek Ürün Barkod No: ")

        # Ürün güncelleme işlemleri
        for urun in ürünler:
            if urun[0] == barkod:
                yeni_urun_adi = input("Yeni Ürün Adı: ")
                yeni_musteri_adi = input("Yeni Müşteri Adı: ")
                urun[1] = yeni_urun_adi
                urun[2] = yeni_musteri_adi
                print("Ürün başarıyla güncellendi!")
                return

        print("Güncellenecek ürün bulunamadı.")
    except Exception as e:
        print("Ürün güncellerken bir hata oluştu:", str(e))

def urun_ara():
    try:
        barkod = input("Aranacak Ürün Barkod No: ")

        # Ürün arama işlemleri
        for urun in ürünler:
            if urun[0] == barkod:
                print("Ürün bulundu!")
                print("Ürün Adı:", urun[1])
                print("Müşteri Adı:", urun[2])
                return

        print("Aranan ürün bulunamadı.")
    except Exception as e:
        print("Ürün ararken bir hata oluştu:", str(e))

def urun_sil():
    try:
        barkod = input("Silinecek Ürün Barkod No: ")

        # Ürün silme işlemleri
        for urun in ürünler:
            if urun[0] == barkod:
                ürünler.remove(urun)
                print("Ürün başarıyla silindi!")
                return

        print("Silinecek ürün bulunamadı.")
    except Exception as e:
        print("Ürün silerken bir hata oluştu:", str(e))

def veresiye_borc_hesapla():
    try:
        # CSV dosyasını oku ve verileri al
        with open('veresiye.csv', 'r') as file:
            reader = csv.reader(file)
            veresiye_borclari = list(reader)

        # Veresiye borçlarını hesapla
        toplam_borc = 0
        for borc in veresiye_borclari:
            toplam_borc += float(borc[1])

        print("Toplam Veresiye Borcu:", toplam_borc)
    except FileNotFoundError:
        print("Veresiye dosyası bulunamadı.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))

def aylik_gelir_hesapla():
    try:
        # CSV dosyasını oku ve verileri al
        with open('gelir.csv', 'r') as file:
            reader = csv.reader(file)
            gelir_verileri = list(reader)

        # Aylık geliri hesapla
        aylık_gelir = 0
        for gelir in gelir_verileri:
            aylık_gelir += float(gelir[1])

        print("Aylık Gelir:", aylık_gelir)
    except FileNotFoundError:
        print("Gelir dosyası bulunamadı.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))

def bakkal_otomasyonu():
    print("Bakkal Otomasyonu")
    ana_menu()

bakkal_otomasyonu()
