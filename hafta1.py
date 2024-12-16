
print("hellooo")  

if 5 > 2: 
    print("Beş ikiden büyüktür!")  #girinti (tab boşluğu) yapmak zorundayız

"""üç tirnak da yorum satiri yapmayi sağlaMAZ"""

a = 5
print(type(a))

b= "mafe"
print(type(b))

c=float(3) #şeklinde veri tipini belirterek de yazabiliriz
print(c)   #3.0 şeklinde 

"""
Değişken adı bir harf veya alt çizgi karakteri ile başlamalıdır  
• Değişken adı bir sayı ile başlayamaz 
• Değişken adı yalnızca alfasayısal karakterler ve alt çizgiler içerebilir (A-z, 0-9 ve _ ) 
• Değişken adları büyük/küçük harfe duyarlıdır (yaş, Yaş ve YAŞ üç farklı değişkendir) 

myvar 
my_var  
_my_var 
myVar 
MYVAR 
myvar2 
myVariableName
MyVariableName
my_variable_name 
"""

x, y, z = "Portakal", "Muz", "Kiraz" 
print(x) 
print(y) 
print(z)

meyveler = ["elma", "ananas", "seftali"] 
x, y, z = meyveler 
print(x) 
print(y) 
print(z) 


x = "zeynep"
y = "özdemir"
print(x + " " + y)  # + yerine , de kullanilabilir.  ayrıca farkli veri tiplerinde de , kullanımı sorun olmaz tek bir printte değişkenleri yazdırabiliriz


x = "muhteşem" #global degisken

def fonk(): 
    x = "harika" #yerel degisken sadece fonk içinde ulaşılabilir
    print("Hava " + x) 

fonk ()  #ilk fonksiyonu çağırdık hava harika print edildi

print("Hava " + x)  #bu print ise fonkdaki degiskene ulaşamaz, global degiskene ulaşır ve hava muhteşem çıkar


def fonk(): 
    global x  #fonk içindeki değişken global tanımlayabiliriz ve fonk dışında da ulaşılabilir yaparız
    x = "harika" 
fonk() 
print("Hava " + x) #fonk dışında print yaparak x değişkenine ulaşabiliriz, fonk içinde print etmek zorunda değiliz


x = "muhteşem"  #global
def fonk(): 
    global x  #yerel değişkeni global yaptık
    x = "harika"  #artık buna dışardan ulaşılabilir global oldu
fonk() 
print("Hava " + x) #fonk dışında yapılan bu print önce muhteşemi alır ama sonra değeri değişir ve harika değişkenine ulaşabilir, bu nedenle harika çıkar





