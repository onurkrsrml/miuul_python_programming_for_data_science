#####################################################
# PYTHON İLE VERİ ANALİZİ (DATA ANALYSIS WITH PYTHON)
#####################################################
# - NumPy
# - Pandas
# - Veri Görselleştirme: Matplotlib & Seaborn
# - Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Exploratory Data Analysis)

#############################################
# NUMPY
#############################################

# Neden NumPy? (Why Numpy?)
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

#############################################
# Neden NumPy?
#############################################
import numpy as np
from numpy.ma.extras import column_stack

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b




##################################################
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
##################################################
import numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int) # 0'lardan oluşan 10 elemanlı bir array int tipinde
np.zeros(10, dtype=str) # 0'lardan oluşan 10 elemanlı bir array str tipinde
np.zeros((3, 5)) # 3x5 boyutunda 0'lardan oluşan bir array / matris

np.random.randint(0, 10, size=10) # 0-10 arasında rastgele 10 sayı
np.random.randint(0, 10, size=(3, 5)) # 3x5 boyutunda 0-10 arasında rastgele sayılardan oluşan bir array / matris

np.random.normal(10, 4, (3, 4)) # ortalama 10, standart sapma 4 olan 3x4 boyutunda normal dağılıma sahip bir array / matris
# np.random.normal(ortalama, standart sapma, (satır, sütun))
# np.random.normal(kitle ortalama, argüman, boyut bilgisi)
# Belirli bir istatistiksel dağılıma göre sayı üreten fonk/method

#############################################
# NumPy Array Örnekleri (Exstra araştırma!!!)
#############################################
np.arange (0, 10, 2) # 0'dan 10'a kadar 2'şer artan sayılar
np.linspace(0, 1, 5) # 0-1 arasında 5 sayı
np.linspace(0, 1, 20) # 0-1 arasında
np.linspace(0, 1, 20, False) # 0-1 arasında 20 sayı, son say
# np.linspace(başlangıç, bitiş, sayı, son sayı dahil mi?)
##############################################

#####################################################
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
#####################################################
import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5) # 0-10 arasında rastgele 5 sayı. başa 0 yazılmazsa 0-10 arasında rastgele üret sayılır
a.ndim # number of dimensions / boyut sayısı
a.shape # dimensions of the array (e.g., 3x5 for 3 rows and 5 columns)
a.size # total number of elements
a.dtype # data type of array elements

#############################################
# Yeniden Şekillendirme (Reshaping)
#############################################
import numpy as np

# Yöntem 1
np.random.randint(1, 10, size=9) # 1-10 arasında rastgele 9 sayı
np.random.randint(1, 10, size=9).reshape(3, 3) # 1-10 arasında rastgele 9 sayı ve 3x3 boyutunda matris

# Yöntem 2
ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)


#############################################
# Index Seçimi (Index Selection)             !!!!!!****** DİKKAT ******!!!!!!
#############################################
import numpy as np
a = np.random.randint(10, size=10)
a[0]
a[0:5]
a[0] = 999

m = np.random.randint(10, size=(3, 5))

m[0, 0]
m[1, 1]
m[2, 3]

m[2, 3] = 999

m[2, 3] = 2.9

m[:, 0] # slicing: tüm satırlar, 0. sütun
m[1, :] # slicing: 1. satır, tüm sütunlar
m[0:2, 0:3] # slicing: 0-2 satırlar, 0-3 sütunlar

############################################
# Fancy Index (İstediğimiz Elemanları Seçme)
############################################
import numpy as np

v = np.arange(0, 30, 3)
v[1]
v[4]

catch = [1, 2, 3]

v[catch]

#################################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
#################################################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

#######################
# Klasik döngü ile
#######################

# for i in v:
#     print(i)

ab = []
for i in v:
    if i < 3:
        ab.append(i)

#######################
# Numpy ile
#######################
v < 3

v[v < 3]
v[v > 3]
v[v != 3]
v[v == 3]
v[v >= 3]

#############################################
# Matematiksel İşlemler (Mathematical Operations)
#############################################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2
v - 1

np.subtract(v, 1) # v - 1
np.add(v, 1) # v + 1
np.mean(v) # np.sum(v) / len(v)
np.sum(v) # toplam
np.min(v) # minimum
np.max(v) # maximum
np.var(v) # varyans
v = np.subtract(v, 1) # v - 1. array'e atama

np.std(v) # standart sapma
np.median(v) # medyan
np.percentile(v, 25) # 1. çeyrek
np.percentile(v, 75) # 3. çeyrek
np.corrcoef(v) # korelasyon
np.cov(v) # kovaryans
np.log(v) # logaritma



#######################
# NumPy ile İki Bilinmeyenli Denklem Çözümü
#######################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

# ilk array'de katsayılar, ikinci array'de sonuçlar olacak
# [5, 1] x0'ın katsayısı
# [1, 3] x1'in katsayısı
# [12, 10] sonuçlar
a = np.array([[5, 1], [1, 3]]) # katsayılar
b = np.array([12, 10]) # sonuçlar

np.linalg.solve(a, b) # x0 ve x1 değerleri bulunur. linalg: linear algebra/lineer cebir



########################################################################################################################
######### (SUMMARY) NumPy ##############################################################################################

# Neden NumPy? (Why Numpy?)
# 1) Hız: Verimli/sabit tipte veri saklar
# 2) Fonksiyonel /vektörel düzeyde çeşitli kolaylıklar sağlamaktadır

# Numpy Array Özellikleri
# Fancy Index

######### (SUMMARY) NumPy ##############################################################################################
########################################################################################################################



#############################################
# PANDAS
#############################################

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

#############################################
# Pandas Series
#############################################
import pandas as pd

# ekonometrik ve zaman serisi problemleri için ortaya çıktı
s = pd.Series([10, 77, 12, 4, 5])
type(s)
s.index # index bilgisi, RangeIndex(start=0, stop=5, step=1)
s.dtype # tip bilgisi, dtype('int64')
s.size # eleman sayısı, 5
s.ndim # boyut sayısı, 1
s.values # içindeki değerlere erişmek, array([10, 77, 12,  4,  5], dtype=int64)

# numpy index bilgisi içermez. pandas series'te index bilgisi bir iç özelliktir, index ve values vardır.
# pandas series' te sonuna values ekleyerek numpy array'e dönüştürebiliriz. / diğer bir tanımla
# pandas series' in sonuna values ekledik ve değerlerine erişmek istedik bu durumda biz pandas series' in index bilgisiyle
# ilgilenmiyoruz demektir. Bu durumda pandas series'i numpy array'e dönüştürmüş oluyoruz.
# values ifadesine seriler ile çalışan bir method uygulamak istediğimizde hata alırız ama bu çıktının farklı bir veri
# yapısı olabileceği farkındalığı taşırsak karşılaşabileceğimiz problemleri daha hızlı çözeriz.
type(s.values) # numpy array dir, numpy.ndarray

s.head() # ilk 5 eleman
s.head(3) # ilk 3 eleman
s.tail(3) # son 3 eleman


#############################################
# Veri Okuma (Reading Data)
#############################################
import pandas as pd

df = pd.read_csv("datasets/advertising.csv") # csv dosyasını okuma
df.head()
# pandas cheatsheet ile yaygın kullanımlara ulaşabiliriz (https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

# df = pd.read_csv("datasets/advertising.csv", usecols=["TV", "radio"]) # usecols: sadece belirli sütunları okumak için

#############################################
# Veriye Hızlı Bakış (Quick Look at Data)
#############################################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head() # ilk 5 gözlem
df.tail() # son 5 gözlem
df.shape # boyut bilgisi
df.info() # genel bilgi # pandas df' de object ve category ikisi de category type'dır.
df.columns # sütun isimleri
df.index # index bilgisi
df.describe().T # betimsel istatistikler (özet istatistikler). T: transpozunu alır

df.select_dtypes(include=["object"]).columns # object veri tipindeki sütunları seçer

df.isnull() # eksik gözlemler pandas df türü
df.isnull().values # eksik gözlemler numpy array türü. Pandas df' de .values kullanıldığında numpy array'e dönüşür
df.isnull().values.any() # eksik gözlem var mı? True/False. !!!Veri setinde eksik gözlem var mı?!!!
df.dropna() # eksik gözlemleri siler / kalıcı değil
df.dropna(inplace=True) # eksik gözlemleri siler / kalıcı (inplace=True ile kalıcı hale getirir)

df.isnull() # eksik gözlem sayısı. True=1 False=0
df.isnull().sum() # eksik gözlem sayısı topalamı. !!!Değişkenlerdeki eksikliklerin toplamı!!!
df["sex"].head() # kategorik değişkenin ilk 5 gözlemi
df["sex"].value_counts() # kategorik değişkenin sınıflarına erişmek


#################################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas) (satır indexleri üzerinde işlemler)
#################################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

df.index # index bilgisi
df[0:13] # 0-13' e kadar satırlar / 13 dahil değil
df[0:13:2] # 0-13' e kadar 2'şer atlayarak satırlar / 13 dahil değil

# pandasta satır silme işlemi
df.drop(0, axis=0).head() # 0. satırı sil / kalıcı değil
# çoklu silme için
# df.drop(0:13, axis:0).head() # hata verir çünkü slicing yapamazsınız
# onun yerine range kullanılır
df.drop(range(0, 13), axis=0).head() # 0-13'e kadar satırları sil / kalıcı değil
# ya da liste oluşturur onu kullanırız
delete_indexes = [1, 3, 5, 7] # silmek istediğimiz indexler
df.drop(delete_indexes, axis=0).head(10) # 1, 3, 5, 7. satırları sil

# kalıcı silmek için   !!!!!!****** DİKKAT ******!!!!!!
# df.drop(delete_indexes, axis=0, inplace=True) # inplace ile kalıcı silme!!!
# diğer yöntem
df = df.drop(delete_indexes, axis=0) # kalıcı hale getirmek için df'ye atama yapılır

# sütun silme işlemi
df.drop("pclass", axis = 1).head() # pclass sütununu sil / kalıcı değil


###########################
# Değişkeni Indexe Çevirmek
###########################

df["age"].head() # age değişkeni
df.age.head()
df["age"][0:5:2] # age değişkeninin 0-5 arasındaki 2'şer atlayarak satırlarını seç

df.index = df["age"] # age değişkenini index/sıra yap
df.head()
df.index

df.drop("age", axis=1).head() # age değişkenini sil / kalıcı değil
# df.drop("age", axis=1, inplace=True) # age değişkenini sil/kalıcı


###########################
# Indexi Değişkene Çevirmek
###########################

df.index

# Yöntem 1
df["age"] = df.index # age index'ini değerleri ile age isimli değişkene çevir/ekle(age i oluştur index değerlerini ata)
df.head()

# Yöntem 2
df.drop("age", axis=1, inplace=True) # age değişkenini sütundan sildik yeniden deniyoruz
df.head()

df.reset_index().head() # index te yer alan degeri silip yeni bir sutun/degisken olarak ekleyecek
df = df.reset_index() # kalıcı hale getirme
df.head()


###############################
# Değişkenler Üzerinde İşlemler (sütun indexleri üzerinde işlemler)
###############################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None) # tüm sütunları göster/max kolon sayısını sınırsız yapar
df = sns.load_dataset("titanic")
df.head()

"age" in df # age değişkeni var mı?

df["age"].head() # age değişkeni seç
df.age.head() # age değişkeni seç

# !!!!!!****** DİKKAT ******!!!!!!
df["age"].head()
type(df["age"].head()) # pandas series türünde bir veri!!! ama neden? biz pandas df üzerinden işlem yapıyoruz?_çünkü tek boyutlu bir veri
# sadece bir değişken tek başına çağrıldığında tek boyutlu veri olur. pandas df ile çalışıyor olsan bile bu bir pandas series türünde bir veri olur

# çok boyutlu olarak seçebilmek için köşeli parantez içinde liste girmeliyiz / çift köşeli parantez
# 2 boyutlu bir veri elde etmek için yani pandas df ile çalışırken onun türünde bir veri için çift köşeli parantez kullanmalıyız
df[["age"]].head() # 2 boyutlu bir veri yapısı elde ederiz.
type(df[["age"]].head()) # pandas df türünde bir veri

df[["age", "alive"]] # ikili seçim

col_names = ["age", "adult_male", "alive"] # seçmek istediğimiz sütun isimleri 2 den de fazla olursa kolay işlem
df[col_names].head()
type(df[col_names]) # pandas df türünde bir veri çünkü col_names değişkeni liste türünde ve 2 boyutlu

df_name = "alive"
type(df[df_name]) # pandas series türünde bir veri çünkü df_name değişkeni string türünde ve 1 boyutlu


df["age2"] = df["age"]**2 # age değişkeninin karesi yeni bir değişken olarak eklendi
df["age3"] = df["age"] / df["age2"] # age değişkeninin age2 değişkenine bölümü yeni bir değişken olarak eklendi
df.head()

df.drop("age3", axis=1).head() # age3 değişkenini sütun olarak sil / kalıcı değil
df.drop("age3", axis=1, inplace=True) # age3 kalıcı sil
df.head()

col_names = ["age", "adult_male", "alive"]
df.drop(col_names, axis=1).head() # ilgili listedeki sütunları sil / kalıcı değil (çoklu silme)


# !!!!!!****** DİKKAT ******!!!!!!
# aynı ismi içeren birden fazla değişkene erişmek için loc kullanılır
# burada loc ile içerisinde age geçen tüm sütunları seçtik ama ~ yani tilda işareti ile age içermeyen sütunları seçtik
df.loc[:, ~df.columns.str.contains("age")].head() # age içermeyen sütunları seç / kalıcı değil
# df = df.loc[:, ~df.columns.str.contains("age")].head() # kalıcı seçer age barındıranları siler / inplace yerine atama yaptık
df.head()
"age" in df # False



#######################
# iloc & loc
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer based selection
df.iloc[0:3] # 0 dan 3 e kadar olan satırları seç / 3 dahil değil
df.iloc[0, 0] # 0. satır, 0. sütun

df.iloc[0:3, "age"] # hata verir çünkü iloc integer based selection'dır, string ile çalışmaz
df.iloc[0:3, 0:3] # 0:3 satırlar, 0:3 sütunlar
df.iloc[0:3, 3] # 0:3 satırlar, 3. sütun
df.iloc[0:3, [0, 3, 5]] # 0:3 satırlar, ilgili sütunlar


# loc: label based selection / mutlak olarak isimlendirmenin kendisini seçiyor
df.loc[0:3]  # 0 dan 3 e olan satırları seç / 3 dahil

df.loc[0:3, 0:3] # hata verir çünkü loc label based selection'dır, integer ile çalışmaz
df.loc[0:3, "age"] # 0:3 satırlar, age sütunu

col_names = ["age", "embarked", "alive"] # loc ile çoklu seçim için önce sütun isimlerini bir listeye atarız
df.loc[0:3, col_names] # 0:3 satırlar, ilgili sütunlar


#######################################
# Koşullu Seçim (Conditional Selection)
#######################################
import pandas as pd
import seaborn as sns # seaborn veri setleri ile çalışmak için
pd.set_option('display.max_columns', None) # tüm sütunları göster
df = sns.load_dataset("titanic") # seaborn veri setlerinden birini("titanic") yükledik
df.head()

df[df["age"] > 50].head() # age değişkeni 50'den büyük olanlar / tüm değişkenler

# age değişkeni 50'den büyük olanlar / sadece age
df[df["age"] > 50].count() # sonuctan hicbir degisken secmedik, hepsine count atti / hatali
df[df["age"] > 50]["age"].count() # age değişkeni 50'den büyük olanların sayısı


df.values # numpy array' e donusturur
df.columns # sutunlar
df.dtypes # tip bilgisi
df["fare"].dtypes # ilgili degiskenin tip bilgisi
df[df["fare"] > 50]["fare"].count() # fare in 50 buyuk degerlerinin sayisi
df[df["fare"] > 50]["fare"].head()


df.loc[df["age"] > 50, ["age"]].head() # age > 50, age göster
df.loc[df["age"] > 50, ["age", "class"]].head() # age > 50, age ve class göster
# !!! her koşul parantez içerisine yazılmalı !!!
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head() # (age > 50( ve (sex == male), age ve class göster
# (age > 50) ve (sex == male) ve (embark_town == Cherbourg), age ve class göster
df.loc[(df["age"] > 50) & (df["sex"] == "male") & (df["embark_town"] == "Cherbourg"), ["age", "class"]].head()
# (age > 50) ve (sex == male) ve (embark_town == Cherbourg), age, class ve embark_town göster
df.loc[(df["age"] > 50) & (df["sex"] == "male") & (df["embark_town"] == "Cherbourg"), ["age", "class", "embark_town"]]
# iç içe veya lı koşulda veya kısmı iç içe iki parantezde yazılır
# (age > 50) ve (sex == male) ve ((embark_town == Cherbourg) veya (embark_town == Southampton)), age, class ve embark_town göster
df.loc[(df["age"] > 50) & (df["sex"] == "male") & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")), ["age", "class", "embark_town"]]

# veya koşulumuzu görebilmek için atama yaparak kalıcı hale getirmeliyiz
# df = df.loc[(df["age"] > 50) & (df["sex"] == "male") & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")), ["age", "class", "embark_town"]]
# daha düzenli olması için alt alta yaz
# df = df.loc[(df["age"] > 50) & (df["sex"] == "male")
#        & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
#        ["age", "class", "embark_town"]]

df.head() # üstteki koşul kaydedildi kontrolü
df["embark_town"].value_counts() # veya lı koşul kontrolü, normalde 3 frekans var iken koşulumuzda yalnızca 2sini seçtik


# orjinal df e orjinal haliyle ulaşabilmek adına yeni bir değişkene atadık
df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()



#############################################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
#############################################

# - count() # say
# - first() # ilk
# - last() # son
# - mean() # ort
# - median() # medyan
# - min() # min
# - max() # max
# - std() # standart sapma
# - var() # varyans
# - sum() # toplam
# - pivot table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean() # yaş değişkeninin ortalaması

# cinsiyete göre yaş ortalamaları
# Yöntem 1
df.groupby("sex")["age"].mean() # groupby gruplamasında sex kırılımı age değişkeni ortalaması

# Yöntem 2
df.groupby("sex").agg({"age": "mean"}) # groupby ve aggregation birlikte kullanımı önerilir
# kütüphane gibi süslü paranteze aldık

# sebebi ise çoklu fonk bir arada sonuç çıkarmak istenmesi durumlarında kolay ve anlaşılır
df.groupby("sex").agg({"age": ["mean", "sum"]}) # cinsiyete göre yaş ort ve toplamı
# veriyi cinsiyet e göre groupby aldık/kırdık sonra yaşın ort ve yaşın sum ı aldık

# ayni durumun embark_town a göre frekans sayılarını alalım
df.groupby("sex").agg({"age": ["mean", "sum"], "embark_town": "count"})
# embark_town frekansı değil sex frekansı nı çıktı verdi / istenilen çıktı değil çünkü iki si sayısal değişken değil

# sayısal değişkenler ile istenilen sonucu alırız
df.groupby("sex").agg({"age": ["mean", "sum"], # aynı zamanda survived değişkeni nin 0 a yakınlığına bakalım
                       "survived": "mean"})
# YORUM: kadınların %74 erkeklerin %18 i hayatta kalmış

# sex ve embark_town kırılımında age ve survived ortalaması
df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                       "survived": "mean"})
# YORUM: cinsiyete göre ilgili duraklardan binen yolcuların yaş ort ve hayatta kalma ort

# sex, embark_town ve class kırılımında age ve survived ortalaması
df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                       "survived": "mean"})
# YORUM: cinsiyete göre ve duraklara göre kırılımların class a göre kırılımında yaş ort ve hayatta kalma oranı
# burada hayatta kalma ortalamalarında değeri 0.000 olan frekanslardaki sonuç ya kişi/değişken olmaması ya da 1 kişi olması
# sex, embark_town ve class kırılımında age ve survived ortalaması ve cinsiyet sayısı ile bunu öğrenelim
df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})
# YORUM: cinsiyete göre binilen durağa göre binilen sınıflarda yaş ort hayatta kalma oranı ve o cinsiyetin/kişi sayısı



#######################
# Pivot table
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()


# pivot table ın ön tanım değeri mean(ortalama) dir

# yaş ve gemiye binme lokasyonunu ifade eden tablo ve kesişimde hayatta kalma bilgisine erişim
# row/index de sex, columns da embarked, values argümanı olarak/kesişim de survived
df.pivot_table("survived", "sex", "embarked") # value survived index sex columns embarked
# cinsiyete göre ve lokasyona göre ortalama hayatta kalma değerleri

#  bu kesişimde survived değerlerinin standard sapma ları hesaplandı
df.pivot_table("survived", "sex", "embarked", aggfunc = "std")

#  columns ["embarked", "class"] / çoklu columns
df.pivot_table("survived", "sex", ["embarked", "class"])

# hem satır hem sütun lardan 2 seviyeli index e tek value içeren ortalama değer pivot table
df.pivot_table("survived", ["sex", "alone"], ["embarked", "class"])

# hem satır hem sütun lardan 2 seviyeli index e çift value içeren ortalama değer pivot table
df.pivot_table(["survived", "age"], ["sex", "alone"], ["embarked", "class"])

# hem satır hem sütun lardan 2 seviyeli index e çift value içeren varyans pivot table
df.pivot_table(["survived", "age"], ["sex", "alone"], ["embarked", "class"], aggfunc = "var")


df.head()

# hem cinsiyet kırılımı hem lokasyon kırılımı ve yaş kırılımı istiyoruz ama sayısal olduğu için önce kategorik çevir
# cut ve qcut ile değişkenleri bölüp yeni değişkene atayalım
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90]) # önce değişken sonra aralık gir
df.head()

# yaş kırılımında hayatta kalmaları inceleyebiliriz artık
df.pivot_table("survived", "sex", "new_age") # age kategorik ve sex kırılımında survived ort

# bir boyut daha eklersek, class değişkeninin kategorik versiyonunu ekliyoruz
df.pivot_table("survived", "sex", ["new_age", "class"]) # age ve class kategorik değikenleri ile sex kırılımında survived ort

# cinsiyeti saydırarak kişi sayısını bulmaya çalışıyoruz
df.pivot_table("survived", "sex", ["new_age", "class"], aggfunc = ["mean", "count"])

df.head()

pd.set_option('display.width', 500) # ekrandaki çıktı gösterim miktarı ayarı. \ ile alt satıra geçmeden kurtulma


#############################################
# Apply ve Lambda
#############################################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

# Apply: Satıur ve Sütunlara fonk uygular
# Lambda: Kullan at fonk

# amaç önce iki farklı age değişkeni daha oluşturmak ve sonrasında üzerinde işlemler yapmak
# önce uzun yoldan basit işlemler ile adım adım yapalım
df["age2"] = df["age"]*2 # age2, age in 2 katı olsun
df["age3"] = df["age"]*5 # age3, age in 5 katı olsun

# tek tek age içeren değişkenleri 10 a böldük
(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

# for döngüsü ile bunu daha kolay yapalım
#ilk adım age içerenleri bul
for col in df.columns:
    if "age" in col:
        print(col)

#age içerenleri 10 a böl
for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

# yapılan değişikliği df de kaydet
for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

# şimdi ise apply lambda ile deneyelim, age leri tek tek yazdık
df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

# loc kullanarak apply lambda uyguladık
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()


# !!!!!!****** DİKKAT ******!!!!!!
# öyle bir fonk olsun ki bu fonk uygulandığı df deki değerleri standartlaştırsın(istatistikçilerin kullandığı yaygın normalleştirme fonk)
# bütün gözlem birimlerinden ilgili değişkenin ort çıkaracak ve std bölecek
# içinde age barındıranları seçecek, değişkenden sütun ort çıkaracak, sütun standart sapmasına bölecek
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

# dışarıda bir fonk tanımlayıp içerisinde bu standartlaştırmayı girebiliriz ve kendi loc fonksiyonumuzun içine yazabiliriz
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std() # değişkenden ort çıkar, std böl(standartlaştırma/normalleştirme)

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head() # standartlaştırma def i loc içinde yazdık

# df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler) # değişiklikleri kaydet

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler) # değişiklikleri kaydet
df.head()



#############################################
# Birleştirme (Join) İşlemleri
#############################################
import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3)) # random sayilar 1-30 arasinda, 5-3 luk np array olustur
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"]) # df1 adinda df olustur. index = m, columns = ilgili)
df2 = df1 + 99 # df2 adinda baska bir df olustur df1 in elemanlarina 99 ekleyerek ata

pd.concat([df1, df2]) # concat = df leri toplar(index i oldugu gibi alir-siralamaz)

pd.concat([df1, df2], ignore_index=True) # df deki index i resetler-siralar

# concat da axis = 0(default) alirsan alt alta, axis = 1 alirsan yan yana toplar

#######################
# Merge ile Birleştirme İşlemleri
#######################

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]}) # pd.DataFrame veriyi df e cevir. elimizdeki dict ile df olusturduk
# veri yapisini yorumlayacak olursak: dict{}, str:, list str[], list int[], df(). Yani 6 farkli veri yapisi vardir.

pd.merge(df1, df2) # merge: otomatik employees'a gore df1 df2 yi birlestirdi.
pd.merge(df1, df2, on="employees") # eger ki farkli bir degisken ile yapmak istersek on= argumani ile de yapabiliriz

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2) # yeni df e atadik, devami asagidaki df den birlestirecegiz

# yorumlayarak yapalim. df4 te mudur bilgisi var ama az once employees ile birlestirme yapmistik, burada hangi degiskeni kullanacaz?
df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']}) # ortak degisken olarak group var bununla merge edecektir/gerektiginde biz de secebiliriz

pd.merge(df3, df4)  # group degiskenine gore otomatik merge edecektir



#############################################
# VERİ GÖRSELLEŞTİRME: MATPLOTLIB & SEABORN
#############################################

#############################################
# MATPLOTLIB
#############################################

# Kategorik değişken: sütun grafik. seaborn icindeki countplot ya da matplotlib icindeki bar
# Sayısal değişken: hist, boxplot (istatistiksel grafikler) ikisi de dagilim gosterir boxplat aykiri deger de gosterir


#############################################
# Kategorik Değişken Görselleştirme
#############################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt # matplot icinden pyplot i tanimlama
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df['sex'].value_counts().plot(kind='bar') # sex degiskeni value + sayilari ver, plot = cizdir, kind = tip/tur, bar=sutun bilgisi
plt.show()

# pip install --upgrade matplotlib # konsoldan paket guncelle


#############################################
# Sayısal Değişken Görselleştirme
#############################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()
# aykiri degerleri ceyreklik degerler uzerinden gosterebiliyor.
# verinin kendi icindeki dagilimini goz onunde bulundurarak genel dagilimin disindaki gozlemleri yakalar



#############################################
# Matplotlib'in Özellikleri
#############################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# katmanli sekilde veri gorsellestirme

#######################
# plot
#######################

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show() # noktalardan cizgi grafigi

plt.plot(x, y, 'o') # o argumani nokta seklinde gosterir
plt.show()
# !!!!!onceki grafigi kapatmadan diger fonk calistirdigimizda grafiklerin ustune atar/birlesir!!!!!

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o') # ilgili degerlere nokta koyar
plt.show()



#######################
# marker
#######################

y = np.array([13, 28, 11, 100])

plt.plot(y, marker='o') # marker i nokta ile goster
plt.show()

plt.plot(y, marker='*') # marker i * ile goster
plt.show()

markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h'] # marker tipleri

#######################
# line
#######################

y = np.array([13, 28, 11, 100])
plt.plot(y)
plt.show()

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashed")
plt.show()

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dotted")
plt.show()

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashdot", color="r")
plt.show()

#######################
# Multiple Lines
#######################

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

#######################
# Labels
#######################

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
# Başlık
plt.title("Bu ana başlık")

# X eksenini isimlendirme
plt.xlabel("X ekseni isimlendirmesi")

plt.ylabel("Y ekseni isimlendirmesi")

plt.grid()
plt.show()

#######################
# Subplots
#######################

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1) # 1 satirli 2 sutunlu grafik olusturma/ 1 e 2 lik grafik, 1. grafik
plt.title("1") # 1. grafigini olusturuyoruz
plt.plot(x, y)
plt.show()


# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)
plt.show()


# 3 grafiği bir satır 3 sütun olarak konumlamak.
# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)
plt.show()


# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)
plt.show()


# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)
plt.show()



#############################################
# SEABORN
#############################################
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips") # tips df i getir
df.head()

df["sex"].value_counts() # sex degiskeni sayisi getir
# seaborn un countplot ile veri gorsellestirme
sns.countplot(x=df["sex"], data=df) # ilk arguman=degisken, ikinci arg=df goster. !!!(x, y, data isaretleme lazim)!!!
plt.show()

# matplotlib de yapma
df['sex'].value_counts().plot(kind='bar')
plt.show()


#############################################
# Sayısal Değişken Görselleştirme
#############################################

sns.boxplot(x=df["total_bill"]) # boxplot ile gorsellestirme
plt.show()

df["total_bill"].hist() # pandas ta histogram gorsellestirme
plt.show()



#####################################################################
# GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ADVANCED FUNCTIONAL EDA)
#####################################################################
# 1. Genel Resim
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
# 3. Sayısal Değişken Analizi (Analysis of Numerical Variables)
# 4. Hedef Değişken Analizi (Analysis of Target Variable)
# 5. Korelasyon Analizi (Analysis of Correlation)


#############################################
# 1. Genel Resim
#############################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T # sayisal degiskenlerin betimsel istatistikleri
df.isnull().values.any()
df.isnull().sum()

# kalıp olarak df check fonk
def check_df(dataframe, head=5):
    print("##################### Shape #########################")
    print(dataframe.shape)
    print("##################### Types #########################")
    print(dataframe.dtypes)
    print("##################### Head ##########################")
    print(dataframe.head(head))
    print("##################### Tail ##########################")
    print(dataframe.tail(head))
    print("##################### NA ############################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df) # df de ki degisiklikleri goster

# farkli df lerde deneyelim
df = sns.load_dataset("tips")
check_df(df)

df = sns.load_dataset("flights")
check_df(df)



###################################################################
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
###################################################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

# kategorik degisken tipleri : bool, object, category

# bir takim denemeler
df["survived"].value_counts() # survived value frekansi
df["sex"].unique() # sex unique degerleri
df["class"].nunique() # class nunique/number unique yani unique degerlerinin frekansi/sayisi


# buyuk veri setlerinde kategorik degiskenleri bilmek ya da yakalamak zordur bunu sistematik olarak secebilmek lazim
# bazi int64 veri tipleri de aslinda sayisal ama kategorik olabiliyor survived gibi. 0-1 ler ama 2 tip kategorisi var sadece

# df de tip bilgisine gore kategorik degiskenleri getir
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

# str(df[col].dtypes) # acilimi
#str(df["sex"].dtypes) in ["object"] # True

# type i int veya float ama aslinda kategorik degisken diye bul
# tipi int veya float olani bul unique frekansi belli degerin altinda olani sec
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

# # !!!!!!****** DİKKAT ******!!!!!!
# !!!!!! normalde kategorik olup aslinda gereksiz degerleri olan/kategorik olmayanlari sec !!!!!!
# object ve category tipinde olanlar ama bu degiskenlerin sinif sayisi cok fazla olabilir
# ornegin name isim degiskeni olsa 891 unique olacakti, bu kategorik degildir. olcum degeri tasimaz
# "kardinalitisi yuksek degiskenler/cardinality" denir. olculemeyecek/olcum degeri tasimayacak kadar/aciklanabilirlik tasimayacak kadar
# sinifi vardir anlamina gelir. bir kategorik degiskenin 50 sinifi olmasi cok yuksek ihtimalle bilgi tasimadigi anlamina gelebilir
# cokca essiz degere sahipse dolayisiyla bu sayisal degiskendir
# dolayisiyla programarik olarakta bu degiskenleri yakalayip kategorik olmayacak sekilde saymak lazim.
# df columns da gez str olarak category veya object olanlarda nunique degeri 20 ustu olanlari sec
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]] # bu df de yok

# elimizde tipi kategorik olmayip aslinda kendisi kategorik olanlari bulduk
# tipi kategorik olup kendisi aslinda kategorik olmayanlari bulduk

cat_cols = cat_cols + num_but_cat # normalde kategorik olanlari gizli kategoriklerle topladik

# tipi kategorik olup aslinda kategorik olmayanlari cikarma
cat_cols = [col for col in cat_cols if col not in cat_but_car] # cat_cols da gez cat_but_car icinde yoksa kalanlari sec

# df icinde bizim yorumladigimiz kategorik degiskenleri getir
df[cat_cols]

# kendi yorumumuzla sectigimiz degiskenlerin nunique degerlerini kontrol ederek tutarliliga bakalim
df[cat_cols].nunique() # cat_cols sec unique frekanslari getir

# yorumlarimizin disinda kalan yani kategorik olmayanlari getir
[col for col in df.columns if col not in cat_cols] # cat_cols icinde olmayan sec df ten getir


# kategorikleri sectik diger adima gecis. birlikte fonk yazalim


# girilen degisken degerlerinde her siniftan kac tane var
df["survived"].value_counts() # survived icindeki deger frekansi
# siniflarin yuzdelik bilgisi yazdir
100 * df["survived"].value_counts() / len(df) # survived degiskeni siniflari 100 carp ve df in boyutuna bol
# fonk yukaridaki islemi yaptiralim
# dataframe ve col_name disaridan cagrilacak degiskenler, Ratio sabit
# print (yazdir) pd.DataFrame ile df olustur {dict icine yaz} ilk key:value = col_name degiskeni: dataframe df te her sinif kac tane sec
# ikinci key: value = "Ratio" sabit degiskeni: degiskendeki siniflarin yuzdelik bilgisi bul
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

cat_summary(df, "sex") # fonk a df teki sex degiskenini cagir


# simdi ise tum columns icin for dongusu ile fonk hepsinde uygulayalim
for col in cat_cols:
    cat_summary(df, col)



# veri gorsellestirmesi ekleyelim. tek + kategorik degisken = seaborn countplot ile sutun grafigi cizilmeli
def cat_summary(dataframe, col_name, plot=False): # plot:False on tanimli deger False olmali ki True iken kontrol saglayalim
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot: # plot True iken seaborn dan countplot ile sutun grafigi
        sns.countplot(x=dataframe[col_name], data=dataframe) # x= dataframe in ilgili degiskeni, data=olusturdugumuz dataframe
        plt.show(block=True) # block=True : grafik kapanana kadar kodlari calismasini durdurur

cat_summary(df, "sex", plot=True) # sex degiskenini cagir, plot True dondur sutun grafigi versin

# şimdi ise bunu bütün dataframe içindeki değişkenlere uygulayalım.

# for col in cat_cols:
#     cat_summary(df, col, plot=True)

# burada birkac grafigi bize verdikten sonra hata aldik.
# hatayi aldigimiz degiskeni bulalim. adult_male degiskeni hata verdi, type bool
# countplot fonk da type bool degiskenlerini genellememis
# bu yuzden bool tipini bulup grafigini olusturmadan diger degiskene gecelim.
for col in cat_cols:
    if df[col].dtypes == "bool":
        print(col + " : type bool\n##########################################") # bool degiskeni olani ayirt edelim
    else:
        cat_summary(df, col, plot=True)
###


# type bool degiskeninin degerlerini type int a cevirdi
df["adult_male"].astype(int)

# simdi de bunu dongu icine yazalim ki her degiskende type bool kontrol edip var ise onun degerleri degistirsin
for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int) # artik type bool gorunce farkli oldugunu ekrana yazdirmayip degisken degistiriyoruz
        cat_summary(df, col, plot=True)

    else:
        cat_summary(df, col, plot=True)



# mantiksal olarak usttekine gore daha karmasik olan ama fonk icinde/basinda type bool kontrolunu if ile yaptik, ic ice kosul
def cat_summary(dataframe, col_name, plot=False):

    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int) # fonk icinde once type bool kosul kontrolu sonra dataframe icine hem degiskenler ve frekanslari hem de standartlastirma islemi uyguladik

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)
# simdi de karmasik olan bu fonk da az once hata veren adult_male degiskenini deniyoruz
# karmasik ve uzun da olsa ise yaradi ama biz her zaman en kisayi secmeliyiz ki farkli ozellikler cikip bize hata olusturmasin
cat_summary(df, "adult_male", plot=True)



# bizim standart kullanmamiz gereken cat_summary fonk ustte de kullanmis oldugumuz gibi bu fonk dur
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

cat_summary(df, "sex") # deneme



###############################################################
# 3. Sayısal Değişken Analizi (Analysis of Numerical Variables)
###############################################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

# onceki yazmis oldugumuz fonk getir ustune devam et simdilik
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]



df[["age","fare"]].describe().T # betimsel istatistikler

num_cols = [col for col in df.columns if df[col].dtypes in ["int","float"]] # num_cols a int ve float olanlari ata
num_cols = [col for col in num_cols if col not in cat_cols] # kategorik olmayanlari cat_cols kontrolu ile sec, filtreleme yap sayisal bul

# yeni fonk yaz, argumanlar dataframe, numerical_col olustur
def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99] # ceyreklik
    print(dataframe[numerical_col].describe(quantiles).T) # betimsel istatistigi fonk a uyarla/describe().T bul

num_summary(df, "age") # deneme age

# dongu ile yukarida filtreleyerek buldugumuz tum sayisal degiskenlere ustteki betimsel istatistigi bul fonk calistir
for col in num_cols:
    num_summary(df, col)



# grafiklestirelim / sayisal oldugundan histogram grafigi
# ustteki fonk plot=False ekledik, grafik olusturmak icin fonk disinda cagrildiginda True dondurecez
def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot: # True ise
        dataframe[numerical_col].hist() # olusturulan dataframe icinde numerical_col ile cagrilan degiskenin hist grafigi ciz
        plt.xlabel(numerical_col) # x eksenini isimlendir, degiskenin adi olsun
        plt.title(numerical_col) # title gir, degiskenin adi olsun
        plt.show(block=True) # grafigi bize goster, block=True : grafik kapanana kadar kodlari calismasini durdurur

# age degiskeninde deneyelim
num_summary(df, "age", plot=True)

# tum degiskenlerde calistiralim
for col in num_cols:
    num_summary(df, col, plot=True)



###########################################################
# Değişkenlerin Yakalanması ve İşlemlerin Genelleştirilmesi
###########################################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df .info()


# !!!!!! fonksiyon tanımlayacaz / documentation yazdık !!!!!!

# ayarlardan docstring type : numpy olarak değiştirmeyi unutma, fonk içeriğine denir/documentation
# help(grab_col_names) # oluşturduğumuz fonksiyonu kullanacak başka kişiler için documentation ı görmek

# docstring

def grab_col_names(dataframe, cat_th=10,  car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    ------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.

    """
    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < 10 and dataframe[col].dtypes in ["int", "float"]]

    cat_but_car = [col for col in dataframe.columns if
                   dataframe[col].nunique() > 20 and str(dataframe[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_but_car = grab_col_names(df)


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)



def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in num_cols:
    num_summary(df, col, plot=True)



# BONUS
df = sns.load_dataset("titanic")
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

cat_cols, num_cols, cat_but_car = grab_col_names(df)

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

for col in cat_cols:
    cat_summary(df, col, plot=True)


for col in num_cols:
    num_summary(df, col, plot=True)





#########################################################
# 4. Hedef Değişken Analizi (Analysis of Target Variable)
#########################################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")


for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

def grab_col_names(dataframe, cat_th=10,  car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    ------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.

    """
    # cat_cols, cat_but_car
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)

df.head()


# bu "titanic" veri setinde hedef değişkenimiz "survived" dır. Yani hayatta kalma  oranlarını diğer değişkenlerin oranları ile yorumlayacaz
df["survived"].value_counts()
cat_summary(df, "survived")

####################################################
# Hedef Değişkenin Kategorik Değişkenler ile Analizi
####################################################
# groupby a ort alacağımız değişkeni girdik agg olarak target/hedef değişkeni girdik

df.groupby("sex")["survived"].mean() # hedef değişken ile sex değişkeninin ort groupby ile deneyimledik
df.groupby("sex").agg({"survived": "mean"})  # diğer kullanım

# hedef değişkenin bütün kategorik değişkenler ile ort değerlendirmek için fonk oluşturalım
# argümanları gir, üstteki gibi groupby ile ilgili değişkenin ort al, dataframe oluştur ve bunu kaydet, yazdır
def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n") # üstteki groupby ı girdik


target_summary_with_cat(df, "survived", "pclass") # hedef değişken için oluşturduğumuz fonk pclass ile deneyimledik

# şimdi oluşturduğumuz fonksiyonu, önceden filtrelediğimiz kategorik değişkenleri içeren cat_cols ile bütün değişkenlere uyguladık
for col in cat_cols:
    target_summary_with_cat(df, "survived", col)



##################################################
# Hedef Değişkenin Sayısal Değişkenler ile Analizi
##################################################
# target/hedef değişkeni groupby a aldık, agg kısmına ise ort alacağımız değişkenleri girdik

df.groupby("survived")["age"].mean() # target ı groupby a aldık, oranlanacak olan değişkeni agg girdik
df.groupby("survived").agg({"age":"mean"}) # diğer kullanım

# hedef değişkenin bütün sayısal değişkenler ile ort değerlendirmek için fonk oluşturduk
def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n") # üstteki groupby ı girdik


target_summary_with_num(df, "survived","age") # hedef değişkeni age ile değerlendirdik

# şimdi bu fonksiyonu bütün değişkenlerde değerlendiriyoruz
for col in num_cols:
    target_summary_with_num(df, "survived", col)





#################################################
# 5. Korelasyon Analizi (Analysis of Correlation)
#################################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/breast_cancer.csv") # meme kanseri ile alakalı veri seti .csv dosyası
df = df.iloc[:, 1:-1]  # 1 den -1 olan kolonları sil. sebebi ise alakasız değişkenler(id ve unnamed 32 değişkenleri)
df.head()

# ısı haritası oluşturma / yüksek korelasyona sahip değişkenlerden birini silecez, detaylı bir istatistik işlemi yok
# her zaman yüksek korelasyona sahip değişkenlerden birini silme işlemi her zaman yapılacak diye bir şey yok

# Korelasyon değişkenlerin birbiri ile ilişkisini ifade eder. -1 ile +1 arasında değer alır. -1 e veya +1 e yaklaştıkça
# ilişkinin şiddeti kuvvetlenir. 2 değişkenin arasındaki ilişki pozitif ise buna pozitif korelasyon denir. Ve bir değişkenin
# değeri arttıkça diğerinin de değeri artar. İki değişken arasındaki ilişki negatif ise bir değişkenin değeri artarken diğer
# değişkenin değeri azalır. Bu korelasyonlarda. 0 civarındaki bir korelasyon değeri korelasyon olmadığı anlamına gelir.


# numerik degiskenleri seciyor
num_cols = [col for col in df.columns if df[col].dtype in [int, float]] #

# korelasyon hesapliyoruz
corr = df[num_cols].corr() #  .corr: korelasyon hesabi

# grafik ölçüleri girme
sns.set(rc={'figure.figsize': (12, 12)}) # grafik 12x12
sns.heatmap(corr, cmap="RdBu") # sns heatmap: ısı haritası
plt.show()


#######################
# Yüksek Korelasyonlu Değişkenlerin Silinmesi
#######################

# korelasyonun değerinin + - olması önemsiz, mutlak yapıp şiddetli olanları silecez
cor_matrix = df.corr().abs() # .abs mutlak değer yapma


# istatistik girişte de öğretildiği gibi bu matriste orta çizgi ve altı değerler ile üstü değerler tekrar ediyor
# bu sebeple bunları silmemiz gerekiyor. numpy dan bir fonk kullanacaz

#           0         1         2         3
# 0  1.000000  0.117570  0.871754  0.817941
# 1  0.117570  1.000000  0.428440  0.366126
# 2  0.871754  0.428440  1.000000  0.962865
# 3  0.817941  0.366126  0.962865  1.000000


#     0        1         2         3
# 0 NaN  0.11757  0.871754  0.817941
# 1 NaN      NaN  0.428440  0.366126
# 2 NaN      NaN       NaN  0.962865
# 3 NaN      NaN       NaN       NaN


# yukarıdaki matrisi ilk halinden ikinci haline temizlemek için numpy dan bir fonk kullanacaz
#
# 1) (np.ones(cor_matrix.shape), k=1) 1 lerden oluşan ve oluşturmuş olduğumuz matrisin boyutunda bir numpy array oluşturuyoruz
# 2) .astype(bool) bu numpy arrayini bool a çeviriyoruz
# 3) np.triu yukarıdaki 2. matrisin haline çeviriyoruz

# 4) önca bu matrisi oluşturmak için boş bir numpy array i oluşturduk. True False ile doldurduk. Köşegen elemanlarından
#    kurtulduktan sonra kalanlar True değerleri olacağından dolayı bunu cor_matrix matrisinde "where" şu koşulu sağlayanları
#    getir diye gönderdiğimizde son halini elde ettik.

# 5) şimdi ise kalan üst kısımdaki şiddeti yüksek korelasyonu olan değerleri silmek için işlem yapacağız
# 6) drop_list liste oluştur. upper_triangle_matrix.columns kolonlarında gez,
#    any(upper_triangle_matrix[col]>0.90) o kolon değerlerinden herhangi biri 0.90 dan büyük ise seç
# 7) cor_matrix[drop_list] cor_matrix içinde drop_list fonk uygula/korelasyon 0.90 büyükleri seç
# 8) df.drop(drop_list, axis=1) ile koşula uygun değerleri sildik

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col]>0.90) ]
cor_matrix[drop_list]
df.drop(drop_list, axis=1)


# Yukarıda uygulamış olduğumuz işlemleri fonksiyonlaştırıp her ihtiyacımız olduğunda çağırabilelim
# 1) high_correlated_cols fonk oluştur, plot=False default, corr_th=0.90 argümanları gir
# 2) corr = dataframe.corr() korelasyon oluştur
# 3) cor_matrix = corr.abs() mutlak değerini al
# 4) upper_triangle_matrix yukarıdaki gibi köşegen elemanlarına düzeltme işlemi
# 5) drop_list ile belirlediğimiz eşik değeri üstünde olanları silme işlemi
# 6) if plot: görselleştirme işlemi
# 7) return drop_list silme işlemini döndürme
def high_correlated_cols(dataframe, plot=False, corr_th=0.90): # plot=False görsel, corr_th=0.90 korelasyon eşik değeri
    corr = dataframe.corr() # korelasyon oluştur
    cor_matrix = corr.abs() # mutlak değerini al
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool)) # köşegen düzeltme işlemi
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)] # eşit değerine göre silme
    if plot: # görselleştirme işlemi
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list # silme işlemini döndürme


high_correlated_cols(df) # df i çağır kendisine bu fonk uygulasın
drop_list = high_correlated_cols(df, plot=True) # df e silme uygulanmamış halini kaydetme, görsel oluşturma
df.drop(drop_list, axis=1) # silme işlemini uyguluyoruz
high_correlated_cols(df.drop(drop_list, axis=1), plot=True) # silme uygulanmış halinin görseli oluşturma

# kaggle veri setinde hızlı örnek uygulama

# Yaklaşık 600 mb'lık 300'den fazla değişkenin olduğu bir veri setinde deneyelim.
# https://www.kaggle.com/c/ieee-fraud-detection/data?select=train_transaction.csv

df = pd.read_csv("datasets/fraud_train_transaction.csv") # df csv oku
len(df.columns) # df değişken sayısı
df.head()

drop_list = high_correlated_cols(df, plot=True) # fonk silme uygulanmamış görsel oluştur

len(df.drop(drop_list, axis=1).columns) # silme uygula değişken sayısı gör

type(adsa) #


