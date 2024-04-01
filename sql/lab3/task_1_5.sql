-- Выбрать номер рейса и дату-время отправления для 10 рейсов, принёсших наибольшую выручку
-- Следует выбирать только рейсы в состоянии 'Arrived'
-- Даты отправления следует выбирать фактические, а не запланированные
EXPLAIN (ANALYSE)
SELECT
    flight_no,
    actual_arrival,
    actual_departure
FROM flights f
    INNER JOIN (SELECT
                    f_t.flight_id,
                    SUM(tf_t.amount) AS flight_total
                FROM ticket_flights tf_t
                    INNER JOIN flights f_t ON tf_t.flight_id = f_t.flight_id
                WHERE f_t.status = 'Arrived'
                GROUP BY f_t.flight_id
                ORDER BY flight_total DESC
                LIMIT 10
                ) s1 ON s1.flight_id = f.flight_id

--
SELECT
    flight_no,
    actual_arrival,
    actual_departure,
    f_t.flight_id,
    SUM(tf_t.amount) AS flight_total
FROM ticket_flights tf_t
    INNER JOIN flights f_t ON tf_t.flight_id = f_t.flight_id
WHERE f_t.status = 'Arrived'
GROUP BY f_t.flight_id
ORDER BY flight_total DESC
LIMIT 10

