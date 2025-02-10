
##################################################
# Sayılar (Numbers) ve Karakter Dizileri (Strings)
##################################################

print(9) #integer
print(9.2) #float

type(9)
type(9.2)
type("Mrb")

#####################################################
# Atamalar ve Değişkenler (Assignments and Variables)
#####################################################

a = 9
a

b = "Onur"
b

c = 10

d = a - c

###############################################
# Virtual Environment (Sanal Ortam)  ve (Package Management) Paket Yönetimi
###############################################

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
# conda upgrade –all

# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme:
# pip install pandas

# Paket yükleme versiyona göre:
# pip install pandas==1.2.1

# Paketlerin tümünü aktarma:
# conda env export > environment.yaml ya da .yml uzantılı
# pip env export > requirement.txt

# Sanal ortam silme:
# conda env remove -n myenv

# Paketleri dosyadan sanal ortama yükleme:
# conda env create -f environment.yaml

