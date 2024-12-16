listem = ["elma", "muz", "kiraz"] 
print(listem) 

listem = ["elma", "muz", "kiraz", "elma", "kiraz"] 
print(listem) 

listem = ["elma", "muz", "kiraz"] 
print(len(listem))   # öğelerin sayısını yazdırır  3


#Liste öğeleri herhangi bir veri türünde olabilir: 
liste1 = ["elma", "muz", "kiraz"]   #dize
liste2 = [1, 5, 7, 9, 3]            #int
liste3 = [True, False, False]       #boolean

#Bir liste farklı veri türleri içerebilir: 
liste1 = ["abc", 28, True, 35, "erkek"] 

listem = ["elma", "muz", "kiraz"] 
print(type(listem)) 


#Yeni bir liste oluştururken list() kurucusunu kullanmak da mümkündür. 
buListe = list(("elma", "muz", "kiraz")) # çift standart parantezlere dikkat edin 
print(buListe)

    #DİZİLER
# Liste, sıralı ve değiştirilebilir bir koleksiyondur. Yinelenen üyelere izin verir. 
# Tuple, sıralı ve değişmez bir koleksiyondur. Yinelenen üyelere izin verir. 
# Set, sırasız, değiştirilemez* ve indekslenmemiş bir koleksiyondur. Çift üye yok. 
# Sözlük, sıralı** ve değiştirilebilir bir koleksiyondur. Çift üye yok. 
#Set öğeleri değiştirilemez, ancak istediğiniz zaman öğeleri kaldırabilir ve/veya ekleyebilirsiniz. 

listem = ["elma", "muz", "kiraz"] 
print(listem[1])  #2. öğe muz

buListe = ["elma", "muz", "kiraz"] 
print(buListe[-1])   #son öğe kiraz

buListe =["elma", "muz", "kiraz", "portakal", "kivi", "kavun", "mango"] 
print(buListe[2:5]) 

buListe = ["elma", "muz", "kiraz", "portakal", "kivi", "kavun", "mango"] 
print(buListe[:4]) 

buListe = ["elma", "muz", "kiraz", "portakal", "kivi", "kavun", "mango"] 
print(buListe [2:])

buListe = ["elma", "muz", "kiraz", "portakal", "kivi", "kavun", "mango"] 
print(buListe [-4:-1])   # -1 dahil değil yani en sondaki öğe yok yazdırılmaz (mango)


buListe = ["elma", "muz", "kiraz"] 
buListe[1] = "frenk üzümü"   # 2.öğeyi yani muzu değiştirdi üstüne yazdı 
print(buListe) 

buListe = ["elma", "muz", "kiraz", "portakal", "kivi", "mango"] 
buListe[1:3] = ["frenk üzümü", "karpuz"]   # muz ve kiraz ın yerine bu iki yeni öğeyi yazdı
print(buListe)

buListe = ["elma", "muz", "kiraz"] 
buListe[1:2] = ["frenk üzümü", "karpuz"]   #muzun yerine 2 öğe eklediğimiz için kiraz ı bir sağa kaydırdık

buListe = ["elma", "muz", "kiraz"] 
buListe[1:3] = ["karpuz"]  # muz ve kirazın yerine karpuz yazdığımız için çıktıda sadece elma ve karpuz yazdı 
print(buListe) 

# 1 öğeye karşılık 1 öğe değişmek zorunda değil, 1 öğenin yerine 2 öğe ekleyebilir, 2 öğe yerine de 1 öğe yazdırabiliriz

# insert öğenin yerini değiştirmez(üstüne yazmaz), direkt listeye öğe ekler ve dizinin uzunluğunu arttırır
buListe = ["elma", "muz", "kiraz"] 
buListe.insert(2, "karpuz")  # listenin 2.öğesine karpuz u ekle diyor
print(buListe) 

buListe = ["elma", "muz", "kiraz"] 
buListe.append("portakal")  # en sona öğe ekler
print(buListe) 


#Geçerli listeye başka bir listeden öğeler eklemek için extension() yöntemini kullanın. 

#Tropikal unsurları bu listeye ekleyin: 
buListe = ["elma", "muz", "kiraz"] 
tropikal = ["mango", "ananas", "papaya"] 
buListe.extend(tropikal) 
print(buListe)

buListe = ["elma", "muz", "kiraz"] 
buTuple = ["kivi", "portakal"] 
buListe.extend(buTuple) 
print(buListe)

buListe = ["elma", "muz", "kiraz"] 
buListe.remove("muz") 
print(buListe) 

buListe = ["elma", "muz", "kiraz"] 
buListe.pop(1)  # 2.öğeyi çıkardı, parantezin içine bir şey yazmazsan en son öğeyi çıkarır
print(buListe) 

buListe = ["elma", "muz", "kiraz"] 
del buListe[0]  # 1.öğeyi tamamen sildi
print(buListe)

buListe = ["elma", "muz", "kiraz"] 
del buListe  #listeyi tamamen sildi

buListe = ["elma", "muz", "kiraz"] 
buListe.clear() #listeyi boşalttı, liste hala duruyor ama içi boş öğeler yok
print(buListe)



buListe = ["elma", "muz", "kiraz"] 
for x in buListe:  # for ile listedeki tüm elemanları dolaştık ve yazdırdık
    print(x) 

buListe = ["Elma", "muz", "kiraz"] 
for i in range(len(buListe)): 
    print(buListe[i]) 

buListe = ["elma", "muz", "kiraz"] 
[print(x) for x in buListe]


buListe = ["Elma", "muz", "kiraz"] 
i = 0 
while i < len(buListe): 
    print(buListe[i]) 
    i = i + 1


meyveler = ["elma", "muz", "kiraz", "kivi", "mango"] 
yeniListe = [x for x in meyveler if "a" in x] 
print(yeniListe) 

yeniListe = [x for x in meyveler if x != "elma"]
print(yeniListe) 

yeniListe = [x for x in range(10)] 
print(yeniListe)  # 10 a kadarki sayıları yaz

yeniListe = [x for x in range(10) if x < 5]
print(yeniListe)  #5ten küçük sayıları yaz

yeniListe = [x.upper() for x in meyveler] 
print(yeniListe)

yeniListe = ['merhaba' for x in meyveler] 
print(yeniListe)

yeniListe = [x if x != "muz" else "portakal" for x in meyveler] 
print(yeniListe)   #eğer muz yoksa muz ekle, varsa yerine portakal ekle


#LİSTELERDE SIRALAMA






