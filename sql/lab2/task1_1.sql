-- Задача: Выбрать всю информацию о рейсах (flights), в которых номер рейса (flight_no) заканчивается на '488'
SELECT *
FROM flights
WHERE flight_no LIKE '%488'