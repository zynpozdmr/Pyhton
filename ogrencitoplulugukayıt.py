class Ogrenci:
    def __init__(self, ad, soyad, numara, bolum, telefonno):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.bolum = bolum
        self.__telefonno = telefonno  # Erişim kısıtlandı

    # Encapsulation
    def get_telefonno(self):
        return self.__telefonno

    def set_telefonno(self, yeni_telefonno):
        self.__telefonno = yeni_telefonno


class GeziToplulugu(Ogrenci):
    def __init__(self, ad, soyad, numara, bolum, telefonno):
        super().__init__(ad, soyad, numara, bolum, telefonno)

    def ogrenci_ekle(self, ogrenci):
        print(f"{ogrenci.ad} {ogrenci.soyad} gezi topluluğuna eklendi ve kartı verildi.")
        super().ogrenci_ekle(ogrenci, "gezi")


class YBSToplulugu(Ogrenci):
    def __init__(self, ad, soyad, numara, bolum, telefonno):
        super().__init__(ad, soyad, numara, bolum, telefonno)

    def ogrenci_ekle(self, ogrenci):
        print(f"{ogrenci.ad} {ogrenci.soyad} YBS topluluğuna eklendi ve rozet takıldı.")
        super().ogrenci_ekle(ogrenci, "ybs")


class YazilimToplulugu(Ogrenci):
    def __init__(self, ad, soyad, numara, bolum, telefonno):
        super().__init__(ad, soyad, numara, bolum, telefonno)

    def ogrenci_ekle(self, ogrenci):
        print(f"{ogrenci.ad} {ogrenci.soyad} yazılım topluluğuna eklendi ve erişim kartı verildi.")
        super().ogrenci_ekle(ogrenci, "yazilim")


class OgrenciToplulugu:
    def __init__(self):
        self.gezi_ogrenciler = []
        self.ybs_ogrenciler = []
        self.yazilim_ogrenciler = []

    def ogrenci_ekle(self, ogrenci, topluluk):
        if topluluk == "gezi":
            self.gezi_ogrenciler.append(ogrenci)
            print(f"{ogrenci.ad} {ogrenci.soyad} {ogrenci.numara} {ogrenci.bolum} {ogrenci.get_telefonno()} gezi öğrenci listesine eklendi.")
        elif topluluk == "ybs":
            self.ybs_ogrenciler.append(ogrenci)
            print(f"{ogrenci.ad} {ogrenci.soyad} {ogrenci.numara} {ogrenci.bolum} {ogrenci.get_telefonno()} YBS öğrenci listesine eklendi.")
        elif topluluk == "yazilim":
            self.yazilim_ogrenciler.append(ogrenci)
            print(f"{ogrenci.ad} {ogrenci.soyad} {ogrenci.numara} {ogrenci.bolum} {ogrenci.get_telefonno()} yazılım öğrenci listesine eklendi.")
        else:
            print("Geçersiz topluluk.")

    def ogrenci_cikar(self, ogrenci, topluluk):
        if topluluk == "gezi":
            if ogrenci in self.gezi_ogrenciler:
                self.gezi_ogrenciler.remove(ogrenci)
                print(f"{ogrenci.ad} {ogrenci.soyad} gezi öğrencisi topluluktan çıkarıldı.")
            else:
                print("Öğrenci listede bulunamadı.")
        elif topluluk == "ybs":
            if ogrenci in self.ybs_ogrenciler:
                self.ybs_ogrenciler.remove(ogrenci)
                print(f"{ogrenci.ad} {ogrenci.soyad} YBS öğrencisi topluluktan çıkarıldı.")
            else:
                print("Öğrenci listede bulunamadı.")
        elif topluluk == "yazilim":
            if ogrenci in self.yazilim_ogrenciler:
                self.yazilim_ogrenciler.remove(ogrenci)
                print(f"{ogrenci.ad} {ogrenci.soyad} yazılım öğrencisi topluluktan çıkarıldı.")
            else:
                print("Öğrenci listede bulunamadı.")
        else:
            print("Geçersiz topluluk.")

    def ogrenci_listele(self, topluluk):
        if topluluk == "gezi":
            ogrenci_listesi = self.gezi_ogrenciler
        elif topluluk == "ybs":
            ogrenci_listesi = self.ybs_ogrenciler
        elif topluluk == "yazilim":
            ogrenci_listesi = self.yazilim_ogrenciler
        else:
            print("Geçersiz topluluk.")
            return ogrenci_listesi

        return ogrenci_listesi


def main():
    topluluk = OgrenciToplulugu()

    while True:
        print("\n1. Öğrenci Ekle")
        print("2. Öğrenci Çıkar")
        print("3. Öğrenci Listele")
        print("4. Çıkış")

        secim = input("Lütfen bir seçim yapınız: ")

        if secim == "1":
            ad = input("Öğrenci adı: ")
            soyad = input("Öğrenci soyadı: ")
            numara = input("Öğrenci numarası: ")
            bolum = input("Öğrenci bölümü: ")
            telefonno = input("Öğrenci Telefon no: ")
            topluluk_secim = input("Öğrenci hangi topluluğa eklenecek (gezi/ybs/yazilim): ")

            if topluluk_secim in ["gezi", "ybs", "yazilim"]:
                ogrenci = Ogrenci(ad, soyad, numara, bolum, telefonno)

                if topluluk_secim == "gezi":
                    topluluk.ogrenci_ekle(ogrenci, "gezi")
                elif topluluk_secim == "ybs":
                    topluluk.ogrenci_ekle(ogrenci, "ybs")
                elif topluluk_secim == "yazilim":
                    topluluk.ogrenci_ekle(ogrenci, "yazilim")
            else:
                print("Geçersiz topluluk.")
        elif secim == "2":
            ad = input("Öğrenci adı: ")
            soyad = input("Öğrenci soyadı: ")
            topluluk_secim = input("Öğrenci hangi topluluktan çıkarılacak (gezi/ybs/yazilim): ")

            if topluluk_secim in ["gezi", "ybs", "yazilim"]:
                topluluk.ogrenci_cikar(ad, soyad, topluluk_secim)
            else:
                print("Geçersiz topluluk.")
        elif secim == "3":
            topluluk_secim = input("Hangi topluluğun öğrencileri listelenecek (gezi/ybs/yazilim): ")
            ogrenciler = topluluk.ogrenci_listele(topluluk_secim)
            if ogrenciler:
                for ogrenci in ogrenciler:
                    print(f"{ogrenci.ad} {ogrenci.soyad} {ogrenci.numara} {ogrenci.bolum} {ogrenci.get_telefonno()}")
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
