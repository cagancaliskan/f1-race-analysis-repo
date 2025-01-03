# 🏎️ Formula 1 Yarış Stratejisi Analizi

## 📌 Proje Hakkında
Bu proje, Formula 1 yarışlarında **pit stop süreleri, hava durumu, hız ve sektör zamanlarının yarış sonucuna etkisini analiz etmeyi** amaçlamaktadır.  
**Python, SQL ve Apache Spark kullanarak büyük veri analizi ve görselleştirme gerçekleştirilmiştir.**  

## 🚀 Kullanılan Teknolojiler
- **Python** (FastF1, Pandas, NumPy, Matplotlib, Seaborn)
- **SQL** (PostgreSQL, MySQL)
- **Apache Spark** (Büyük veri analizi)
- **Seaborn & Matplotlib** (Fütüristik veri görselleştirme)
- **Git & GitHub** (Sürüm kontrolü)

## 📊 Yapılan Analizler
### 🏁 **Pit Stop Süreleri vs. Yarış Sonucu**
- En hızlı pit stop yapan takımların yarış sonucuna etkisi  
- Lastik değişim stratejileri ve kazanan sürücüler arasındaki ilişki  

### ☁️ **Hava Durumu ve Lastik Seçimi**
- Islak ve kuru hava koşullarında en uygun lastik türü  
- Hangi takım hava değişikliklerine daha hızlı tepki veriyor?  

### ⚡ **Hız ve Sektör Zamanları**
- En hızlı sektör zamanları ve hangi sürücülerin avantajlı olduğu  
- Hangi takım hangi virajda daha iyi performans gösteriyor?  



## 🔥 Nasıl Çalıştırılır?
### 1️⃣ **Gerekli kütüphaneleri yükleyin**
```bash
pip install -r requirements.txt
```
### 2️⃣ **F1 yarış verilerini çekin**
```
python scripts/data_fetch.py
```
3️⃣ SQL analizlerini çalıştırın
```
sqlite3 queries.sql
```
4️⃣ Apache Spark analizlerini çalıştırın
```
python spark_job.py
```
5️⃣ Grafikleri oluşturun
```
python visualize.py
```


##📷 Örnek Grafikler

###🏎️ Pit Stop Süreleri Dağılımı

###📊 Takımlara Göre Ortalama Pit Stop Süreleri
