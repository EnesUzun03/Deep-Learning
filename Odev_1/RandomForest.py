import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score,
                             classification_report, confusion_matrix)

# Verileri içinde bulunduran tablomu çektim
df = pd.read_csv("sample_data/data.csv")

df.drop(columns=["id"], inplace=True, errors = "ignore")# Tablo üzerinde id sütununu sildim gereksiz bir sütün olduğu için
df.dropna(axis=1, how="all", inplace=True)# içerisinde eksik veri bulunan sütunları sildik burda 

print("Veri Seti Boyutu:", df.shape)
print("Sınıf Dağılımı:\n", df["diagnosis"].value_counts())

le = LabelEncoder() # LabelEncoder nesnesi oluşturdum , labelEncoder nesnesi kategorik sütünlları sayısal veriye dönüştürür
#Burada hedef sütun olan diagnosis (tanı) sütunudur bu sütun içerisinde M (Malignant-Kötü huylu tümör) ve B (Benign-iyi huylu tümör) bulunur.
#Ve bulunan B ve M için alfabetik sırada sayısal atama yapılır B - 0 M - 1 olur ve sütun değiştirilir
df["diagnosis"] = le.fit_transform(df["diagnosis"])

#Burada girdi değişkenleri içe çıktı değişkenini ayırıyorum
X = df.drop(columns=["diagnosis"])#diagnosis yani tanı harici tüm tabloyu aldık burası girdi katmanı için kullanılanak özellikler kısmını belirtir 
y = df["diagnosis"] # sadece diagnosis sütununu atarız burası da çıktı sonuç katmanını beltirtir.

# Test ve eğitim verisini bölme burada yapılıyor. Burada %80 eğitim %20 test olacak şekilde ve 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, 
    random_state=42, #random_state=42 kısmında veriyi bölmek için kullanılacak rastgeleliği sabitliyoruz.Bu şekilde verimiz birebir aynı şekilde bölünür.
    stratify=y) #stratify=y ile de tablodaki dağılımı koruyarak eğitim ve test verimizi dağıtıyoruz

#Model seçimi ve inject edilmesi , burada random forest modelini seçtim. Farklı sayıda karar ağacından oluşan bu yapıda farklı farklı tahmiinlerde bulunur karar ağacları
#bu tahminlerin hangisi daha çok oy alırsa sonuç o olur, Burada n_estimators karar ağac sayısıdır burada genelde karar ağacı artarsa sonuçta iyileşme oluyormuş
#bende o yüzden 100-1000-10000 olacak şekilde 3 defa denedim ancak sonuçta bir iyileşme görmedim.
model = RandomForestClassifier(n_estimators=100, random_state=42)
#modelin eğitilmesi
model.fit(X_train, y_train)

#Modelin tahminde bulunması burada X_test verisi üzerinden tahminde bulunucak hasta mı değil mi diye
y_pred = model.predict(X_test)

#test verisinin gerçek sonucu olan y_pred ile y_test verilerinin karşılaştırılması ile bulunan accuracy_score,precision_score,recall_score ve f1_score bulunması
print("\n========= METRİKLER =========")
print(f"Accuracy  : {accuracy_score(y_test, y_pred):.4f}")# burada Accuracy gerçek değerler ile tahmmin değerlerini karşılaştırır. Toplam tahminlerimizin % kaçı doğru buluruz
print(f"Precision : {precision_score(y_test, y_pred):.4f}") #Precision  modelin hasta (M-1 çünkü) dediklerinin % kaçı gerçekten hasta
print(f"Recall    : {recall_score(y_test, y_pred):.4f}") #Recall modelin hasta olanların % kaçına hasta dediğimizi buluruz 
print(f"F1-Score  : {f1_score(y_test, y_pred):.4f}") # f1 skoru precision ve recall’ın harmonik ortalamasıdır
