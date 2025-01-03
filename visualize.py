import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📂 Veri dosyasını yükleyelim
df = pd.read_csv("data/pit_stops_2023_Monza.csv")

# 🔹 Pit stop süreleri histogramı
plt.figure(figsize=(10, 5))
sns.histplot(df["pit_stop_time"], bins=15, kde=True)
plt.title("🏎️ Pit Stop Süreleri Dağılımı")
plt.xlabel("Pit Stop Süresi (s)")
plt.ylabel("Frekans")
plt.show()

# 🔹 Takımların ortalama pit stop süreleri
plt.figure(figsize=(10, 5))
team_avg_pit = df.groupby("team")["pit_stop_time"].mean().sort_values()
sns.barplot(x=team_avg_pit.index, y=team_avg_pit.values)
plt.xticks(rotation=45)
plt.title("Takımlara Göre Ortalama Pit Stop Süreleri")
plt.xlabel("Takım")
plt.ylabel("Ortalama Pit Stop Süresi (s)")
plt.show()

print("✅ Veri görselleştirme tamamlandı!")
