# Flight Scraper

This script scrapes flight details from ScholarTrip and saves the top 3 cheapest flights to a CSV file.

## How to Execute

To run the script, use the following command:

```bash
python scrape_flights.py --from-locations <comma_separated_airport_codes> --to-locations <comma_separated_airport_codes> --departure-date <date_with_days_range> --arrival-date <date_with_days_range> --output-file <output_file.csv>

Parameters
--from-locations: Comma-separated list of departure airport codes (e.g., JFK,IAH,MSY).
--to-locations: Comma-separated list of arrival airport codes (e.g., ICN).
--departure-date: The departure date with optional range (e.g., "2024-12-17 3d"). This means the script will consider dates from 3 days before to 3 days after the specified date.
--arrival-date: The arrival date with optional range (e.g., "2025-01-09 2d"). This means the script will consider dates from 2 days before to 2 days after the specified date.
--output-file: The CSV file to save the results (e.g., new_flights.csv).

Example
To scrape flight details for flights from JFK, IAH, and MSY to ICN with a departure date of December 17, 2024, and an arrival date of January 9, 2025, including a 3-day range before and 2-day range after, and save the results to new_flights.csv, use the following command:

python scrape_flights.py --from-locations JFK,IAH,MSY --to-locations ICN --departure-date "2024-12-17 3d" --arrival-date "2025-01-09 2d" --output-file new_flights.csv
