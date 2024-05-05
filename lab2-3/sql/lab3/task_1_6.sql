-- Выбрать номер рейса, дату-время отправления и количество свободных мест класса Эконом для перелёта
-- из Владивостока в Москву ближайшим рейсом
-- Следует выбирать только рейсы в состоянии 'Scheduled'
EXPLAIN (ANALYSE )
SELECT
    f.flight_no,
    f.status,
    COALESCE(f.actual_departure, f.scheduled_departure) AS departure_time,
    s2.total_seats - COALESCE(s1.booked_seats, 0) AS free_seats
FROM flights f
    LEFT JOIN ( -- get total seats in aircraft per fare condition
    SELECT
        a.aircraft_code,
        s.fare_conditions,
        COUNT(s.seat_no) AS total_seats
    FROM aircrafts a
        INNER JOIN seats s ON a.aircraft_code = s.aircraft_code
    GROUP BY s.fare_conditions, a.aircraft_code
    ) s2 ON f.aircraft_code = s2.aircraft_code
    LEFT JOIN ( -- get booked seats count
    SELECT
        f.flight_id,
        s.fare_conditions,
        COUNT(s.seat_no) AS booked_seats
    FROM boarding_passes bp
        INNER JOIN flights f ON bp.flight_id = f.flight_id
        INNER JOIN seats s ON (f.aircraft_code = s.aircraft_code AND s.seat_no = bp.seat_no)
    GROUP BY f.flight_id, s.fare_conditions
    ) s1 ON f.flight_id = s1.flight_id AND s1.fare_conditions = s2.fare_conditions

WHERE f.departure_airport = 'VVO'
  AND f.arrival_airport IN ('SVO', 'VKO', 'DME')
  AND f.status = 'Scheduled'
  AND s2.fare_conditions = 'Economy'
  ORDER BY (CURRENT_DATE - scheduled_departure) DESC
LIMIT 1
;

CREATE INDEX ix_flights_departure_airport_arrival_airport ON flights (departure_airport, arrival_airport)
CREATE INDEX ix_seats_fare_conditions ON seats (fare_conditions)
CREATE INDEX ix_flights_aircraft_code ON flights (aircraft_code)
CREATE INDEX ix_flights_status ON flights (status)

DROP INDEX ix_flights_departure_airport_arrival_airport
DROP INDEX ix_seats_fare_conditions
DROP INDEX ix_flights_aircraft_code
DROP INDEX ix_flights_status