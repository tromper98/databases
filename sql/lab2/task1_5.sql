-- Задача: Выбрать имена и контактные данные всех пассажиров, указанных в самом дорогостоящем бронировании
-- (среди всех, что есть в базе данных)
EXPLAIN (ANALYZE
    )SELECT
    t.passenger_name,
    t.contact_data
FROM tickets t
WHERE t.book_ref = (SELECT
                        book_ref
                    FROM bookings
                    ORDER BY total_amount DESC
                    LIMIT 1
                    )