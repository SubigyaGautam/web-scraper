# Flight Data Scraper

## Overview

`scrape_flights.py` is a Python script designed to scrape detailed flight information from ScholarTrip and save the results to a CSV file. This tool helps users efficiently find and compare the cheapest flights across multiple departure locations and destinations, covering various date ranges.

## Purpose

The primary aim of this script is to streamline the process of identifying the most cost-effective flights by consolidating data into a single CSV file. By automating the data collection from multiple sources and date ranges, the script eliminates the need for repetitive manual searches on the website, providing a comprehensive overview of flight options in one place.

## Features

- **Comprehensive Search**: Retrieve flight details from multiple departure locations to various destinations.
- **Flexible Date Ranges**: Specify both departure and arrival dates with optional ranges to capture a wider set of flight options.
- **CSV Output**: Automatically save the collected flight data into a CSV file for easy analysis and comparison.

## Benefits

- **Efficiency**: Avoids the need for multiple visits to the website by consolidating flight information into a single file.
- **Convenience**: Simplifies the process of comparing flight options and finding the best deals.
- **Flexibility**: Allows for customized searches across different dates and locations.

With `scrape_flights.py`, users can easily gather and analyze flight data, making travel planning more efficient and straightforward.


## How to Execute
To run the script, use the following command:

```bash
python scrape_flights.py --from-locations <Source-Airportcodes> --to-locations <Destination-Airportcodes> --departure-date "<date>" --arrival-date "<date>" --output-file <name-of-output-file>

```

```bash
Parameters
--from-locations: Comma-separated list of departure airport codes (e.g., JFK,IAH,MSY).
--to-locations: Comma-separated list of arrival airport codes (e.g., ICN).
--departure-date: The departure date with optional range (e.g., "2024-12-17 3d"). This means the script will consider dates from 3 days before to 3 days after the specified date.
--arrival-date: The arrival date with optional range (e.g., "2025-01-09 2d"). This means the script will consider dates from 2 days before to 2 days after the specified date.
--output-file: The CSV file to save the results (e.g., new_flights.csv).


Example
To scrape flight details for flights from JFK, IAH, and MSY to ICN with a departure date of December 17, 2024, and an arrival date of January 9, 2025, including a 3-day range before and 2-day range after, and save the results to new_flights.csv, use the following command:
```
```bash
python scrape_flights.py --from-locations JFK,IAH,MSY --to-locations ICN --departure-date "2024-12-17 3d" --arrival-date "2025-01-09 2d" --output-file new_flights.csv
```

# Flight Data Scraper

## Overview

`scrape_flights.py` is a Python script designed to scrape detailed flight information from ScholarTrip and save the results to a CSV file. This tool helps users efficiently find and compare the cheapest flights across multiple departure locations and destinations, covering various date ranges.

## Purpose

The primary aim of this script is to streamline the process of identifying the most cost-effective flights by consolidating data into a single CSV file. By automating the data collection from multiple sources and date ranges, the script eliminates the need for repetitive manual searches on the website, providing a comprehensive overview of flight options in one place.

## Features

- **Comprehensive Search**: Retrieve flight details from multiple departure locations to various destinations.
- **Flexible Date Ranges**: Specify both departure and arrival dates with optional ranges to capture a wider set of flight options.
- **CSV Output**: Automatically save the collected flight data into a CSV file for easy analysis and comparison.

## Benefits

- **Efficiency**: Avoids the need for multiple visits to the website by consolidating flight information into a single file.
- **Convenience**: Simplifies the process of comparing flight options and finding the best deals.
- **Flexibility**: Allows for customized searches across different dates and locations.

With `scrape_flights.py`, users can easily gather and analyze flight data, making travel planning more efficient and straightforward.


## How to Execute
To run the script, use the following command:

```bash
python scrape_flights.py --from-locations <Source-Airportcodes> --to-locations <Destination-Airportcodes> --departure-date "<date>" --arrival-date "<date>" --output-file <name-of-output-file>

```

```bash
Parameters
--from-locations: Comma-separated list of departure airport codes (e.g., JFK,IAH,MSY).
--to-locations: Comma-separated list of arrival airport codes (e.g., ICN).
--departure-date: The departure date with optional range (e.g., "2024-12-17 3d"). This means the script will consider dates from 3 days before to 3 days after the specified date.
--arrival-date: The arrival date with optional range (e.g., "2025-01-09 2d"). This means the script will consider dates from 2 days before to 2 days after the specified date.
--output-file: The CSV file to save the results (e.g., new_flights.csv).


Example
To scrape flight details for flights from JFK, IAH, and MSY to ICN with a departure date of December 17, 2024, and an arrival date of January 9, 2025, including a 3-day range before and 2-day range after, and save the results to new_flights.csv, use the following command:
```
```bash
python scrape_flights.py --from-locations LFT,IAH,MSY --to-locations KTM --departure-date "2024-12-17 3d" --arrival-date "2025-01-09 3d" --output-file new_flights.csv
```

# Flight Data
Example:
``bash
 python scrape_flights.py --from-locations MSY --to-locations JFK --departure-date "2024-12-17" --arrival-date "2025-01-09" --output-file new_flights.csv
``

| Price | Outbound Route | Inbound Route | Airlines | Outbound Departure Time | Outbound Date | Outbound Duration | Inbound Departure Time | Inbound Date | Inbound Duration | Outbound Layover | Inbound Layover |
|-------|----------------|---------------|----------|-------------------------|---------------|-------------------|------------------------|--------------|------------------|------------------|-----------------|
| 103.0 | MSY - EWR | EWR - MSY | Spirit Airlines / Spirit Airlines | 7:00 AM | Tue, Dec 17 | 3h 2m | 10:03 PM | Thu, Jan 9 | 3h 2m | [] | [] |
| 113.0 | MSY - EWR | EWR - MSY | Spirit Airlines / Spirit Airlines | 3:20 PM | Tue, Dec 17 | 3h 2m | 10:03 PM | Thu, Jan 9 | 3h 2m | ['2h 17m layover in Orlando International Airport'] | [] |
| 118.0 | MSY - EWR | EWR - MSY | Spirit Airlines / Spirit Airlines | 7:00 AM | Tue, Dec 17 | 3h 2m | 1:11 PM | Thu, Jan 9 | 3h 2m | [] | ['2h 54m layover in Hartsfield Jackson Atlanta International Airport'] |

## Notes
- Prices are in USD.
- Layover times indicate the duration of stops at respective airports.
- Ensure to check the airline's website for the most up-to-date information on flight schedules and availability.
