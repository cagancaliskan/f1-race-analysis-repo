import fastf1
import pandas as pd

# Önbelleği etkinleştir (veri çekmeyi hızlandırır)
fastf1.Cache.enable_cache('cache')

def fetch_f1_data(year, grand_prix):
    """Belirtilen yıl ve yarış için telemetri verilerini çeker ve kaydeder."""
    session = fastf1.get_session(year, grand_prix, 'R')
    session.load()
    
    # Tur süreleri ve pit stop verilerini al
    laps = session.laps
    pit_stops = session.pit_stops
    
    # CSV olarak kaydet
    laps.to_csv(f'data/laps_{year}_{grand_prix}.csv', index=False)
    pit_stops.to_csv(f'data/pit_stops_{year}_{grand_prix}.csv', index=False)
    
    print(f"✅ {year} {grand_prix} verileri kaydedildi!")

# Örnek: 2023 Monza GP'sinin verilerini çek
fetch_f1_data(2023, "Monza")
