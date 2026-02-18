-- Daily trip count
SELECT
  DATE(lpep_pickup_datetime) AS day,
  COUNT(*) AS trip_count
FROM ny_taxi.green_taxi_trips
GROUP BY day
ORDER BY day;

-- Busiest borough
SELECT
  borough,
  COUNT(*) AS total_trips
FROM ny_taxi.green_taxi_trips
GROUP BY borough
ORDER BY total_trips DESC;
