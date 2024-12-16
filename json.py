#verileri depolamak ve değiştirmek için kullanılan söz dizimi , taşınabilen veri depolama söz dizimi
import json

x = '{"isim": "onur", "yas": 30, "sehir": "tekirdag"}'
y = json.loads(x)

print(y["yas"])
print(y)


