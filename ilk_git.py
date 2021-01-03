import json
from random import randint

class sistemÜyelik():



    def __init__(self):
        self.durum = True
        self.veriler = self.verileriAl()


    def verileriAl(self):
        try:
            with open("kullanicilar.json" , "r" , encoding= "UTF-8") as dosya:
                veriler = json.load(dosya)

        except FileNotFoundError:
            with open("kullanicilar.json" , "w" , encoding= "UTF-8") as dosya:
                dosya.write("{ }")

            with open("kullanicilar.json" , "r" , encoding= "UTF-8") as dosya:
                veriler = json.load(dosya)

        return veriler        



    def menuGöster(self):
        print("""
        
 
    **** DO GOOD BE HAPPY ****


    1- ) GİRİŞ

    2- ) KAYIT OL

    3- ) ÇIKIŞ        
        
        
        
        """)

    def secim(self):
        sec = int(input("LÜTFEN SEÇİMİNİZİ GİRİNİZ: "))
        

        while sec < 1 or sec > 3:
            sec = int(input("YANLIŞ SEÇİM YAPTINIZ LÜTFEN TEKRAR DENEYİNİZ : "))


        return sec


    def calistir(self):
        self.menuGöster()
        secim = self.secim()
        print(secim)

        if secim == 1:
            self.giris()

        if secim == 2:
            self.kayitOl()

        if secim == 3:
            self.kapat()     





    def giris(self):
        username = input("KULLANICI ADI GİRİNİZ: ")
        password = input("ŞİFRE GİRİNİZ: ")


        kayıtKontrol2 = self.konrolEt(username , password)



        if kayıtKontrol2:
            self.girisBasarili()

        else:
            self.girisBasarisiz("BİLGİLER YANLIŞTIR")     


    def kayitOl(self):
        username = str(input("KULLANICI ADI GİRİNİZ: "))
        

        while True:
            sifre = str(input("LÜTFEN ŞİFRE BELİRLEYİNİZ: "))
            sifreKontrol = str(input("ŞİFRENİZİ KONTROL EDİNİZ: "))

            if sifre == sifreKontrol:
                break


            else:
                print("ŞİFRELER UYUŞMUYOR TEKRAR GİRİNİZ: ")

        email = str(input("E - POSTA GİRİNİZ: "))

        kayıtKontrol1 = self.kayitVarmi(username , email)



        if kayıtKontrol1:
            print("BU KULLANICI ADI VEYA E-POSTA SİSTEMDE KAYITLI ")

        else:
            aktivasyoKodu = self.aktivasyonKoduGönder()
            aktivasyonKoduKontronEtmeli = self.aktivasyonKoduKontronEt(aktivasyoKodu)


            if aktivasyonKoduKontronEtmeli:
                self.kaydet(username , sifre , email)    
            else:
                print("AKTİVASYON KODU GEÇERSİZ" )







    def kayitVarmi(self , username , email):
        
        self.veriler = self.verileriAl()
        try:
            for kullanici in self.veriler["kullanicilar"]:
                if kullanici["username"] == username and kullanici["email"] == email: 

                    return True
        except KeyError:
            return False
        return False






    def konrolEt(self , username , password):
        self.veriler = self.verileriAl()


        for kullanıcı in self.veriler["kullanicilar"]:
            if kullanıcı["username"] == username and kullanıcı["sifre"] == password and kullanıcı["timeout"] == "0" and kullanıcı["aktivasyon"] == "Y":

                return True


        return False



    def girisBasarili(self):
        print("HOŞGELDİNİZ")
        self.durum = False


    def girisBasarisiz(self , sebep):
        print(sebep)



    def aktivasyonKoduGönder(self):
        with open("aktivasyonKodu.txt" , "w") as dosya:
            aktivasyon = str(randint(1000,9999))

            dosya.write(aktivasyon)


        return aktivasyon


    def aktivasyonKoduKontronEt(self , aktivasyon):
        aktivasyonKoduAl = input("AKTİVASYON KODUNU GİRİNİZ: ")

        if aktivasyon == aktivasyonKoduAl:
            return True

        else:
            return False


    def kaydet(self , username , sifre ,email ):

        self.veriler = self.verileriAl()


        try:
            self.veriler["kullanicilar"].append({"username" : username , "sifre" : sifre , "email" : email , "aktivasyon" : "Y" , "timeout" : "0" })
        except KeyError:
            self.veriler["kullanicilar"] = {"username" : username , "sifre" : sifre , "email" : email , "aktivasyon" : "Y" , "timeout" : "0"}


        with open("kullanicilar.json" , "w" , encoding = "utf-8" ) as dosya:
            json.dump(obj = self.veriler , fp = dosya , indent=4)
            print("kayıt basarılı")


    def  kapat(self):
        self.durum = False


sistem = sistemÜyelik()
while sistem.durum:
    sistem.calistir()
