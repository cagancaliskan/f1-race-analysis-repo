import fastf1
import pandas as pd

# Önbelleği etkinleştir (veri çekmeyi hızlandırır)
fastf1.Cache.enable_cache('cache')

def fetch_f1_data(year, grand_prix):
    """Belirtilen yıl ve yarış için verileri çeker ve kaydeder."""
    session = fastf1.get_session(year, grand_prix, 'R')
    session.load()
    
    # 📊 Pit Stop verileri
    pit_stops = session.pit_stops
    
    # 🔹 Hız ve Sektör Verileri
    laps = session.laps
    fastest_laps = laps.pick_fastest()
    
    # ☁️ Hava Durumu Verileri
    weather_data = session.weather_data

    # 📂 CSV olarak kaydet
    pit_stops.to_csv(f'data/pit_stops_{year}_{grand_prix}.csv', index=False)
    fastest_laps.to_csv(f'data/fastest_laps_{year}_{grand_prix}.csv', index=False)
    weather_data.to_csv(f'data/weather_{year}_{grand_prix}.csv', index=False)
    
    print(f"✅ {year} {grand_prix} verileri güncellendi ve kaydedildi!")

# Örnek: 2023 Monza GP'sinin verilerini çek
fetch_f1_data(2023, "Monza")
