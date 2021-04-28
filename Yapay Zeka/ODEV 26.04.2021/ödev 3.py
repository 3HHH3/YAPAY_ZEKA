"""
Hasan Hüseyin Harmancı
205510025 
Mekatronik Prg.

Yapay Zeka
26.04.2021

3.) [2, 4, 6, 6, 8, 2, 12, 54, 15] gibi.  listedeki elemanlari 
tekrarlamadan yazan fonksiyonu kullanarak yeni bir liste olusturun."""

# set () kullanarak
# yinelenenleri listeden kaldırma


# liste
test_list = [2, 4, 6, 6, 8, 2, 12, 54, 15]
print("Orijinal liste : " + str(test_list))

# set() fonk kullanarak yinelenen sayıları kaldırıyoz.
test_list = list(set(test_list))

# Kaldırıldıktan sonra ekrana değerleri basıyoruz.
print("Yinelenenleri kaldırdıktan sonraki liste : " + str(test_list))