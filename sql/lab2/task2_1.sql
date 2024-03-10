-- Задача: Для всех рейсов Домодедово, находящихся в статусе 'Delayed', поменять статус на 'Cancelled'
UPDATE flights
SET
    status = 'Cancelled'
WHERE departure_airport = 'DME'
  AND status = 'Delayed'
;

-- Обратный SQL-запрос:
UPDATE flights
SET
    status = 'Delayed'
WHERE flight_id IN (
                    348,
                    761,
                    974,
                    2469,
                    5377,
                    5858
    )