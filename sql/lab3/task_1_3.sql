-- Выбрать все «счастливые» коды бронирования со списками имён пассажиров в каждом из них
-- На одно бронирование со «счастливым» кодом должен быть ровно один результат запроса
-- Под «счастливым» кодом понимается код, в котором первые три символа совпадают с тремя последними (например, '0DA0DA')
EXPLAIN (ANALYSE) SELECT
    t.book_ref,
    string_agg(passenger_name, ', ') AS passengers
FROM tickets t
WHERE SUBSTRING(t.book_ref for 3) = SUBSTRING(t.book_ref from 4 for 6)
GROUP BY t.book_ref