"""
Hasan Hüseyin Harmancı
205510025 
Mekatronik Prg.

Yapay Zeka
26.04.2021

2.) Faktöriyel bulan fonksiyon"""

def fonksiyon(num):# fonksiyon tanımı
    fact=1
    for i in range(1, num+1):#faktöriyel bulmak için for döngüsü 
        fact=fact*i
    return fact    #geri dönüş faktöriyel 
sayı=int(input("Lütfen faktöriyel bulmak için herhangi bir sayı girin: "))
sonuç=fonksiyon(sayı)#işlev çağırın ve değeri değişken sonuca atayın
print("{} sayısını faktöriyeli {}".format(sayı,sonuç))