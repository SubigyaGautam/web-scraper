# web-scraper-flight-details
This is used to scrape and get flight details

How to execute - 

python scrape_flights.py --from-locations <comma_seprated_airport_codes>  --to-locations <comma_seprated_airport_codes> --departure-date <date_with_how many_days_before_or_after> --arrival-date <date_with_how many_days_before_or_after> --output-file new_flights.csv

example : python scrape_flights.py --from-locations JFK IAH MSY  --to-locations ICN --departure-date "2024-12-17 3d" --arrival-date "2025-01-9 2d" --output-file new_flights.csv
