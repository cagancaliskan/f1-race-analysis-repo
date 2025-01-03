from pyspark.sql import SparkSession

# Apache Spark oturumunu başlat
spark = SparkSession.builder.appName("F1PitStopAnalysis").getOrCreate()

# CSV verisini yükle
df = spark.read.csv("data/pit_stops_2023_Monza.csv", header=True, inferSchema=True)

# En hızlı pit stop yapan sürücüyü bul
df.groupBy("driver").avg("pit_stop_time").orderBy("avg(pit_stop_time)").show()

# Takımlara göre ortalama pit stop süresi
df.groupBy("team").avg("pit_stop_time").orderBy("avg(pit_stop_time)").show()

# Pit stop süresi 2.5 saniyenin altında olanları filtrele
df.filter(df["pit_stop_time"] < 2.5).show()

print("✅ Apache Spark analizleri tamamlandı!")
