-- Для билетов с кодом бронирования '58DF57' выбрать имена пассажиров, номер рейса, дату-время отправления
-- и дату-время прибытия
EXPLAIN (ANALYSE)
SELECT
    t.passenger_name,
    f.flight_no,
    f.actual_arrival,
    f.actual_departure
FROM tickets t
    INNER JOIN ticket_flights tf ON t.ticket_no = tf.ticket_no
    INNER JOIN flights f ON tf.flight_id = f.flight_id
WHERE t.book_ref = '58DF57'

CREATE INDEX ix_tickets_book_ref ON tickets (book_ref)

-- Execution Time before index create: 65.626 ms
-- Execution Time after index create: 0.103 ms
