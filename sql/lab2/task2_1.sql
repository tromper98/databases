-- Задача: Для всех рейсов Домодедово, находящихся в статусе 'Delayed', поменять статус на 'Cancelled'
UPDATE flights
SET status = 'Cancelled'
WHERE (departure_airport = 'DME' OR arrival_airport = 'DME')
  AND status = 'Delayed'
;

-- Обратный SQL-запрос:
UPDATE flights
SET status = 'Delayed'
WHERE flight_id IN (
                348,
                761,
                974,
                2469,
                5377,
                5858,
                34275,
                36780,
                46165,
                53170,
                59329
    )

-- Доработать запросы с учетом того, что должны проверяться departure_airport и arrival_airport