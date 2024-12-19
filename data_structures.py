
###############################################
# VERİ YAPILARI (DATA STRUCTURES)
###############################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set


###############################################
# Veri Yapılarına Giriş ve Hızlı Özet
##############################################

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

#######################
# Tipleri değiştirmek
#######################

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

#######################
# Çok Satırlı Karakter Dizileri
#######################

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

#######################
# Karakter Dizilerinin Elemanlarına Erişmek
#######################

# index ler 0 dan başlar bu sebeple ilk indexi yazdırmak için name[0]
name
name[0]
name[3]
name[2]

#######################
# Karakter Dizilerinde Slice İşlemi
#######################

# böl anlamına da gelen birden fazla index i seçmek için, [0:2] de 2 sayılmaz 0,1 inci index yazdırılır
name[0:2]
long_str[0:10]

#######################
# String İçerisinde Karakter Sorgulamak
#######################

long_str

"veri" in long_str
# python da key sensitive var harf büyük ise yazılır
"Veri" in long_str

"bool" in long_str

###############################################
# String (Karakter Dizisi) Metodları
###############################################

# method lara erişmek için kullanılır
dir(str)
dir(int)

#######################
# len
#######################

#len method u bir gömülü fonksiyondur, str lere uygulanabilir. karakter boyut/uzunluk bilgisi verir

name = "john"
type(name)
type(len) #builtin_function_or_method

len(name)
len("onurkarasurmeli")
len("miuul")

### !!! Eğer bir fonksiyon class yapısı içinde tanımlandı ise "method", değil ise "function" dur !!!

#######################
# upper() & lower(): küçük-büyük dönüşümleri
#######################

# girilen str büyük karakter dizilerine dönüştürdü
"miuul".upper()
# girilen str küçük karakter dizilerine dönüştürdü
"MIUUL".lower()

# type(upper)
# type(upper())

#######################
# replace: karakter değiştirir
#######################

hi = "Hello AI Era"
hi.replace("l", "p")

#######################
# split: böler
#######################

# bir değer girilmez ise ön tanımlı değer yani boşluk böler
"Hello AI Era".split()

#######################
# strip: kırpar
#######################

" ofofo ".strip()
"ofofo".strip("o")


#######################
# capitalize: ilk harfi büyütür
#######################

"foo".capitalize()

dir("foo")

"foo".startswith("f")

###############################################
# Liste (List)
###############################################

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır.

notes = [1, 2, 3, 4]
type(notes)
names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]
type(not_nam)

not_nam[0]
not_nam[5]
not_nam[6]

# liste içerisindeki liste elemanına erişme
not_nam[6][1]

type(not_nam[6])
type(not_nam[5])

type(not_nam[6][1])

notes[0] = 99

not_nam[0:4]

###############################################
# Liste Metodları (List Methods)
###############################################

dir(notes)

#######################
# len: builtin python fonksiyonu, boyut bilgisi.
#######################

len(notes)
len(not_nam)

#######################
# append: eleman ekler
#######################

notes

# liste sonuna eleman eklendi
notes.append(100)

#######################
# pop: indexe göre siler
#######################

# girilen index teki değer listeden silindi
notes.pop(0)

#######################
# insert: indexe ekler
#######################

# girilen  index teki değer yerine yeni değer eklendi
notes.insert(2, 99)

