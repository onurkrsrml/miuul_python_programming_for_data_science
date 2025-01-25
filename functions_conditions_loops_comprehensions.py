##################################################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSIONS
##################################################
# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comprehesions


###############################################
# FONKSİYONLAR (FUNCTIONS)
###############################################

###############################################
# Fonksiyon Okuryazarlığı
###############################################

# Parametre de argüman da tanımlama için doğrudur.
# Parametre, fonksiyon tanımlaması esnasında ifade edilen değişkenlerdir.
# Argüman ise fonksiyon çağrılırken gönderilen değerlerdir.
# Yaygın kullanımı ise argüman olarak adlandırma eğilimindedir.

print("a", "b")

print("a", "b", sep="__")

#######################
# Fonksiyon Tanımlama
#######################
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


#######################
# Docstring
#######################

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


######################################
# Fonksiyonların Statement/Body Bölümü
######################################

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


###################################################################
# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
###################################################################

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


############################################
# Ne Zaman Fonksiyon Yazma İhtiyacımız Olur?
############################################

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


######################################################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
######################################################

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


##########################################
# Fonksiyon İçerisinden Fonksiyon Çağırmak
##########################################

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


#######################################################
# Lokal & Global Değişkenler (Local & Global Variables)
#######################################################

list_store = [1, 2]

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1, 9)
# Local etki alanındaki değişkenler fonksiyonun çalıştığı süre boyunca geçerlidir.
# Global etki alanındaki değişkenler ise bütün çalışma içerisinden erişilebilen değişkenlerdir.
# Buna rağmen local etki alanındaki değişkenler global etki alanını değiştirebilir.


###############################################
# KOŞULLAR (CONDITIONS)
###############################################

# True-False'u hatırlayalım.
1 == 1
1 == 2

# if
if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 11

if number == 10:
    print("number is 10")

number = 10
number = 20


def number_check(number):
    if number == 10:
        print("number is 10")

number_check(12)


#######################
# else
#######################

def number_check(number):
    if number == 10:
        print("number is 10")

number_check(12)


def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)

#######################
# elif
#######################

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_check(6)


### Bireysel Denemelerim Başlangıç

eski_maas = 5500
print(eski_maas)
if eski_maas == 5000:
    print("eski_maas 5000")

if eski_maas != 5000:
    print("eski_maas 5000 değil")

if eski_maas > 5000:
    print("eski_maas 5000 den büyük")

if eski_maas < 5000:
    print("eski_maas 5000 den küçük")

def maas_kontrol(eski_maas):
    if eski_maas == 5000:
        print("eski_maas 5000")
    elif eski_maas > 5000:
        print("eski_maas 5000 den büyük")
    elif eski_maas < 5000:
        print("eski_maas 5000 den kücük")
    else:
        print("eski_maas 5000 değil")

maas_kontrol(eski_maas)


maaslar = [5000, 6000, 7000, 8000, 9000]

def maas_kontrol(maaslar):
    if maaslar[0] == 5000:
        print("maas 5000")
    else:
        print("maas 5000 değil")

    if maaslar[1] == 5000:
        print("maas 5000")
    else:
        print("maas 5000 değil")

maas_kontrol(maaslar)


for a in maaslar:
    if a == 5000:
        print("maas 5000")
    else:
        print("maas 5000 değil")


for maas in maaslar:
    print(maas + maas*0.2)

for maas in maaslar:
    print(int(maas + maas*0.5))


ücretler = [20, 30, 40, 50, 60]

for ücret in ücretler:
    print(ücret)

for ücret in ücretler:
    print(ücret*20/100 + ücret)

for ücret in ücretler:
    print(int(ücret + ücret * 0.2))

for ücret in ücretler:
    print(int(ücret + ücret * 0.3))

for ücret in ücretler:
    print(int(ücret + ücret * 0.5))


def yeni_ücret(ücret, rate):
    return int(ücret*rate/100 + ücret)

yeni_ücret(15, 10)
yeni_ücret(45, 30)

for ücret in ücretler:
    print(yeni_ücret(ücret, 10))

ücretler2 = [15, 25, 35, 45, 55]

for ücret in ücretler2:
    print(yeni_ücret(ücret, 10))


#ücret 30 ve üstü olanlara yüzde 10 30 altındakilere yüzde 20 zam yapılacak.
for ücret in ücretler:
    if ücret >= 30:
        print(yeni_ücret(ücret, 10))
    else:
        print(yeni_ücret(ücret, 20))


### Bireysel Denemelerim Sonu


###########################
# Uygulama - Mülakat Sorusu
###########################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"


# Bireysel Denemelerim Başlangıç

# 1. Deneme
cümle = "hi my name is john and i am learning python"

len(cümle)

a=0
yeni_cümle = []
for i in cümle:
    a= a + 1
    if a % 2 == 0:
        yeni_cümle.append(i.upper())
    else:
        yeni_cümle.append(i.lower())

yeni_cümle = ''.join(yeni_cümle)
print(yeni_cümle)

# 2. Deneme
cümle.split()
yeni_cümle2 = 0
i = 0
def change_string(cümle):
    for i in range((yeni_cümle2)):
        if i % 2 == 0:
            yeni_cümle2[i] = yeni_cümle2[i].lower()
        else:
            yeni_cümle2[i] = yeni_cümle2[i].upper()
    return ' '.join(yeni_cümle2)

change_string("hi my name is john and i am learning python")

# Bireysel Denemelerim Sonu


# range fonksiyonu bize iki değer arasında sayı üretme imkanı sağlar
range(len("miuul")) # m, i, u, u, l

range(0, 5) # 0, 1, 2, 3, 4

for i in range(len("miuul")): # tüm değişkenlerin indexlerini yazdırmak için
    print(i)

# 4 % 2 = 0
# m =

def alternating(string):
    new_string = "" # değişiklikleri kaydetmek için boş bir string oluşturduk.
    # girilen string in tüm index lerini gez
    for string_index in range(len(string)): # string in bütün indexlerini gezmek için
        # index çift ise büyük harfe çevir
        if string_index % 2 == 0: # indexlerin çift olup olmadığını kontrol ediyoruz
            new_string += string[string_index].upper() # çift indexlerin harflerini büyük yap ve yeni string e ekle
        # index tek ise küçük harfe çevir
        else:
            new_string += string[string_index].lower() # tek indexlerin harflerini küçük yap ve yeni string e ekle
    print(new_string) # yeni string i yazdır

alternating("miuul") # fonksiyonu çalıştır


##########################
# break & continue & while
##########################

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)


for salary in salaries:
    if salary == 3000:
        continue
    print(salary)


# while

number = 1
while number < 5:
    print(number)
    number += 1


##################################################
# Enumerate: Otomatik Counter/Indexer ile for loop
##################################################

# enumerate fonksiyonu bir iterable(iteratif) obje alır ve her bir elemanın indexini ve elemanını birlikte döndürür.
# bu sayede hem indexe hem de elemana erişebilir ve işlem yapabiliriz.

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

# for index, student in enumerate(students, 1): # buradaki 1 indexin başlangıç değerini belirler. farklı bir değer de yazılabilir.
for index, student in enumerate(students, 1):
    print(index, student)


for index, student in enumerate(students):
    print(index, student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)


###########################
# Uygulama - Mülakat Sorusu
###########################
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]


# Bireysel Denemelerim Başlangıç

CIFT = []
TEK = []

def divide_students(students, new_students = []):
    for index, student in enumerate(students):
        if index % 2 == 0:
            CIFT.append(student)
        else:
            TEK.append(student)
    return new_students

divide_students(students)
new_students = CIFT + TEK

# Bireysel Denemelerim Sonu


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

st = divide_students(students)
st[0]
st[1]


###################################################
# alternating fonksiyonunun enumerate ile yazılması
###################################################

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is john and i am learning python")


####################
# Mülakat Sorusu - 1
####################

# çözüm
def alternating(string) :
    new_string = ""
    for i, string_index in enumerate(string):
        if i % 2 == 0:
            new_string += string_index.upper()
        else:
            new_string += string_index.lower()
    print (new_string)

alternating("miuul")


#######################
# Zip
#######################
# zip fonksiyonu iki veya daha fazla listeyi birleştirmek için kullanılır.

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students, departments, ages))


###############################################
# lambda, map, filter, reduce
###############################################
# lambda: kısa süreli ve anonim fonksiyonlar oluşturmak için kullanılır.
# map: bir fonksiyonu bir liste üzerinde çalıştırmak için kullanılır.
# filter: bir fonksiyonu bir liste üzerinde filtrelemek için kullanılır.
# reduce: bir fonksiyonu bir liste üzerinde reduce etmek için kullanılır.

# lambda
# python ın fonksiyonel programlama yönüne hitap eden, vektör seviyesinde işlemler yapma yönüne hitap eden bazı araçlardır.
# kullan-at fonksiyondur. Değişkenlerde yer tutmaz
def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b

new_sum(4, 5)

# map
# döngü yazmaktan kurtarır.
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))


# del new_sum # üstteki örneğe ait olan lambda fonksiyonunu sildik.

# map fonksiyonu ile lambda fonksiyonu birlikte kullanımı(yalnızca elimizdeki listeyi kullanarak işlem yaptık)
# def fonk tanımlamadık(lambda kullandık), for döngüsü kullanmadık(map kullandık)
list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2 , salaries))


# FILTER
# filter fonk giriş parametreleri olarak bir koşul ele alır. True ise listeye ekler.
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

# REDUCE
# tüm elemanlara işlemi uygulama 1+2=3 3+3=6 6+4=10 soldan sağa ilk eleman+ikinci eleman sonra üçüncü eleman ...
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)


###############################################
# COMPREHENSIONS
###############################################

#######################
# List Comprehension
#######################

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

# yukarıdaki işlemi list comprehension ile yapalım
[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

# işlemin list comprehensiona adım adım evrimi
[salary * 2 for salary in salaries] # maaşları for ile gezip 2 ile çarptık
[salary * 2 for salary in salaries if salary < 3000] # 3000 den küçük olan maaşları for ile gezip 2 ile çarptık
[salary * 2 if salary < 3000 else salary * 0 for salary in salaries] # 3000 den küçük olan maaşları for ile gezip 2 ile çarptık, büyük olanları 0 ile çarptık
# eğer ki yalnızca "if" işlemi yapılacak ise "for" dan SONRA yazılmalıdır
# eğer ki hem "if" hem "else" işlemi yapılacak ise "for" dan ÖNCE yazılmalıdır

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]
# yukarıdaki işlemde new_salary fonksiyonunu kullanarak işlem yaptık
# totalde for döngüsü if else blogu ve fonksiyonu bir arada kullandık

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]
# yukarıdaki işlemde students listesindeki öğrencileri students_no listesindeki öğrencilerle karşılaştırıp
# eğer students_no listesinde yoksa büyük harf yap, varsa küçük harf yap

# not in kullanımı
[student.upper() if student not in students_no else student.lower() for student in students]
# yukarıdaki işlemde students listesindeki öğrencileri students_no listesindeki öğrencilerle karşılaştırıp
# eğer students_no listesinde yoksa küçük harf yap, varsa büyük harf yap

# Bireysel Denemelerim Başlangıç
ogrenci = ["John", "Mark", "Venessa", "Mariam"]
ogrenci_degıl = ["John", "Venessa"]

def new_students():
    return [i.lower() if i in ogrenci_degıl else i.upper() for i in ogrenci]

[new_students() if i in ogrenci else new_students() for i in range(len(ogrenci_degıl))]
# Bireysel Denemelerim Sonu

#######################
# Dict Comprehension
#######################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v*2 for (k, v) in dictionary.items()}


###########################
# Uygulama - Mülakat Sorusu
###########################

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir
# Key'ler orjinal değerler value'lar ise değiştirilmiş değerler olacak.


numbers = range(10)
new_dict = {}

for i in numbers:
    if i % 2 == 0:
        new_dict[i] = i ** 2

{i: i ** 2 for i in numbers if i % 2 == 0}


#######################################
# List & Dict Comprehension Uygulamalar
#######################################

####################################################
# Bir Veri Setindeki Değişken İsimlerini Değiştirmek
####################################################

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

# veri seti çağırma
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]


####################################################################################
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz
####################################################################################

# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']

[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

##############################################################################
# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz.
##############################################################################

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

# klasik olarak seaborn datasetini çağırma işlemi
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

# sadece numerik değişkenlerin seçilmesi
# df.dtype == "O" df(dataframe) de dtype(data type) ın içinde "O"(object) yani (kategorik) değişkenlerin seçilmesi
# df[col].dtype != "O" şu anlama gelir: df(dataframe) deki col değişkeninin dtype(data type) ının "O"(object) eşit değil/olmadığı kontrolü
# yani "O" object değilse nümerik değişkenleri seçmek istiyoruz anlamına gelir. sayısal değişkenleri seçmek için kullanılır.
num_cols = [col for col in df.columns if df[col].dtype != "O"]
# boş sözlük oluşturma
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

# kısa yol

# yukarıdaki for u dict comprehensions ile yazdık
{col: agg_list for col in num_cols}

#
new_dict = {col: agg_list for col in num_cols}

# .head() fonksiyonu ile ilk 5 gözlemi görmek için kullanılır.
# df de num_cols içinde nümerik olanları ayıklayıp .head() ile ilk 5 gözlemi gösterdik.
df[num_cols].head()

# .agg() fonk ile nümerik değişkenlerin istenilen işlemlerini yapabiliriz.
#
# .agg() fonksiyonuna gönderdiğiniz sözlüğün(new_dict) içerisindeki değişkenler eğer girilen df de varsa(df[num_cols])
# bu değişkenleri key bölümünden tutar value bölümüne girdiğiniz bütün fonksiyonları(agg_list = ["mean", "min", "max", "sum"])
# uygular ve sonucu size gösterir.
#
# df[num_cols].agg(new_dict) işlemi sonucunda size nümerik değişkenlerin istenilen işlemlerini yapmış bir dataframe döner.
#
# ***************!!!!!!!!!!!!!!! ALERT: ADVANCED BİR İŞLEM !!!!!!!!!!!!!!!***************
df[num_cols].agg(new_dict)
# ***************!!!!!!!!!!!!!!! ALERT: ADVANCED BİR İŞLEM !!!!!!!!!!!!!!!***************

#################
# Ekstra Bilgiler
#################

# veri setlerindeki uyarıları kapatmak için kullanılır
#warnings.filterwarnings("ignore")

# comprehensions sırası
# 1) for yapıştır, 2)if var mı? (for + if) / else var mı? (if + for), 3)en başa koşulları yaz

# "in" ve "not in" kullanımları
# "an" in "Furkan" # True
# "t" not in "Furkan" # True
# "f" in "Furkan" # False

