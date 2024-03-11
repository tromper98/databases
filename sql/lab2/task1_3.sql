-- Задача: Выбрать всю информацию о рейсах (flights) на самолёте Сухой Суперджет-100,
-- для которых аэропорт Чебоксар является пунктом отправления либо прибытия
SELECT
    f.*
FROM flights f
WHERE departure_airport = (SELECT
                               ad_t.airport_code
                           FROM airports_data ad_t
                           WHERE city ->> 'ru' = 'Чебоксары'
                           )
  AND f.aircraft_code = (SELECT
                             ad_t.aircraft_code
                         FROM aircrafts_data ad_t
                         WHERE model ->> 'ru' = 'Сухой Суперджет-100'
                         )

UNION ALL

SELECT
    f.*
FROM flights f
WHERE arrival_airport = (SELECT
                             ad_t.airport_code
                         FROM airports_data ad_t
                         WHERE city ->> 'ru' = 'Чебоксары'
                         )
  AND f.aircraft_code = (SELECT
                             ad_t.aircraft_code
                         FROM aircrafts_data ad_t
                         WHERE model ->> 'ru' = 'Сухой Суперджет-100'
                         )