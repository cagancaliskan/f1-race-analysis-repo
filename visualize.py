import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 🎨 Fütüristik Neon Tema
plt.style.use("dark_background")

# 🌈 Renk paleti (Neon etkisi için)
neon_colors = ["#00FFFF", "#FF00FF", "#FFD700", "#FF4500", "#32CD32"]

# 📂 Verileri yükleyelim
df_pit = pd.read_csv("data/pit_stops_2023_Monza.csv")
df_speed = pd.read_csv("data/fastest_laps_2023_Monza.csv")
df_weather = pd.read_csv("data/weather_2023_Monza.csv")

# 🔹 En Hızlı Turlar Grafiği (Neon Efekti)
plt.figure(figsize=(12, 6))
for i, driver in enumerate(["Verstappen", "Hamilton", "Leclerc"]):
    sns.lineplot(x=df_speed["lap_number"], y=df_speed[driver], color=neon_colors[i], linewidth=2.5, label=driver)

plt.title("🏎️ En Hızlı Turlar", fontsize=14, color="white")
plt.xlabel("Tur Numarası", fontsize=12, color="white")
plt.ylabel("Tur Süresi (s)", fontsize=12, color="white")
plt.grid(color="#444444", linestyle="dotted")
plt.legend(facecolor="black", edgecolor="white", fontsize=10)
plt.savefig("figures/neon_fastest_laps.png", dpi=300)

# 🔥 Pit Stop ve Hava Durumu İlişkisi (Neon Bar Grafiği)
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_weather, x="weather_condition", y="pit_stop_time", palette=neon_colors)
plt.title("☁️ Hava Durumu ve Pit Stop Süreleri", fontsize=14, color="white")
plt.xlabel("Hava Durumu", fontsize=12, color="white")
plt.ylabel("Pit Stop Süresi (s)", fontsize=12, color="white")
plt.grid(color="#444444", linestyle="dotted")
plt.savefig("figures/neon_weather_vs_pit.png", dpi=300)

# ⏳ Hız Göstergesi (Custom Speedometer)
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
angles = np.linspace(0, np.pi, 6)
labels = ["1", "2", "3", "4", "5", "6"]
ax.set_xticks(angles)
ax.set_xticklabels(labels, color="cyan", fontsize=14)

# Gösterge içi çizgiler
for i, angle in enumerate(angles):
    ax.plot([0, angle], [0, 1], color="cyan", lw=2)

ax.set_yticklabels([])
ax.spines["polar"].set_visible(False)
ax.set_facecolor("black")
plt.title("🚀 Ortalama Hız Göstergesi", color="white", fontsize=16)
plt.savefig("figures/neon_speedometer.png", dpi=300)

print("✅ Fütüristik grafikler oluşturuldu ve kaydedildi!")
