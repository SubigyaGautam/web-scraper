import argparse
import csv
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_flights(from_location, to_location, departure_date, return_date):
    og_departure_date = departure_date
    chrome_driver_path = r'D:\chromedriver-win32\chromedriver-win32\chromedriver.exe'  # Update this path

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')  # Disable GPU for better performance in headless mode
    chrome_options.add_argument('--disable-extensions')  # Disable extensions for faster browsing

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = f'https://scholartrip.com/search/{from_location}-{to_location}/{departure_date}/{return_date}'
    driver.get(url)

    logging.info(f'Scraping flights from {from_location} to {to_location} for {og_departure_date} - {return_date}')

    time.sleep(10)

    result_cards = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'search-result-card'))
    )
    logging.info(f'Component loaded successfully')

    flights = []
    for card in result_cards:
        try:
            price_element = card.find_element(By.CSS_SELECTOR, '.sr-price-wrap__price-full')
            price_text = price_element.text.strip() if price_element else 'Price not available'
            price = float(re.sub(r'[^\d.]', '', price_text)) if price_text != 'Price not available' else None

            leg_items = card.find_elements(By.CSS_SELECTOR, '.fl-leg__item')
            legs = []
            for i, leg in enumerate(leg_items):
                airline_logo_element = leg.find_element(By.CSS_SELECTOR, '.fl-leg__logo')
                airline_name = airline_logo_element.get_attribute('data-original-title')

                leg_data = leg.find_element(By.CSS_SELECTOR, '.leg-data')
                
                departure_col = leg_data.find_elements(By.CSS_SELECTOR, '.leg-data__col')[0]
                arrival_col = leg_data.find_elements(By.CSS_SELECTOR, '.leg-data__col')[-1]

                departure_time = departure_col.find_element(By.CSS_SELECTOR, '.leg-data__time').text.strip()
                departure_date = departure_col.find_element(By.CLASS_NAME, 'leg-data__date').text.strip()

                departure_iata = departure_col.find_element(By.CSS_SELECTOR, '.leg-data__iata span').text.strip()

                arrival_time = arrival_col.find_element(By.CSS_SELECTOR, '.leg-data__time').text.strip()
                arrival_iata = arrival_col.find_element(By.CSS_SELECTOR, '.leg-data__iata span').text.strip()
                # Use JavaScript to extract the date
                departure_date = driver.execute_script(
                    "return arguments[0].querySelector('.leg-data__col:first-child .leg-data__date').textContent;", 
                    leg_data
                ).strip()
                
                arrival_date = driver.execute_script(
                    "return arguments[0].querySelector('.leg-data__col:last-child .leg-data__date').textContent;", 
                    leg_data
                ).strip()

                duration = driver.execute_script("""
                    return document.querySelector('.fl-leg__fl-length span').textContent;
                """)

                layover_elements = leg_data.find_elements(By.CSS_SELECTOR, '.leg-data__stop-icon')
                layovers = [layover.get_attribute('data-original-title') for layover in layover_elements if layover.get_attribute('data-original-title')]
                
                legs.append({
                    'Leg': f"{'Outbound' if i == 0 else 'Return'}",
                    'Airline Name': airline_name,
                    'Departure IATA': departure_iata,  # Keep this as the first IATA
                    'Arrival IATA': arrival_iata,      # Move this to be the second IATA
                    'Departure Date': departure_date,
                    'Departure Time': departure_time,
                    'Arrival Date': arrival_date,
                    'Arrival Time': arrival_time,
                    'Duration': duration,
                    'Layovers': layovers,
                    'Price': price,
                })
            flights.append(legs)

        except Exception as e:
            logging.error(f"Error extracting information from a search result card: {e}")

    logging.info(f'Got {len(flights)} flights from {from_location} to {to_location} for {og_departure_date} - {return_date}')
    driver.quit()
    return flights

def parse_datetime(datetime_str):
    # Example: "4:30 PM<i>+2d</i>"
    parts = datetime_str.split('<i>')
    time = parts[0].strip()
    date = '+2d' if len(parts) > 1 else ''
    return time, date

def parse_date_with_range(date_range_str):
    """Parses a date with an optional range (e.g., '2024-12-16 3d')."""
    parts = date_range_str.split()
    date = datetime.strptime(parts[0], '%Y-%m-%d')
    range_days = int(parts[1][:-1]) if len(parts) > 1 and parts[1].endswith('d') else 0
    return date, range_days

def convert_price(price_str):
    try:
        # Remove any non-numeric characters like commas, currency symbols, etc.
        return float(re.sub(r'[^\d.]', '', price_str))
    except (ValueError, TypeError):
        # If conversion fails, return None or a default value
        return None

def main():
    parser = argparse.ArgumentParser(description='Scrape and find flights from ScholarTrip.')
    
    parser.add_argument('--from-locations', type=str, nargs='+', required=True, help='List of IATA codes for departure locations')
    parser.add_argument('--to-locations', type=str, nargs='+', required=True, help='List of IATA codes for arrival locations')
    parser.add_argument('--departure-date', type=str, required=True, help='Departure date with optional range (e.g., "2024-12-16 3d")')
    parser.add_argument('--arrival-date', type=str, required=True, help='Arrival date with optional range (e.g., "2025-01-10 2d")')
    parser.add_argument('--output-file', type=str, required=True, help='Output CSV file')

    args = parser.parse_args()

    # Parse departure and arrival dates with ranges
    departure_date, departure_range = parse_date_with_range(args.departure_date)
    arrival_date, arrival_range = parse_date_with_range(args.arrival_date)
    
    all_results = []

    # Scrape flights within the date ranges
    for from_location in args.from_locations:
        for to_location in args.to_locations:
            for i in range(-departure_range, departure_range + 1):
                current_departure_date = departure_date + timedelta(days=i)
                formatted_departure_date = current_departure_date.strftime('%Y-%m-%d')

                for j in range(-arrival_range, arrival_range + 1):
                    current_arrival_date = arrival_date + timedelta(days=j)
                    formatted_arrival_date = current_arrival_date.strftime('%Y-%m-%d')

                    logging.info(f"Scraping flights from {from_location} to {to_location} for {formatted_departure_date} to {formatted_arrival_date}")
                    flights = scrape_flights(from_location, to_location, formatted_departure_date, formatted_arrival_date)

                    # if flights:
                    #     sorted_flights = sorted(flights, key=lambda x: float(x['Price']) if x['Price'] else float('inf'))
                    #     top_3_flights = sorted_flights[:3]
                    #     all_results.extend(top_3_flights)
                    all_results.append(flights)

    # Writing results to CSV
    logging.info(f'Writing {len(all_results)} flights to CSV')

    with open(args.output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            'Price',
            'Outbound Route',
            'Inbound Route',
            'Airlines',
            'Outbound Departure Time','Outbound Date','Outbound Duration'
            'Inbound Departure Time', 'Inbound Date','Inbound Duration',
            'Outbound Layover', 'Inbound Layover'
        ])
        
        for flight_group in all_results:
            for flight_pair in flight_group:
                outbound = next((f for f in flight_pair if f['Leg'] == 'Outbound'), None)
                inbound = next((f for f in flight_pair if f['Leg'] == 'Return'), None)

                if outbound and inbound:
                    price = outbound['Price']  # Assuming price is the same for both legs

                    writer.writerow([
                        price,
                        f"{outbound['Departure IATA']} - {outbound['Arrival IATA']}",
                        f"{inbound['Departure IATA']} - {inbound['Arrival IATA']}",
                        f"{outbound['Airline Name']} / {inbound['Airline Name']}",
                        outbound['Departure Time'],
                        outbound['Departure Date'],
                        outbound['Duration'],
                        inbound['Departure Time'],
                        inbound['Departure Date'],
                        inbound['Duration'],
                        outbound['Layovers'],  # Outbound Layover
                        inbound['Layovers']    # Inbound Layover
                    ])
                elif outbound:
                    # Handle one-way trips (only outbound flight)
                    price = convert_price(outbound['Price'])
                    writer.writerow([
                        price,
                        f"{outbound['Departure IATA']} - {outbound['Arrival IATA']}",
                        '',  # No inbound flight
                        outbound['Airline Name'],
                        outbound['Departure Time'],
                        outbound['Departure Date'],
                        outbound['Duration'],
                        '',  # No inbound departure time
                        '',  # No inbound date
                        '',  # No inbound duration
                        outbound['Layovers'],  # Outbound Layover
                        ''  # No inbound layovers
                    ])
                elif inbound:
                    # Handle return-only trips
                    price = convert_price(inbound['Price'])
                    writer.writerow([
                        price,
                        '',  # No outbound flight
                        f"{inbound['Departure IATA']} - {inbound['Arrival IATA']}",
                        inbound['Airline Name'],
                        '',  # No outbound departure time
                        '',  # No outbound date
                        '',  # No outbound duration
                        inbound['Departure Time'],
                        inbound['Departure Date'],
                        inbound['Duration'],
                        '',  # No outbound layovers
                        inbound['Layovers']  # Inbound Layover
                    ])
if __name__ == '__main__':
    main()
