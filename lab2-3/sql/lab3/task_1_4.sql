-- Выбрать номер рейса, дату-время отправления и дату-время прибытия последнего по времени отправления рейса,
-- прибывшего из Краснодара в Калининград
-- Следует выбирать только рейсы в состоянии 'Arrived'
-- Даты отправления и прибытия следует выбирать фактические, а не запланированные
EXPLAIN ANALYZE
SELECT
    flight_no,
    MAX(actual_departure) AS last_departure,
    MAX(actual_arrival) AS last_arrival
FROM flights f
WHERE status = 'Arrived'
  AND f.arrival_airport = 'KGD'
  AND f.departure_airport = 'KRR'
GROUP BY flight_no
;

-- код аэропорта Краснодара: KRR
-- код аэропорта Калининграда: KGD