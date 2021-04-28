"""
HASAN HÜSEYİN HARMANCI 
20551025
MEKATRONİK 
22.03.2021

Doğalgaz Faturası

kullanicidan her mevsimden bir ay icin dogal gaz faturasi miktarlarini aliniz. 
Birim fiyati hesaplayiniz. ortalama aylik sarfiyati ve gunluk sarfiyati hesaplayiniz. 
her ayin kac gun oldugunu belirtip, aylik dogalgaz faturalarini hesaplayiniz. 
ekran fotsosuyla odevi gonderiniz.

ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
nisan = haziran = eylül = kasım = 30
şubat = 28 """

aylık_sarfiyat = int(input("Aylık Sarfiyati Giriniz: "))
fatura_tutarı = float(input("Fatura Tutarini Giriniz: "))
ay = int(input("İşlem yapmak istediğiniz Ayın degerini giriniz: "))

birim_fiyat = fatura_tutarı / aylık_sarfiyat
print("\nBirim Fiyatı: ", birim_fiyat)

günlük_sarfiyat = aylık_sarfiyat / ay
print("Günlük sarfiyati: ", günlük_sarfiyat)

aylik = birim_fiyat * günlük_sarfiyat * ay
print("Aylık Doğalgaz Fatura Tutarı: ", aylik)

