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

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

# for index, student in enumerate(students, 1): # buradaki 1 indexin başlangıç değerini belirler. farklı bir değer de yazılabilir.
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


