# TASK 6: CSV Parsing [COMPLETED]
import csv
from typing import List
from tabulate import tabulate
from city import City
from country import Country
from country import add_city_to_country


def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    :return: A list of City objects.
    """
    cities = []
    with open(path_to_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            city_ascii = row['city_ascii']
            coordinates = f"({row['lat']}, {row['lng']})"
            country_name = row['country']
            iso3 = row['iso3']
            population = (row['population'])
            city_id = int(row['id'])

            # Create Country instance if not already created
            if not Country.name_to_countries.get(country_name):
                Country(country_name, iso3)

            city = City(city_ascii, coordinates, country_name, population, city_id)
            add_city_to_country(city, country_name, iso3)
            cities.append(city)



# Test case 1: World CSV file 
if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    for country in Country.name_to_countries.values():
        country.print_cities()
        print("\n")
