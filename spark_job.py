from pyspark.sql import SparkSession

# Apache Spark oturumunu başlat
spark = SparkSession.builder.appName("F1RaceAnalysis").getOrCreate()

# CSV verilerini yükle
pit_stops_df = spark.read.csv("data/pit_stops_2023_Monza.csv", header=True, inferSchema=True)
fastest_laps_df = spark.read.csv("data/fastest_laps_2023_Monza.csv", header=True, inferSchema=True)
weather_df = spark.read.csv("data/weather_2023_Monza.csv", header=True, inferSchema=True)

# ⚡ En hızlı tur atan sürücüleri analiz et
fastest_laps_df.groupBy("driver").avg("lap_time").orderBy("avg(lap_time)").show()

# ☁️ Hava durumu ve pit stop ilişkisi
weather_df.join(pit_stops_df, "session_time").groupBy("weather_condition").avg("pit_stop_time").show()

# 🔥 Takımlara göre ortalama pit stop süreleri
pit_stops_df.groupBy("team").avg("pit_stop_time").orderBy("avg(pit_stop_time)").show()

print("✅ Apache Spark analizleri tamamlandı!")
