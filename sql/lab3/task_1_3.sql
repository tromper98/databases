-- Выбрать все «счастливые» коды бронирования со списками имён пассажиров в каждом из них
-- На одно бронирование со «счастливым» кодом должен быть ровно один результат запроса
-- Под «счастливым» кодом понимается код, в котором первые три символа совпадают с тремя последними (например, '0DA0DA')
EXPLAIN (ANALYSE)
SELECT
    t.book_ref,
    STRING_AGG(passenger_name, ', ') AS passengers
FROM tickets t
WHERE SUBSTRING(t.book_ref FOR 3) = SUBSTRING(t.book_ref FROM 4 FOR 6)
GROUP BY t.book_ref