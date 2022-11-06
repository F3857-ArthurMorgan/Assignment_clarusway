#ARTIK YIL SORUSUNUN ÇÖZÜMÜ
yıl = int(input("Artık yıl olup olmadığını öğrenmek istediğin yılı gir : "))
if (yıl % 4 == 0) and (yıl % 100 != 0 or yıl % 400 == 0) :
    print("{} is a leap year ".format(yıl))
else:
    print("{} is not a leap year ".format(yıl))