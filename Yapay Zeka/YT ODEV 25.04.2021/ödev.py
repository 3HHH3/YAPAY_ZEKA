"""
Hasan Hüseyin Harmancı
205510025 
Mekatronik Prg.

Yapay Zeka
25.04.2021

Youtube Ödevi
https://youtu.be/ltRROGJoVYs


#*******************************************************************


1.) friends = ['ahmet','mehmet', 'ebru', 'mahmut', 'ayşe'] 
listesindeki mahmut hariç diğer elemenları while ve for 
loop kullanarak yazdırın

"""

import random
friends = ['ahmet', 'mehmet', 'ebru', 'mahmut', 'ayşe']

x = 0
# x değeri, friends değişkeninin eleman değerinden
# küçük olduğu sürece while dön. çalışacaktır.
while(x < len(friends)):
    friend = friends[x]
    x = x+1
    # Eğer listede mahmut adlı bir kelime rastlarsa
    # continue komutu ile mahmut kelimesini es geçecektir
    # ve geri kalan hepsini ekrana basacaktır.
    if friend == "mahmut":
        continue
    print(friend)


for friend in friends:
    # Eğer listede mahmut adlı bir kelime rastlarsa
    # continue komutu ile mahmut kelimesini es geçecektir
    # ve geri kalan hepsini ekrana basacaktır.
    if friend == "mahmut":
        continue
    print(friend)


# *******************************************************************


"""
2.) Kullanıcı tarafından girilen 2 rakam arasındaki çift sayılaın çıktısını alın
Burda input fonk. ile min ve max sayı değerlerini alıyoruz ve int fonk. 
ile sayıya dönüştürüyoruz ve yanındaki değişkenlere değereini atıyoruz.
"""

minNum = int(input("Lütfen minimum sayısını giriniz: "))
maxNum = int(input("Lütfen maxmum sayısını giriniz: "))


"""Burda ise for döngüsünü, range fonk. ile minNum ve maxNum sayısı 
arasına kadar gidebileceğini bildiriyoruz.
ve her döngüde evenNum değişkeniyle if koşulu işe işleme tabi tutuyoruz

Not: For dön. de maxNum dahil değil. Eğer dahil etmek isteseydik 'maxNum + 1' yazacaktık."""

for evenNum in range(minNum, maxNum):
    # çift sayı olmadığı durumunda continue komutu ile es geçiyoruz o sayıları
    if evenNum % 2 != 0:
        continue
    else:
        print(evenNum)


# *******************************************************************


"""
3.) While döngüsünü kullanarak 1-100 arasında sayı tahminlerini yapabileceğiniz bir program yazın
"""

# burda biz random kütüphaneini dosyamıza dahil ettik.
# burda ise 1- 100 sayıları arasında rastgele bir sayı üretmesini istedik.
xnum = random.randint(1, 100)

num = int(input("Lütfen 1 ile 100 arasında bir sayı girin: "))
"""simdi oluşturduğumuz sayı, daha önce oluşturulan rastegele sayıya 
eşit değilse sürekli tekrar etmesini itiyoruz."""
while num != xnum:
    if num < xnum:  # eğer bilemem gereken rakam yazdığım rakamdan küçükse
        print(f'{num} daha büyük bir sayı girin')
        num = int(input(''))
        # yukarıda daha önce bilgilendirdiğimiz için tekrar içine birşey yazmamıza gerek yok

    else:
        print(f'{num} daha küçük bir sayı girin')
        num = int(input(''))
        # yukarıda daha önce bilgilendirdiğimiz için tekrar içine birşey yazmamıza gerek yok
        # Not: input fonk içini boş bırakırsn hata verir ama içine '' yaparsan hata vermez unutma.

# Eğer aranan sayı bulunduysa ekranımızda bulduğumuz sayıyı basacaktır.
print(f'Tekbikler {num} yakaladınız!')

# *******************************************************************


"""
4.) celciuses = [20, 25, 30, 35] derecelerini kelvin ve fahrenheit 
olarak iki ayrı liste halinde gösterin
K = C + 273
F = C * 9 / 5 + 32
"""

celciuses = [20, 25, 30, 35]
kelvin = []  # burda boş bir kelvin listesi oluşturduk döngünün sonunda içi dolu olacak
# burda boş bir fahrenheit listesi oluşturduk döngünün sonunda içi dolu olacak
fahrenheit = []

"""for dön ile yukarıdaki celciuses değerlerini 
sırasıyla aldık ve 'c' adlı değişkene sırasıyla 
atadık daha sonra döngünün içinde c ile aritmetik 
işlemler yaptık"""
for c in celciuses:
    k = c+273
    # burda ise boş olan kelvin listesini sırasıyla k adlı değişkenin değerlerini atıyor.
    kelvin.append(k)
    f = c*9/5+32
    # burda ise boş olan kelvin listesini sırasıyla k adlı değişkenin değerlerini atıyor.
    fahrenheit.append(f)

print(kelvin)
print(fahrenheit)

"""
Çıktı: 
[293, 298, 303, 308]
[68.0, 77.0, 86.0, 95.0]
"""


# *******************************************************************


"""
5.) Kullanıcılardan bir sayı girişi isteyelim ve o sayı ve öncekilerin toplamını yazalım 

"""
num = int(input("Lütfen bir sayısını giriniz: "))
# eğer yazdığımız sayı 0' dan küçükse ekranımızda negatiftir diye yazdıracak. Değilse 
# elsedeki kodları çalıştıracaktır.
if num < 0:  
    print("Negatif bir sayı girdiniz")
else:
    # burda ise sum adlı değişken olusturduk çünkü sırasıyla toplayacamız değerleri bu değişkene atacaz
    sum = 0  
    # yazdığımız sayı 0' dan büyük olduğu sürece devam edecektir taki negatif sayılara 
    # gelince while döngüden çıkacaktır ve en sonunda tplam değerini ekranımıza gösterecktir.
    while num > 0:  
        # sum adlı değişken her seferinde döngüde dönen rakamı topluyarak gidecektir 
        # ve her seferinde de num adlı değişkeni bir azaltarak gidecektir.
        sum += num
        num -= 1
    print("Toplam sayısı: ", sum)
