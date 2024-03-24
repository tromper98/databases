-- Задача: Выбрать всю информацию о рейсах (flights), для которых аэропорт Краснодар
-- является пунктом отправления либо прибытия
SELECT
    f.*
FROM flights f
WHERE departure_airport = (SELECT
                               ad.airport_code
                           FROM airports_data ad
                           WHERE city ->> 'ru' = 'Краснодар'
                           )

UNION ALL

SELECT
    f.*
FROM flights f
WHERE arrival_airport = (SELECT
                             ad.airport_code
                         FROM airports_data ad
                         WHERE city ->> 'ru' = 'Краснодар'
                         )
CREATE INDEX ix_flights_departure_airport ON flights (departure_airport)
CREATE INDEX ix_flights_arrival_airport ON flights (arrival_airport)

EXPLAIN (ANALYZE ) SELECT
    f.*
FROM flights f
WHERE departure_airport = 'KRR'
    OR arrival_airport = 'KRR'
;


SELECT
 ad.airport_code
FROM airports_data ad
WHERE city ->> 'ru' = 'Краснодар'
;
-- KRR