
########################################################################################################################
########################################################################################################################
###############################<<<<<< PYTHON PROGRAMMING FOR DATA SCIENCE >>>>>>########################################
########################################################################################################################
########################################################################################################################

# 1 - ÇALIŞMA ORTAMI AYARLARI
# 2 - VERİ YAPILARI
# 3.1 - FONKSİYONLAR
# 3.2 - KOŞULLAR VE DÖNGÜLER
# 3.3 - COMPREHENSIONS
# 4.1 - PYTHON İLE VERİ ANALİZİ: NUMPY
# 4.2 - PYTHON İLE VERİ ANALİZİ: PANDAS
# 4.3 - PYTHON İLE VERİ ANALİZİ: VERİ GÖRSELLEŞTİRME
# 4.4 - PYTHON İLE VERİ ANALİZİ: GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ
# 5 - MÜLAKAT SORULARI
# 6 - CASE STUDY



########################################################################################################################
# 1 - ÇALIŞMA ORTAMI AYARLARI
########################################################################################################################


###############################################
# Sayılar (Numbers) ve Karakter Dizileri (Strings)
###############################################

print(9) #integer
print(9.2) #float

type("Mrb")


###############################################
# Atamalar ve Değişkenler (Assignments and Variables)
###############################################

a = 9

b = "Onur"

c = 10

d = a - c


###############################################
# Virtual Environment (Sanal Ortam)
###############################################

# Sanal ortamların listelenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create –n myenv

# Sanal ortamı aktif etme:
# conda activate myenv

# Sanal ortam silme:
# conda env remove -n myenv


###############################################
# Paket Yönetimi (Package Management)
###############################################

# pip paket yönetim aracı
# pip: pypi (python package index)

# Paket yükleme:
# conda install numpy

# Aynı anda birden fazla paket yükleme:
# conda install numpy scipy pandas

# Paket silme:
# conda remove package_name

# Belirli bir versiyona göre paket yükleme:
# conda install numpy=1.20.1

# Paket yükseltme:
# conda upgrade numpy

# Tüm paketlerin yükseltilmesi:
# conda update --all
# conda upgrade --all

# Yüklü paketlerin listelenmesi:
# conda list

# Paketlerin tümünü aktarma:
# conda env export > environment.yaml/.yml
# pip env export > requirement.txt

# Paketleri dosyadan sanal ortama yükleme:
# conda env create -f environment.yaml

# uv paket yönetim aracı
# uv: universal viewer, dosya görüntüleyici
# uv self update # uv kendini güncelleme
# uv init example # uv proje başlatma
# uv add ruff # uv ruff paketini ekleme
# uv lock # uv paketleri kilitleme/sürüm sabitleme
# uv sync # uv paketleri senkronize etme
# uv pip compile requirements.txt # uv pip gereksinimlerini derleme
# uv venv # uv sanal ortam oluşturma
# echo 'import requests; print(requests.get("https://astral.sh"))' > example.py # örnek python dosyası oluşturma
# uv add --script example.py requests # uv requests paketini örnek python dosyasına ekleme

# rm -rf example/ # örnek proje klasörünü silme
# uv run ruff check . # uv ruff paketini çalıştırma
# uv run ruff --fix . # uv ruff paketini otomatik düzeltme ile çalıştırma
# uv list # uv yüklü paketleri listeleme
# uv install package_name # uv paket yükleme
# uv uninstall package_name # uv paket kaldırma
# uv update --all # uv tüm paketleri güncelleme
# uv upgrade --all # uv tüm paketleri yükseltme





########################################################################################################################
# 2 - VERİ YAPILARI
########################################################################################################################

###############################################
# VERİ YAPILARI (DATA STRUCTURES)
###############################################

# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - String Metodları (String Methods)
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set


###############################################
# Veri Yapılarına Giriş ve Hızlı Özet
###############################################

# Sayılar: integer
x = 46
type(x)

# Sayılar: float
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String
x = "Hello ai era"
type(x)

# Boolean
True
False
type(True)
5 == 4
3 == 2
1 == 1
type(3 == 2)

# Liste
x = ["btc", "eth", "xrp"]
type(x)
print(x[1])

# Sözlük (dictionary)
# x = {"key":"value"}
x = {"name": "Peter", "Age": 36}
type(x)
print(x["Age"])

# Tuple
x = ("python", "ml", "ds")
type(x)
print(x[1])

# Set
x = {"python", "ml", "ds"}
type(x)

# Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.


###############################################
# Sayılar (Numbers): int, float, complex
###############################################

a = 5
b = 10.5

a * 3
a / 7
a * b / 10
a ** 2


# Tipleri değiştirmek
#____________________

int(b)
float(a)

int(a * b / 10)

c = a * b / 10

int(c)


###############################################
# Karakter Dizileri (Strings)
###############################################

print("John")
print('John')

"John"
name = "John"
name = 'John'


# Çok Satırlı Karakter Dizileri
#______________________________

# 3 tırnak arasına yazıldıklarında birden çok satırlı str değişkeni elde edilir
"""Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""

long_str = """Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""


# Karakter Dizilerinin Elemanlarına Erişmek
#__________________________________________

# index ler 0 dan başlar bu sebeple ilk indexi yazdırmak için name[0]
name
name[0]
name[3]
name[2]


# Karakter Dizilerinde Slice İşlemi
#__________________________________

# böl anlamına da gelen birden fazla index i seçmek için, [0:2] de 2 sayılmaz 0,1 inci index yazdırılır
name[0:2]
long_str[0:10]


# String İçerisinde Karakter Sorgulamak
#______________________________________

long_str

"veri" in long_str
# python da key sensitive var harf büyük ise yazılır
"Veri" in long_str

"bool" in long_str


###############################################
# String Metodları (String Methods)
###############################################

# method lara erişmek için kullanılır
dir(str)
dir(int)


# len: boyut bilgisi
#___________________

#len method u bir gömülü fonksiyondur, str lere uygulanabilir. karakter boyut/uzunluk bilgisi verir

name = "john"
type(name)
type(len) #builtin_function_or_method

len(name)
len("onurkarasurmeli")
len("miuul")

### !!! Eğer bir fonksiyon class yapısı içinde tanımlandı ise "method", değil ise "function" dur !!!


# upper() & lower(): küçük-büyük dönüşümleri
#___________________________________________

# girilen str büyük karakter dizilerine dönüştürdü
"miuul".upper()
# girilen str küçük karakter dizilerine dönüştürdü
"MIUUL".lower()

# type(upper)
# type(upper())


# replace: karakter değiştirir
#_____________________________

hi = "Hello AI Era"
hi.replace("l", "p")


# split: böler
#_____________

# bir değer girilmez ise ön tanımlı değer yani boşluk böler
"Hello AI Era".split()


# strip: kırpar
#______________

" ofofo ".strip()
"ofofo".strip("o")


# capitalize: ilk harfi büyütür
#______________________________

"foo".capitalize()

dir("foo")

"foo".startswith("f")


###############################################
# Boolean (True - False): bool
###############################################

# Boolean veri tipi iki değerden birini alabilir: True (doğru) veya False (yanlış).

type(True)
type(False)
5 == 4 # False
1 == 1 # True
3 == 2 # False
type(3 == 2) # bool

###############################################
# Liste (List)
###############################################

# - Değiştirilebilir
# - Sıralıdır ve Index işlemleri yapılabilir
# - Kapsayıcıdır

notes = [1, 2, 3, 4]
type(notes)
names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]
type(not_nam)

not_nam[0]
not_nam[5]
not_nam[6]

# liste içerisindeki liste elemanına erişme
#__________________________________________

not_nam[6][1]

type(not_nam[6])
type(not_nam[5])

type(not_nam[6][1])

notes[0] = 99

not_nam[0:4]


# Liste Metodları (List Methods)
#_______________________________

dir(notes)

# append: eleman ekler

notes.append(100) # liste sonuna eleman eklendi


# pop: indexe göre siler

notes.pop(0) # girilen index teki değer listeden silindi


# insert: indexe ekler

notes.insert(2, 99) # girilen  index teki değer yerine yeni değer eklendi


###########################################################
# Sözlük (Dictonary)
###########################################################

# Değiştirilebilir
# Sırasız (3.7 sonra sıralı oldu)
# Kapsayıcı

# key-value
# dic = {key: value} dictionary dir. key ve value değerleri vardır.
# key ler unique olmalıdır.
# key ler değiştirilemez olmalıdır. (immutable)
# value ler değiştirilebilir.
# key ler sadece string ve sayısal ifadeler olabilir.
# value herhangi bir veri tipi olabilir.

# bu yapıda yani süslü parantez ile tanımlamalara bir diğer örnek set yapısıdır.
# set yapısıda süslü parantez ile tanımlanır fakat set yapısında key-value yapısı yoktur.
# bu konudaki en basit fark set lerde value değeri yoktur : nokta ifadesi yoktur.
# set yapısında sadece key ler vardır ve key ler unique olmalıdır.
# set yapısında key ler değiştirilemez olmalıdır. (immutable)
# set yapısında key ler sadece string ve sayısal ifadeler olabilir.
# set yapısında value herhangi bir veri tipi olabilir.
# set yapısında key ler sırasızdır.

dictionary = {"REG": "Regression",
              "LOJ": "Logistic Regression",
              "CART": "Classification and Regrassion Trees"}

dictionary["REG"]

dictionary = {"REG": 10,
              "LOJ": 20,
              "CART": 30}

dictionary = {"REG": ["RMSE", 10],
              "LOJ": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary["CART"][1]

dict = {"key": "value"}
type(dict)

x = {"name": "Peter", "Age": 36}
type(x)
print(x["Age"])


# Key Sorgulama
#______________

"YSA" in dictionary


# Key'e Göre Value'ya Erişmek
#____________________________

dictionary["REG"]
dictionary.get("REG")


# Value Değiştirmek
#__________________

dictionary["REG"] = ["YSA", 10]


# Tüm Key'lere Erişmek
#_____________________

# dil içerisine tanımladığımız veri yapısının adını girersek ya da tipini ifade eden
# kısaltmayı girersek bu veri yapısına uygun olan metodları görebiliriz.
dictionary.keys()


# Tüm Value'lara Erişmek
#_______________________

dictionary.values()

# Tüm Çiftleri Tuple Halinde Listeye Çevirme
#___________________________________________

# key ve value değerlerini tuple yapısına çevirir ve liste içerisine atar
dictionary.items()


# Key-Value Değerini Güncellemek
#_______________________________

dictionary.update({"REG": 11})


# Yeni Key-Value Eklemek
#_______________________

# eğer ki girilen key değeri dictionary içerisinde yok ise yeni key-value ekler, var ise günceller
dictionary.update({"RF": 10})


###########################################################
# Demet (Tuple)
###########################################################

# - Değiştirilemez
# - Sıralıdır
# - Kapsayıcıdır

# zaman zaman değiştirilemez bir veri yapısı kullanmak istediğimizde tuple yapısını kullanırız

t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

t[0] = 99

# tuple içerisindeki elemanları değiştirmek için önce listeye çevirip değişiklik yapılır sonra tekrar tuple yapısına çevrilir
t = list(t)
t[0] = 99
t = tuple(t)
type(t)


###########################################################
# Set
###########################################################

# - Değiştirilebilir
# - Sırasız ve Eşsizdir
# - Kapsayıcıdır


# difference(): İki kümenin farkı
#________________________________

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar.
set1.difference(set2)
set1 - set2

# set2'de olup set1'de olmayanlar.
set2.difference(set1)
set2 - set1


# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
#___________________________________________________________________

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)


# intersection(): İki kümenin kesişimi
#_____________________________________

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

# alternatif olarak & işareti de kesişim elemanlarını bulmak için kullanılabilir
set1 & set2



# union(): İki kümenin birleşimi
#_______________________________

set1.union(set2)
set2.union(set1)



# isdisjoint(): İki kümenin kesişimi boş mu?
#___________________________________________

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1) == False and print("Kesişim var")


# isdisjoint(): Bir küme diğer kümenin alt kümesi mi?
#____________________________________________________

set1.issubset(set2)
set2.issubset(set1)


# issuperset(): Bir küme diğer kümeyi kapsıyor mu?
#_________________________________________________

set2.issuperset(set1)
set1.issuperset(set2)





########################################################################################################################
# 3.1 - FONKSİYONLAR
########################################################################################################################

# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comprehesions


###############################################
# FONKSİYONLAR (FUNCTIONS)
###############################################

# Fonksiyon Okuryazarlığı
#________________________

# Parametre de argüman da tanımlama için doğrudur.
# Parametre, fonksiyon tanımlaması esnasında ifade edilen değişkenlerdir.
# Argüman ise fonksiyon çağrılırken gönderilen değerlerdir.
# Yaygın kullanımı ise argüman olarak adlandırma eğilimindedir.

print("a", "b")

print("a", "b", sep="__")


# Fonksiyon Tanımlama
#________________________

# Fonksiyonlar, belirli bir işlevi yerine getiren kod bloklarıdır.
# Fonksiyon tanımlama işlemi def anahtar kelimesi ile başlar.
# Fonksiyon adı, parantez içerisine alınır.
# Parantez içerisinde parametreler tanımlanabilir.
# Parametreler opsiyoneldir.
# Fonksiyonun işlevi iki nokta üst üste (:) ile belirtilir.
# Fonksiyonun işlevi blok yapısı içerisinde tanımlanır.
# Fonksiyonun işlevi sonlandırılırken bir alt satıra geçilir.
# Fonksiyonun işlevi sonlandırıldığında geri dönüş değeri belirtilmezse None döner.
# Fonksiyonun işlevi sonlandırıldığında geri dönüş değeri belirtilirse return anahtar kelimesi ile belirtilir.

# Parametresiz bir fonksiyon tanımlayalım.
# Fonksiyonun üzerinde 2 boşluk bırakmak pep8 standartlarına uymak için önemlidir.
def hello_world():
    print("Hello World")


hello_world()


# Parametreli bir fonksiyon tanımlayalım.
def calculate(x):
    print(x * 2)


calculate(5)


# fonk return ile döndürülen değeri döndürür.
def calculate2(x):
    return x * 2


print(calculate2(5))


# İki argümanlı/parametreli bir fonksiyon tanımlayalım.
def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)

summer(8, 7)

summer(arg2=8, arg1=7)


# Argümanların yeri ve kullanım sırası önemlidir. Çağrıldığı sırada sırasıyla tanımlanmalıdır.
# Argümanların sırası değiştirilerek çağrılmak istendiği takdirde adı ile çağrılmalıdır.


# Docstring
#________________________

def summer1(arg1, arg2):
    print(arg1 + arg2)


summer1(7, 9)


def summer(arg1, arg2):
    # Aşağıdaki docstring, fonksiyonun ne işe yaradığını açıklar. Ve burada google docstring standartları kullanılmıştır.
    """
    Sum of two numbers
    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float

    Examples:
        summer(1, 3)

    Notes:
        This function is used to sum two numbers.

    """

    # Aşağıda numpy docstring standartları kullanılmıştır.
    """
    Sum of two numbers
    Parameters/Args
    ----------
        arg1 : int, float # First number to be summed
        arg2 : int, float # Second number to be summed

    Returns
    -------
        int, float # Sum of two numbers
    """

    print(arg1 + arg2)


summer(1, 3)


# Fonksiyonların Statement/Body Bölümü
#________________________

# def function_name(parameters/arguments):
#     statements (function body)

def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")


say_hi()


def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")


say_hi("miuul")


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)

# girilen değerleri bir liste içinde saklayacak fonksiyon.
list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)
    # Gövde(body) kısmı local scope/etki alanı dır. Bu local liğin tanımı : işareti ile başlar.
    # Geçici değişkenlerdir ve sağ alttaki bölümde görüntülenmez, orası global scope dur.


add_element(1, 8)
add_element(18, 8)
add_element(180, 10)


# !!!!!!!! Biz list_store u atamadık ama append method u direkt olarak list_store a atadı ama nasıl?
# Kullandığımız bazı method lar yeniden atama işlemi yapmaya gerek kalmaksızın ilgili veri yapısında
# kalıcı değişiklikler yapabilirler. !!!!!!!!!

# Bütün çalışma içerisinden erişilebilen değişkenlere global scope/etki alanındaki değişkenler denir.
# Global scope/etki alanındaki değişkenlerin tanımı = işareti ile başlar.
# Sadece fonksiyonlar içerisinde tanımlanan değişkenler local scope/etki alanındadır.
# Local scope/etki alanındaki değişkenler fonksiyonun çalıştığı süre boyunca geçerlidir.


# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
#________________________

def divide(a, b):
    print(a / b)


divide(1, 2)


# Eğer bir argümanın ön tanımlı bir değeri varsa, bu argüman fonksiyon çağrılırken belirtilmeyebilir.
# Bu duruma ön tanımlı argüman denir
def divide(a, b=1):
    print(a / b)


divide(10)


def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")


say_hi()
say_hi("mrb")
# Yukarıdaki iki tanımlama da aynı işlemi yapar. Eğer argüman belirtilmezse ön tanımlı argüman çalışır.
# Eğer ön tanımlı argüman belirtilirse belirtilen argüman çalışır.
# Ama ön tanımlı argüman olmasına rağmen argüman belirtilirse belirtilen argüman çalışır!!!!!


# Ne Zaman Fonksiyon Yazma İhtiyacımız Olur?
#________________________

# - Kod tekrarını önlemek
# Elimizde akıllı sokak lambalarının ısı, nem ve şarj değerlerini tutan bir veri yapısı olsun.
# varm, moisture, charge

(56 + 15) / 80
(17 + 45) / 70
(52 + 45) / 80


# Bu hesaplamaları sürekli manuel olarak yapmamak için bir fonksiyon yazabiliriz.
# Bu kendini tekrar etmeme prensibinin adı DRY (Don't Repeat Yourself) prensibidir.
# DRY

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(98, 12, 78)
calculate(17, 45, 70)
calculate(52, 45, 80)


# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
#________________________

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


# calculate(98, 12, 78) * 10

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


calculate(98, 12, 78) * 10

a = calculate(98, 12, 78)


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output


calculate(98, 12, 78)

type(calculate(98, 12, 78))

varma, moisturea, chargea, outputa = calculate(98, 12, 78)


# vukarıdaki işlem sayesinde biz bu değerleri sonrasında kullanmak üzere hafıza da tutmuş olduk.
# bir fonk çıktısını kullanmak istiyorsak return kullanmalıyız.
# daha önceki örneklerde yalnızca print kullandık ve çıktıyı daha sonra kullanamadık.
# yalnızca bir çıktısı olan yerlerde tekli tanımlama yapıyorduk fakat bu işlemde 4 çıktımız vardı.
# bu yüzden 4 çıktıyı da tek tek tanımlamamız gerekti.


# Fonksiyon İçerisinden Fonksiyon Çağırmak
#________________________

def calculate(varm, moisture, charge):
    # çıktımızın int olması için aşağıdaki gibi bir işlem yapabiliriz.
    return int((varm + moisture) / charge)


calculate(90, 12, 12) * 10


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)


# !!!!!!!!!! YENİ BİR FONKSİYON TANIMLIYORUZ VE İÇERİSİNDE ÖNCEDEN TANIMLANMIŞ FONKSİYONLARI ÇAĞIRIYORUZ.
# ÇAĞIRMIŞ OLDUĞUMUZ FONKSİYONLARIN ARGÜMANLARINI DA BU TANIMLADIĞIMIZ ANA FONKSİYONDAN BİÇİMLENDİRMEK İSTİYORUZ.
# BU DURUMDA ANA FONKSİYONU TANIMLARKEN MİSAFİR EDECEĞİ FONKSİYONLARIN ARGÜMANLARINI DA TANIMLAMAMIZ GEREKİR. !!!!!!!!!!

def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


# !!!!!!!!!!! Burada calculate fonksiyonu içerisindeki çıktıyı a değişkenine atadık,
# ve bu a değişkenini standardization fonksiyonundaki argümanlar içerisine koyduk.
# Şöyle ki ANA Fonksiyonumuzu standardization fonksiyonu argümanlarından yalnızca p ile biçimlendirme yapacağımızdan dolayı
# ANA Fonksiyona p yi tanımlamamız yeterli olacaktır. !!!!!!!!!!
# Dışarıdan biçimlendirmek istediğimiz değerlerin argümanlarını ANA Fonksiyona tanımlamamız yeterli olacaktır. a' yı diğer
# fonksiyondan alıp ANA Fonksiyonun içerisinde kullanacağız bu sebeple ANA Fonksiyona tanımlamadık. !!!!!!!!!!

all_calculation(1, 3, 5, 12)


# Bu örnekte ise calculate fonksiyonunu standardization fonksiyonunun içerisinde a değişkeni olarak kullanmayacağız.
# Bu sebeple ANA Fonksiyonumuzda a değişkenini tanımlamamız gerekmektedir.
# Ayrıca fonksiyonu çalıştırmak istediğimizde bu sefer 5 değer girmemiz gerekir çünkü artık 5 argümanımız vardır.
def all_calculation(varm, moisture, charge, a, p):
    print(calculate(varm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 19, 12)


# Lokal & Global Değişkenler (Local & Global Variables)
#________________________

list_store = [1, 2]


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 9)
# Local etki alanındaki değişkenler fonksiyonun çalıştığı süre boyunca geçerlidir.
# Global etki alanındaki değişkenler ise bütün çalışma içerisinden erişilebilen değişkenlerdir.
# Buna rağmen local etki alanındaki değişkenler global etki alanını değiştirebilir.





########################################################################################################################
# 3.2 - KOŞULLAR VE DÖNGÜLER
########################################################################################################################







########################################################################################################################
# 3.3 - COMPREHENSIONS
########################################################################################################################







########################################################################################################################
# 4.1 - PYTHON İLE VERİ ANALİZİ: NUMPY
########################################################################################################################







########################################################################################################################
# 4.2 - PYTHON İLE VERİ ANALİZİ: PANDAS
########################################################################################################################







#########################################################################################################################
# 4.3 - PYTHON İLE VERİ ANALİZİ: VERİ GÖRSELLEŞTİRME
########################################################################################################################







########################################################################################################################
# 4.4 - PYTHON İLE VERİ ANALİZİ: GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ
########################################################################################################################







########################################################################################################################
# 5 - MÜLAKAT SORULARI
########################################################################################################################







########################################################################################################################
# 6 - CASE STUDY
########################################################################################################################











########################################################################################################################
# !!!!!!************************************************* DİKKAT *************************************************!!!!!!

# loc iloc önemli. loc kullanım %99

# unique, dtype, value.count(), drop

# polars araştır

# veri yapılarını iyi tanımak hataları çözmeyi kolaylaştırır

# pd ifadesine command/ctrl basarak aynı anda tıkla ve pd.read_csv yazdığında pandas'ın içindeki fonksiyonları görebilirsin.
# command + f sonra read_ arat sonra kullanabileceğin fonk görünüyor.
# seçmi olduğun fonk üzerine tıkla + command/ctrl ile fonk içine girer

# df.info() fonksiyonu ile veri seti hakkında bilgi alabiliriz. Veri setindeki sütunların isimleri, veri tipleri ve bellek
# kullanımı hakkında bilgi verir.
# df.describe() fonksiyonu ile veri seti hakkında istatistiksel bilgilere ulaşabiliriz. Veri setindeki sayısal sütunlar
# için ortalama, standart sapma, min, max, çeyreklikler gibi bilgileri verir.

# df.isnull().values #(pandas series) eksik gözlemler numpy array türü. Pandas df' de .values kullanıldığında numpy array'e dönüşür

# df.describe().T # betimsel istatistikler (özet istatistikler). T: transpozunu alır. Sütunları satırlara çevirir. Sütunlar artık satırlar olur.

# df.select_dtypes(include=["object"]).columns # object veri tipindeki sütunları seçer

# df["sex"].value_counts() # kategorik değişkenin sınıflarına erişmek

# inplace=True # değişiklikleri kalıcı yapar
# axis=0 satır, axis=1 sütun
#

#                  ----------ARALARINDAKİ FARKLAR------------
# numpy            ---       pandas series                ---       pandas dataframe
# tek boyutlu      ---       tek boyutlu                  ---       çok boyutlu
# vektör           ---       sütun                        ---       tablo
# sadece sayısal   ---       hem sayısal hem kategorik    ---       hem sayısal hem kategorik


# type(df["age"].head()) # pandas series / tek köşeli parantez
# type(df[["age"]].head()) # pandas dataframe / çift köşeli parantez


# df = df.reset_index() # değişikliği kalıcı hale getirmek


# df.loc[:, ~df.columns.str.contains("age")].head()
# loc seçim işlemi için
# [:] bütün satırlar
# ~ tilda işareti değili/zıttı demek
# columns.str kolonlarda string operasyonu
# contains stringlere uygulanan bir metod. Verilen str ifadenin kendisinden önceki str de var olup olmadığını kontrol eder

# | pipe işareti ya da anlamına gelir

# .value_counts() sınıfları ve frekansları

# pivot table ın ön tanım değeri mean(ortalama) dir

# aggfunc = "std" # standard sapma
# aggfunc = "count" sayisi
#agg({"sex": "count"}) cinsiyete göre sayıları yani kişi sayısı
# df.describe().T # sayisal degiskenlerin betimsel istatistikleri

# sayısal değişkenleri kategorik değişkenlere çevirmek için kullanılan en yaygın iki fonk
# cut = sayısal ı hangi kategorilere bölmeyi biliyorsan ve belirtmek istersen
# örn: yaş değişkeninde 0-3 bebek 4-12 çocuk 13-30 genç 40-üstü yaşlı vb
# qcut = sayısal değişkeni tanımıyoruz çeyreklik değerlerine bölmek için
# değerleri yüzdelik oranda çeyrekliklere otomatik böler

# cut, qcut islemlerinde ornegin (0:15] = 0 dahil degil 15 dahil. ( = dahil degil, ] = dahil

# !!!!!!****** ÖNEMLİ ******!!!!!!
# survived kırılımında ortalamasını ve sayısını alarak sex index i ve new_age ile class kategorik değişkenleri ile değerleri bul
# df.pivot_table("survived", "sex", ["new_age", "class"], aggfunc = ["mean", "count"])

# pd.set_option('display.width', 500) # ekrandaki çıktı gösterim miktarı ayarı. \ ile alt satıra geçmeden kurtulma

# ignore_index=True # df index i siralar-resetler

# df[].value_counts() ile kategorilere erisim ve sayisi sikca kullanilacak!!!

# !!!!!!!!!!!!!!!!!! DF CHECK !!!!!!!!!!!!!!!!!!
# def check_df(dataframe, head=5):
#     print("##################### Shape #########################")
#     print(dataframe.shape)
#     print("##################### Types #########################")
#     print(dataframe.dtypes)
#     print("##################### Head ##########################")
#     print(dataframe.head(head))
#     print("##################### Tail ##########################")
#     print(dataframe.tail(head))
#     print("##################### NA ############################")
#     print(dataframe.isnull().sum())
#     print("##################### Quantiles #####################")
#     print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)



# df["adult_male"].astype(int) # degisken degerlerini degistirme islemi

# sns.countplot(x=dataframe[col_name], data=dataframe) # x= dataframe in ilgili degiskeni, data=olusturdugumuz dataframe



# !!!!!! DEFAULT STANDARTLAŞTIRMA FONKSİYONU KULLANIMI !!!!!!

# 1) MAIN FUNCTION

# def cat_summary(dataframe, col_name):
#     print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
#                         "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
#     print("##########################################")

# 2) FIRST CONTROL

# cat_summary(df, "sex") # sex degiskeninde deneme/ gecici islem

# 3) RUN FOR ALL DATA FRAME COLUMNS

# for col in cat_cols:
#     cat_summary(df, col, plot=True)

# 4) ADD DATA VISUALIZATION IN FUNC "cat_summary"

# def cat_summary(dataframe, col_name, plot=False): # plot:False on tanimli deger False olmali ki True iken kontrol saglayalim
#     print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
#                         "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
#     print("##########################################")
#
#     veri gorsellestirme
#     if plot: # plot True iken seaborn dan countplot ile sutun grafigi
#         sns.countplot(x=dataframe[col_name], data=dataframe) # x= dataframe in ilgili degiskeni, data=olusturdugumuz dataframe
#         plt.show(block=True) # block=True : grafik kapanana kadar kodlari calismasini durdurur

# 5) CHECK FOR "sex"

# cat_summary(df, "sex", plot=True) # sex degiskenini cagir, plot True dondur sutun grafigi versin

# 6) RUN FOR ALL COLUMNS... BUT "type bool" ERROR

# for col in cat_cols:
#     cat_summary(df, col, plot=True)

# 7) ... CHECK FOR "type bool" AND PUT ***** THEN RUN FOR ALL COLUMNS

# for col in cat_cols:
#     if df[col].dtypes == "bool":
#         print(col + " : type bool\n##########################################") # bool degiskeni olani ayirt edelim
#     else:
#         cat_summary(df, col, plot=True)

# 8) OR CHANGE "type bool" TO "int" FOR "adult_male"

# df["adult_male"].astype(int) # adult_male degiskeninde deneme/ gecici islem

# 9) THEN CHANGE FOR ALL "type bool"

# for col in cat_cols:
#     if df[col].dtypes == "bool":
#         df[col] = df[col].astype(int) # artik type bool gorunce farkli oldugunu ekrana yazdirmayip degisken degistiriyoruz
#         cat_summary(df, col, plot=True)
#
#     else:
#         cat_summary(df, col, plot=True)

# 10) RESULT

# standardization and data visualization for all columns perfectly

# Varsayılan olarak plt.show(block=True) şeklinde çalışır.
# "Bloklama" (blocking), programın grafiği kapatana kadar diğer kodları çalıştırmasını durdurur.
# Eğer block=False kullanılırsa, grafik açılır ama kod çalışmaya devam eder.
# Bu durumda grafik hemen kapanabilir
# plt.show(block=False) grafik acilir ama kod calismaya devam eder.

# !!!!!!************************************************* DİKKAT *************************************************!!!!!!
########################################################################################################################