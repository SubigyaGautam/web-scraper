# This repo contains various webscraping tools that can be handy :)

# Flight Data Scraper

`scrape_flights.py` is a Python script designed to scrape detailed flight information from ScholarTrip and save the results to a CSV file. This tool helps users efficiently find and compare the cheapest flights across multiple departure locations and destinations, covering various date ranges.

# Purpose

The primary aim of this script is to streamline the process of identifying the most cost-effective flights by consolidating data into a single CSV file. By automating the data collection from multiple sources and date ranges, the script eliminates the need for repetitive manual searches on the website, providing a comprehensive overview of flight options in one place.

# Features

- **Comprehensive Search**: Retrieve flight details from multiple departure locations to various destinations.
- **Flexible Date Ranges**: Specify both departure and arrival dates with optional ranges to capture a wider set of flight options.
- **CSV Output**: Automatically save the collected flight data into a CSV file for easy analysis and comparison.

# How to Execute

To run the script, use the following command:

```bash
python scrape_flights.py --from-locations <Source-Airportcodes> --to-locations <Destination-Airportcodes> --departure-date "<date>" --arrival-date "<date>" --output-file <name-of-output-file>

Parameters
--from-locations: Space-separated list of departure airport codes (e.g., JFK IAH MSY).
--to-locations: Space-separated list of arrival airport codes (e.g., ICN KTM).
--departure-date: The departure date with optional range (e.g., "2024-12-17 3d").
--arrival-date: The arrival date with optional range (e.g., "2025-01-09 2d").
--output-file: The CSV file to save the results (e.g., new_flights.csv).
```

Example
```bash
python scrape_flights.py --from-locations JFK IAH MSY --to-locations MSD --departure-date "2024-12-17 3d" --arrival-date "2025-01-09 3d" --output-file new_flights.csv
```

# Flight Data
Example:
``bash
 python scrape_flights.py --from-locations MSY --to-locations EWR --departure-date "2024-12-17" --arrival-date "2025-01-09" --output-file new_flights.csv
``

| Price | Outbound Route | Inbound Route | Airlines | Outbound Departure Time | Outbound Date | Outbound Duration | Inbound Departure Time | Inbound Date | Inbound Duration | Outbound Layover | Inbound Layover |
|-------|----------------|---------------|----------|-------------------------|---------------|-------------------|------------------------|--------------|------------------|------------------|-----------------|
| 103.0 | MSY - EWR | EWR - MSY | Spirit Airlines / Spirit Airlines | 7:00 AM | Tue, Dec 17 | 3h 2m | 10:03 PM | Thu, Jan 9 | 3h 2m | [] | [] |
| 113.0 | MSY - EWR | EWR - MSY | Spirit Airlines / Spirit Airlines | 3:20 PM | Tue, Dec 17 | 3h 2m | 10:03 PM | Thu, Jan 9 | 3h 2m | ['2h 17m layover in Orlando International Airport'] | [] |
| 118.0 | MSY - EWR | EWR - MSY | Spirit Airlines / Spirit Airlines | 7:00 AM | Tue, Dec 17 | 3h 2m | 1:11 PM | Thu, Jan 9 | 3h 2m | [] | ['2h 54m layover in Hartsfield Jackson Atlanta International Airport'] |

# Notes
- Prices are in USD.
- Layover times indicate the duration of stops at respective airports.
- This data provides a general idea. Always check the airline's website for the most up-to-date information on flight schedules and availability.

# Other tools coming soon...
