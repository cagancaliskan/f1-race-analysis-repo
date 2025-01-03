-- 1️⃣ En hızlı pit stop yapan ilk 5 sürücü
SELECT driver, MIN(pit_stop_time) AS fastest_pit
FROM pit_stop_data
GROUP BY driver
ORDER BY fastest_pit ASC
LIMIT 5;

-- 2️⃣ En çok pit stop yapan sürücüler
SELECT driver, COUNT(*) AS total_pit_stops
FROM pit_stop_data
GROUP BY driver
ORDER BY total_pit_stops DESC;

-- 3️⃣ Ortalama pit stop süresine göre takımlar
SELECT team, AVG(pit_stop_time) AS avg_pit_time
FROM pit_stop_data
GROUP BY team
ORDER BY avg_pit_time ASC;

-- 4️⃣ Pit stop süreleri 2.5 saniyeden kısa olan sürücüler
SELECT driver, pit_stop_time
FROM pit_stop_data
WHERE pit_stop_time < 2.5
ORDER BY pit_stop_time ASC;
