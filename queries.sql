-- 🏎️ 1️⃣ En hızlı pit stop yapan ilk 5 sürücü
SELECT driver, MIN(pit_stop_time) AS fastest_pit
FROM pit_stop_data
GROUP BY driver
ORDER BY fastest_pit ASC
LIMIT 5;

-- ⚡ 2️⃣ En hızlı sektör zamanları
SELECT driver, MIN(sector_1_time + sector_2_time + sector_3_time) AS fastest_lap
FROM fastest_laps_data
GROUP BY driver
ORDER BY fastest_lap ASC
LIMIT 5;

-- ☁️ 3️⃣ Hava durumu ve lastik seçimi analizi
SELECT weather_condition, COUNT(*) AS race_count, AVG(pit_stop_time) AS avg_pit
FROM weather_data
JOIN pit_stop_data ON weather_data.session_time = pit_stop_data.session_time
GROUP BY weather_condition
ORDER BY avg_pit ASC;

-- 🔥 4️⃣ Takımlara göre ortalama pit stop süreleri
SELECT team, AVG(pit_stop_time) AS avg_pit_time
FROM pit_stop_data
GROUP BY team
ORDER BY avg_pit_time ASC;
