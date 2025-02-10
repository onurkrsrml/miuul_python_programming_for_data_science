###############################################
# Python Alıştırmalar
###############################################
from os.path import split

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)


l = [1, 2, 3, 4,"String",3.2, False]
type(l)
# Sıralıdır
# Kapsayıcıdır
# Değiştirilebilir

d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d)
# Değiştirilebilir
# Kapsayıcı
# Sırasız
# Key değerleri farklı olacak

t = ("Machine Learning", "Data Science")
type(d)
# Değiştirilemez
# Kapsayıcı
# Sıralı

s = {"Python", "Machine Learning", "Data Science","Python"}
type(s)
# set([1,2,3]) => set içerisinde iterable aldığı için [] verilir
# Değiştirilebilir
# Sırasız + Eşsiz
# Kapsayıcı


###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."

# YÖNTEM 1
new_text = text.upper()
new_text = new_text.replace(",", " ")
new_text = new_text.replace(".", " ")
new_text.split()

# YÖNTEM 2
text.upper().replace(",", " ").replace(".", " ").split()

# YÖNTEM Onur
text = text.upper()
text = text.replace(",", " ")
text = text.replace(".", " ")
text = text.split()


###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]


# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)


# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.

# YÖNTEM 1
lst[0]
lst[10]

# YÖNTEM 2
idx = [0, 10]
[lst[i] for i in idx]


# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
data = lst[0:4]
data


# Adım 4: Sekizinci index'teki elemanı silin.
lst.pop(8)
lst

# Bonus: .pop() sildiği elemanı çıktı olarak verir, bunu kaydedebiliriz.
a = lst.pop(8)
a
lst

# YÖNTEM 2
del lst[8]
lst

# YÖNTEM 3
lst.remove("N")  # remove: ilk gördüğü karakteri kaldırır
lst

lst.remove("A")
lst



# Adım 5: Yeni bir eleman ekleyin.
lst.append("Onur")
lst.append(101)

# # BONUS - EK BİLGİ
# # Başka bir ekleme yöntemi
lst.append(["a", "b", "c"])
print(lst)
lst.extend(["a", "b", "c"])
print(lst)


# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

# YÖNTEM 1
lst[8] = "N"

# YÖNTEM 2
lst.insert(8, "N")
lst


# # # # DİKKAT-KOPYALARKEN .copy() kullanmayı unutmayalım!!! # # # #
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
new_lst = lst
lst
del new_lst[0]
new_lst
lst

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
new_lst = lst.copy()
lst
del new_lst[0]
new_lst
lst


###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.
dict.keys()


# Adım 2: Value'lara erişiniz.
dict.values()


# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

# YÖNTEM 1
dict['Daisy'][1] = 13
dict

# YÖNTEM 2
dict.update({"Daisy":[dict['Daisy'][0],13]})
dict

# YÖNTEM 3
dict.update({"Daisy": ["England", 13]})
dict

# YÖNTEM 4
dict["Daisy"] = ["England", 13]
dict

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

# YÖNTEM 1
dict.update({"Ahmet": ["Turkey", 24]})
dict

# YÖNTEM 2
# NOT => Eğer key yoksa dict bunu oluşturur
dict["Ahmet"] = ["Turkey", 24]
dict


# Adım 5: Antonio'yu dictionary'den siliniz.

# YÖNTEM 1
dict.pop("Antonio")
dict

# YÖNTEM 2
del dict["Antonio"]
dict


# # DİKKAT-KOPYALARKEN .copy() kullanmayı unutmayalım!!!
# d_new = d
# d
# d_new
# d.pop("Daisy")
# d
# d_new
#
# # .copy()
# d_new = d.copy()
# d
# d_new
# d.pop("Ahmet")
# d
# d_new



###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]

# YÖNTEM 1
def func(lst):
    cift_list = []
    tek_list = []
    for i in lst:
        if i % 2 == 0:
            cift_list.append(i)
        else:
            tek_list.append(i)

    return cift_list, tek_list

cift, tek = func(l)

# LIST COMP. ÇÖZÜMÜ
def func(lst):
    cift_list = [i for i in lst if i % 2 == 0]
    tek_list = [i for i in lst if i % 2 != 0]
    return cift_list, tek_list
cift, tek = func(l)


def func(lst):
    cift_list, tek_list = [i for i in lst if i % 2 == 0], [i for i in lst if i % 2 != 0]
    return cift_list, tek_list
cift, tek = func(l)


def func(lst):
    return [i for i in lst if i % 2 == 0], [i for i in lst if i % 2 != 0]

cift, tek = func(l)


###########################################################################################################################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###########################################################################################################################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

# YÖNTEM 1
for i, ogr in enumerate(ogrenciler):
    if i < 3:
        print(i, ogr, "Mühendislik")
    else:
        print(i, ogr, "Tıp")


##############################################################################################################################################################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
##############################################################################################################################################################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]



##############################################################################################################################################################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
##############################################################################################################################################################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])






