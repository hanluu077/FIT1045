# Task 7: Shortest Path [IN PROGRESS]
"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a function to create a path, encoded as an Itinerary, that is shortest for some Vehicle.

@file path_finding.py
"""
import math
import networkx

from city import City, get_city_by_id
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley
from csv_parsing import create_cities_countries_from_csv


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Itinerary:  # Itinerary | None
    """
    Returns a shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: A shortest path from departure to arrival, or None if there is none.
    """
    # return iternary when chosenvehicle == CrappyCrepeCar
    if isinstance(vehicle, CrappyCrepeCar):
        return Itinerary([from_city, to_city])  # Itinerary __init__(self, cities: list[City])
    
    # chosenCehicle != CrappyCrepeCar = contains other 
    else: 
        g = networkx.Graph()  
        cities_id = list(City.id_to_cities.keys())
        cities_len = len(cities_id)

        # Ceate individual nodes for all city
        for city in cities_id:
            g.add_node(city)

    # NEED TO GO THROUGH ALL THE CITY NODES 

    # FIND OUT HOW LONG IT TAKES --> travel_time = vehicle.compute_travel_time(city1, city2)
        travel_time = vehicle.compute_travel_time(city1, city2)
   
    # USE NETWORK TO FIND SHORTEST PATH (USE ID TO FIND THE LEAST TIME)
        path_sequence_ids = networkx.shortest_path(g, source=from_city.city_id, target=to_city.city_id) 
        

if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")

    from_cities = set()
    for city_id in [1036533631, 1036142029, 1458988644]:
        from_cities.add(get_city_by_id(city_id))

    #we create some vehicles
    vehicles = create_example_vehicles()

    to_cities = set(from_cities)
    for from_city in from_cities:
        to_cities -= {from_city}
        for to_city in to_cities:
            print(f"{from_city} to {to_city}:")
            # for test_vehicle in vehicles:
            #     shortest_path = find_shortest_path(test_vehicle, from_city, to_city)
            #     print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
            #           f" hours with {test_vehicle} with path {shortest_path}.")

