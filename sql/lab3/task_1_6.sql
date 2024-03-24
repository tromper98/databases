-- Выбрать номер рейса, дату-время отправления и количество свободных мест класса Эконом для перелёта
-- из Владивостока в Москву ближайшим рейсом
-- Следует выбирать только рейсы в состоянии 'Scheduled'
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
  AND EXTRACT(EPOCH FROM (CURRENT_DATE - COALESCE(actual_departure, scheduled_departure))) = (SELECT
                                                                                                  MIN(EXTRACT(EPOCH FROM
                                                                                                              (CURRENT_DATE - COALESCE(actual_departure, scheduled_departure))))
                                                                                              FROM flights f_t
                                                                                              WHERE f_t.departure_airport = 'VVO'
                                                                                                AND f_t.arrival_airport IN ('SVO', 'VKO', 'DME')
                                                                                                AND f_t.status = 'Scheduled'
                                                                                              )
;
