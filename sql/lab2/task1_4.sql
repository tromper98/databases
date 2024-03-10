-- Задача: Выбрать идентификаторы и стоимости 10 самых дорогостоящих бронирований (bookings)
SELECT
    book_ref,
    total_amount
FROM bookings
ORDER BY total_amount DESC
LIMIT 10