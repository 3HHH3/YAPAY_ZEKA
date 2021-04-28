"""
Hasan Hüseyin Harmancı
205510025 
Mekatronik Prg.

Yapay Zeka
26.04.2021

1.) python da girilen bir ismin harflerini tersten sıralama


Python'da bir Stringi ters çevirmek için yerleşik bir işlev yoktur.
En hızlı Yol, geriye doğru adım atan bir dilim kullanmaktır '-1'.

Bu özel örnekte, dilim ifadesi [::-1], dizenin sonunda başlar 
ve 0 konumunda biter, adımla hareket -1, negatif bir, 
yani bir adım geri anlamına gelir.
"""

#Bir String'i argüman olarak alan bir fonksiyon oluşturduk
def kelime_fonk(x):
    # Geriye doğru dizgiyi döndür ve Dizenin sonundan başlayarak 
    # dizgiyi kesin ve geriye doğru hareket ettirin.
    return x[::-1]
#Parametre olarak bir dizeyle işlevi çağır
kelime = kelime_fonk("hasan")

#Sonucu yazdır
print(kelime)