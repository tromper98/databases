-- Для всех типов самолётов выбрать количество мест по классам обслуживания
-- Ожидаемая схема набора результатов: (aircraft_code, fare_conditions, seat_count)
EXPLAIN (ANALYSE)
SELECT
    s.aircraft_code,
    s.fare_conditions,
    COUNT(*) AS seat_count
FROM seats s
GROUP BY s.aircraft_code, s.fare_conditions
