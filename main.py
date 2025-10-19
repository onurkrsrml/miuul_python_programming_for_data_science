
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

###########################################################
# Sayılar (Numbers) ve Karakter Dizileri (Strings)
###########################################################

print(9) #integer
print(9.2) #float

type("Mrb")

###########################################################
# Atamalar ve Değişkenler (Assignments and Variables)
###########################################################

a = 9

b = "Onur"

c = 10

d = a - c

###########################################################
# Virtual Environment (Sanal Ortam)  ve (Package Management) Paket Yönetimi
###########################################################

# Sanal ortamların listelenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create –n myenv

# Sanal ortamı aktif etme:
# conda activate myenv

# Yüklü paketlerin listelenmesi:
# conda list

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

# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme:
# pip install pandas

# Paket yükleme versiyona göre:
# pip install pandas==1.2.1

# Paketlerin tümünü aktarma:
# conda env export > environment.yaml/.yml
# pip env export > requirement.txt

# Sanal ortam silme:
# conda env remove -n myenv

# Paketleri dosyadan sanal ortama yükleme:
# conda env create -f environment.yaml

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

###########################################################
# VERİ YAPILARI (DATA STRUCTURES)
###########################################################

# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set

###########################################################
# Veri Yapılarına Giriş ve Hızlı Özet
###########################################################



########################################################################################################################
# 3.1 - FONKSİYONLAR
########################################################################################################################

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









###################################
# !!!!!!****** DİKKAT ******!!!!!!
###################################
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

#                                ARALARINDAKİ FARKLAR
# numpy              -       pandas series                  -       pandas dataframe
# tek boyutlu                tek boyutlu                            çok boyutlu
# vektör                     sütun                                  tablo
# sadece sayısal             hem sayısal hem kategorik              hem sayısal hem kategorik


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

# !!!!!!****** DİKKAT ******!!!!!!
# survived kırılımında ortalamasını ve sayısını alarak sex index i ve new_age ile class kategorik değişkenleri ile değerleri bul
# df.pivot_table("survived", "sex", ["new_age", "class"], aggfunc = ["mean", "count"])

# pd.set_option('display.width', 500) # ekrandaki çıktı gösterim miktarı ayarı. \ ile alt satıra geçmeden kurtulma

# ignore_index=True # df index i siralar-resetler

# df[].value_counts() ile kategorilere erisim ve sayisi sikca kullanilacak!!!

# !!!!!!!!!!!!!!!!!! kalıp olarak df check fonk !!!!!!!!!!!!!!!!!!
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
