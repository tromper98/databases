-- Задача: Выбрать идентификаторы самолётов, в которых есть посадочные места с редким классом 'Comfort'
-- (вместо более привычных 'Economy' / 'Business')
SELECT DISTINCT
    ad.aircraft_code
FROM aircrafts_data ad
    INNER JOIN seats s ON ad.aircraft_code = s.aircraft_code
WHERE s.fare_conditions = 'Comfort'
