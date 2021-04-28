"""
HASAN HÜSEYİN HARMANCI 
20551025
MEKATRONİK 
22.03.2021

print ozellikleri Ödev
derste ogrendigimiz print ozelliklerinin hepsini kendi yazmis 
oldugunuz kendinizi veya yasadiginiz yeri anlattiginiz kodunuzda kullaniniz.
parametreler   sep, end, file, flush, *
"""
f = open("hasanhuseyinharmanci.txt", "w")
print("Hasan", "Huseyin", "Harmanci", sep=" ", file=f, end="...\n",flush=True)
print("Konya", "Etliekmek", "Mevlana", sep=", ", file=f, end="...\n",flush=True)
print("42", "Konya Spor", "Mevlana Turbesi", sep=", ", file=f, end=" vb.\n", flush=True)
print("25", "06", "2001", sep=".", file=f, flush=True)
print("C++", "Python'dan ustundur", sep=", ", file=f, end=".",flush=True)
f.close()
