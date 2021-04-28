"""
Hasan Hüseyin Harmancı
205510025 
Mekatronik Prg.

Yapay Zeka
22.04.2021

while döngüsünü kullanarak 1’den 100’e kadar olan aralıktaki çift sayıları ekrana yazdırma
"""
a = 0

while a < 100:  # a degeri 100 den küçük olduğu sürece çalışaçaktır
    a += 1  # a değerlerini her döngünde 1 arttıracaktır
    if a % 2 == 0:  # Eğer a değerleri 2 ye bölümünden kalanı 0 'a eşit ise o sayıları ekrana basacaktır.
        print(a)
