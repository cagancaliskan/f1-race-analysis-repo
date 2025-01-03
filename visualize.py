import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🎨 Seaborn fütüristik tema
sns.set_style("darkgrid")

# 📂 Verileri yükle
df_pit = pd.read_csv("data/pit_stops_2023_Monza.csv")
df_speed = pd.read_csv("data/fastest_laps_2023_Monza.csv")
df_weather = pd.read_csv("data/weather_2023_Monza.csv")

# 🔹 Hız ve sektör zamanları çizimi
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_speed, x="lap_number", y="lap_time", hue="driver", palette="coolwarm")
plt.title("🏎️ En Hızlı Turlar")
plt.savefig("figures/fastest_laps.png")

# 🔥 Hava durumu ve pit stop ilişkisi
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_weather, x="weather_condition", y="pit_stop_time", palette="viridis")
plt.title("☁️ Hava Durumu ve Pit Stop Süreleri")
plt.savefig("figures/weather_vs_pit.png")

print("✅ Gelişmiş grafikler oluşturuldu ve kaydedildi!")
