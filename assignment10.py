isim = str(input("korona ölüm riskine hoş geldin adın nedir:"))
isim = isim.title().strip()
seçenek = ["yes", "no"]

değişken_1 = str(input("75 yaşından büyükmüsün:"))
değişken_1 = değişken_1.lower().strip()
while değişken_1 not in seçenek :
    print("lütfen yes veya no şeklinde cevaplayınız")
    değişken_1 = input("75 yaşından büyükmüsün:")
    değişken_1 = değişken_1.lower().strip()

if değişken_1 == "yes" :
    X = True
else :
    X = False


değişken_2 = str(input("sigara kullanıyormusunuz:"))
değişken_2 = değişken_2.lower().strip()
while değişken_2 not in seçenek :
    print("lütfen yes veya no şeklinde cevaplayınız")
    değişken_2 = input("sigara kullanıyormusunuz:")
    değişken_2 = değişken_2.lower().strip()

if değişken_2 == "yes" :
    Y = True
else :
    Y = False


değişken_3 = str(input("kronik rahatsızlığın varmı:"))
değişken_3 = değişken_3.lower().strip()
while değişken_3 not in seçenek :
    print("lütfen yes veya no şeklinde cevaplayınız")
    değişken_3 = input("kronik rahatsızlığın varmı:")
    değişken_3 = değişken_3.lower().strip()

if değişken_3 == "yes" :
    Z = True
else :
    Z = False


değişken_4 = str(input("bağışıklık sistemin zayıfmı:"))
değişken_4 = değişken_4.lower().strip()
while değişken_4 not in seçenek :
    print("lütfen yes veya no şeklinde cevaplayınız")
    değişken_4 = input("bağışıklık sistemin zayıfmı:")
    değişken_4 = değişken_4.lower().strip()

if değişken_4 == "yes" :
    T = True
else :
    T = False

print("Vermiş olduğun cevaplar şu şekilde;\n\n75 yaşından büyükmüsün:{}\n\n,\bsigara kullanıyormusunuz:{}\n\n,\bkronik rahatsızlığın varmı:{}\n\n,\bbağışıklık sistemin zayıfmı:{}".format(değişken_1,değişken_2,değişken_3,değişken_4))
print()
if (X and Y) or Z or T :
    print((X and Y) or Z or T)
    print("Merhaba {} korona virüse yakalanmassan iyi edersin. ölüm riskin çok fazla...".format(isim))
else:
    print((X and Y) or Z or T)
    print("Merhaba {} korona virüse yakalanman durumunda ölüm riskin az olarak hesaplandı.".format(isim))

