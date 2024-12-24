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


#######################
# Fonksiyonların Statement/Body Bölümü
#######################

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


#######################
# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
#######################

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


