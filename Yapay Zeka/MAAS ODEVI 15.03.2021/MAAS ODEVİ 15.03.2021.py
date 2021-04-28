"""
HASAN HÜSEYİN HARMANCI 
20551025
MEKATRONİK 
15.03.2021

maas odevi
kullanicidan iki kisinin maas bilgileri ve vergi dilimleri bilgisi alinacak. 
buna gore net maas hesaplanip ekrana yazdirilacak
"""

print("Maaş Hesaplamaya hoşgeldiniz\n")
print("*2021 Yılı Gelir Vergisi Tarifesi*\n"
      "24.000 TL’ye kadar	                                                Yüzde 15\n"
      "53.000 TL’nin 24.000 TL’si için 3.600 TL, fazlası	                Yüzde 20\n"
      "190.000 TL’nin 53.000 TL’si için 9.400 TL, fazlası	                Yüzde 27\n"
      "650.000 TL’nin 190.000 TL’si için 46.390 TL, fazlası	                Yüzde 35\n"
      "650.000 TL’den fazlasının 650.000 TL’si için 207.390 TL, fazlası        Yüzde 40")

BrutMaas1 = int(input("\nBirinci Kişinin Maaşını Giriniz: "))
vergi1 = int(input("Birinci Kişinin Vergi Dilimini Giriniz: "))
BrutMaas2 = int(input("\n\nİkinci Kişinin Maaşını Giriniz: "))
vergi2 = int(input("İkinci Kişinin Vergi Dilimini Giriniz: "))

print ("\n\nBirinci Kişinin Net Maaşı: ",BrutMaas1-(BrutMaas1*(vergi1/100)),"TL")
print ("İkincinci Kişinin Net Maaşı: ",BrutMaas2-(BrutMaas2*(vergi2/100)),"TL")