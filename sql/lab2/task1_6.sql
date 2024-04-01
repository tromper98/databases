-- Задача: Выбрать идентификаторы самолётов, в которых есть посадочные места с редким классом 'Comfort'
-- (вместо более привычных 'Economy' / 'Business')
EXPLAIN (ANALYZE ) SELECT DISTINCT
    ad.aircraft_code
FROM aircrafts_data ad
    INNER JOIN seats s ON ad.aircraft_code = s.aircraft_code
WHERE s.fare_conditions = 'Comfort'
-- Подумать как можно оптимизировать этот запрос
;
CREATE INDEX ix_seats_aircraft_code_fare_conditions ON seats (aircraft_code, fare_conditions);
DROP INDEX ix_seats_aircraft_code_fare_conditions

-- Before Index Create: 0.296 ms
-- After Index ix_aircraft_code_fare_condition Create: : 0.089 ms