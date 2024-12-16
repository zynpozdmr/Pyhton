a = 5
print(type(a))  #int  (int, sınırsız uzunlukta olabilir)

b=1j           
print(type(b))  #complex (jli ifadeler)

c={"apple","banana","cherry"} #set(dizi)
print(type(c))

d=["watermelon","pineapple"]  #list
print(type(d))

e=("strawberry","bluberry")   #tuple
print(type(e))

f= -55.6465     #float
print(type(f))

g=-6,47          # ,varsa tuple olur  . varsa float olur 
print(type(g))   #tuple

h= 12E4
print(type(h))  #float  ( e veya E  10 anlamına gelir)


print("\n ")

#int ten floata dönüştürme
x=float(a)

#float tan int e dönüştürme
y=int(f)

#int ten complexe dönüştürme
z = complex(a)

print(type(x))
print(type(y))
print(type(z))


print("\n ")

import random
print (random.randrange(1,100))   #rastgele sayı üretiyor



x = int(1) # x 1 olacaktır
y = int(2.8) # y 2 olacaktır
z = int("3") # z 3 olacaktır

print(x, " ", y, " " ,z)

#Üç tırnak (tekli veya ikili) kullanarak bir değişkene çok satırlı bir dize atayabilirsiniz 
a = """Bu bir test verisidir,
Bu bir test verisidir,
Bu bir test verisidir,
Bu bir test verisidir."""
print(a)

#Karakteri 1 konumunda alın (ilk karakterin 0 konumuna sahip olduğunu unutmayın):
a = "Merhaba Dünya!"
print(a[1])         # e harfi yazılır


#"Muz" kelimesindeki harfler arasında dolaşın: x sırayla harfleri gezdi
for x in "muz":
    print(x)


#len() işlevi, bir dizenin uzunluğunu döndürür:
a = "Merhaba Dünya!"
print(len(a))


#Bir dizede belirli bir kelime öbeği veya karakterin olup olmadığını kontrol etmek için in
#anahtar kelimesini kullanabiliriz.Aşağıdaki metinde "ücretsiz" ifadesinin olup olmadığını kontrol edin:
txt = "Hayattaki en iyi şey özgür olmaktır!"
print("özgür" in txt)

#Yalnızca "özgür" varsa yazdırın:
txt = " Hayattaki en iyi şey özgür olmaktır!"
if " özgür" in txt:
    print("Evet, 'özgür' metin içerisinde vardır.")


#Aşağıdaki metinde "pahalı" ifadesinin OLMADIĞINI kontrol edin:
txt = "Orta raflardaki ürünlerden ikincisi bedava!"
print("pahalı" not in txt)

#yalnızca "pahalı" YOKSA yazdırın:
txt = " Orta raflardaki ürünlerden ikincisi bedava!"
if "pahalı" not in txt:
 print("Hayır, pahalı metin içerisinde yoktur.")


 #2. konumdan 5. konuma kadar olan karakterleri alın (5. konum dahil değildir):
b = "Merhaba Bandırma!"
print(b[2:5])

#Karakterleri başlangıçtan 5 konumuna getirin (dahil değildir):
b = "Merhaba Bandırma!"
print(b[:5])

#Karakterleri 2. konumdan sonuna kadar alın:
b = "Merhaba Bandırma!"
print(b[2:])


#Dizenin sonundan dilimi başlatmak için negatif dizinleri kullanın:

#Nereden: "Bandırma! " içinde "ı" (konum -5)  
#sondan başla. sağdan başlayınca 0dan başlamıyor -1 -2 -3 diye saymaya başla -5 ıharfine denk gelir
# Nereye: ancak "Bandırma! " içinde "a" (konum -2) dahil değildir
b = "Merhaba Bandırma!"
print(b[-5:-2]) 



#upper() metodu, dizeyi büyük harfle döndürür:
a = "Merhaba Trakya!"
print(a.upper())


#lower() metodu, dizeyi küçük harfle döndürür:
a = "Merhaba Trakya!"
print(a.lower())


#Boşluk, asıl metinden önceki ve/veya sonraki boşluktur ve çoğu zaman bu boşluğu kaldırmak istersiniz.
#strip() yöntemi, başlangıçtaki veya sondaki tüm boşlukları kaldırır:
a = " Merhaba Trakya! "
print(a.strip()) # returns "Hello, World!"


#replace() yöntemi, bir dizeyi başka bir dizeyle değiştirir:
a = "Merhaba Trakya!"
print(a.replace("M", "N"))


#split() yöntemi, belirtilen ayırıcı arasındaki metnin liste öğeleri haline geldiği bir liste döndürür.
#split() yöntemi, ayırıcının örneklerini bulursa dizeyi alt dizelere böler:
a = "Merhaba, Tekirdağ!"
print(a.split(","))


#İki dizeyi birleştirmek veya birleştirmek için + operatörünü kullanabilirsiniz.
#a değişkenini b değişkeniyle c değişkeniyle birleştirin:
a = "Merhaba"
b = "Çerkezköy"
c = a + b 
# c = a + " " + b       ortaya boşluk bırakmak için
print(c)


Yas = 28
txt = "Benim adım İpek, yaşım: " + str(Yas)
print(txt)


#Dizelere sayılar eklemek için format() yöntemini kullanın (yer tutucu)
yas = 28,56
txt = "Benim adım İpek, yaşım: {}"
print(txt.format(yas))


#Bağımsız değişkenlerin doğru yer tutuculara yerleştirildiğinden emin olmak için {0} dizin numaralarını kullanabilirsiniz:

miktar = 3
itemno = 567
fiyat = 49.95
siparisim = "{1} numaralı üründen {0} adet için {2} TL ödemeliyim."
print(siparisim.format(miktar, itemno, fiyat))

# KAÇIŞ KARAKTERLERİ 
#\' Single Quote 
#\\ Backslash 
#\n New Line 
#\r Carriage Return 
#\t Tab 
#\b Backspace 
#\f Form Feed 
#\ooo Octal value 
#\xhh Hex value """
# örnek,  mesela burda \ \ kullanmazsak " " içinde " " old için hata alırdık bu hatayı engellemk için kaçış karakteri kullandık
txt = "Biz toplumda \"Yazılım Mühendisi\" olarak biliniriz." 
print(txt)

print(10 > 9)    #true
print(10 == 9)   #false
print(10 < 9)    #false

a = 200 
b = 33 
if b > a: 
    print("b değeri a’dan büyüktür") 
else: 
    print("b değeri a’dan büyük değildir") 

    


























