# Task 3: Itinerary [COMPLETED]

import math
from city import City, create_example_cities, get_cities_by_name


class Itinerary():
    """
    A sequence of cities.
    """

    def __init__(self, cities: list[City]) -> None:
        """
        Creates an itinerary with the provided sequence of cities,
        conserving order.
        :param cities: a sequence of cities, possibly empty.
        :return: None
        """
        self.cities = cities

    def total_distance(self) -> int:
        """
        Returns the total distance (in km) of the itinerary, which is
        the sum of the distances between successive cities.
        :return: the total distance.
        """
        total_distance = 0
        for i in range(len(self.cities) - 1):
            total_distance += (self.cities[i].distance(self.cities[i+1]))
        return total_distance


    def append_city(self, city: City) -> None:
        """
        Adds a city at the end of the sequence of cities to visit.
        :param city: the city to append
        :return: None.
        """
        self.cities.append(city)

    def min_distance_insert_city(self, city: City) -> None:
        """
        Inserts a city in the itinerary so that the resulting
        total distance of the itinerary is minimised.
        :param city: the city to insert
        :return: None.
        """

        min_distance = math.inf
        index_to_insert = -1

        for i in range(len(self.cities)):
            if i == 0:
                distance_to_next = city.distance(self.cities[i])
            elif i == len(self.cities) - 1:
                distance_to_next = city.distance(self.cities[i])
            else:
                distance_to_next = city.distance(self.cities[i]) + self.cities[i].distance(self.cities[i+1]) - self.cities[i-1].distance(self.cities[i])

            if distance_to_next < min_distance:
                index_to_insert = i
                min_distance = distance_to_next

        self.cities.insert(index_to_insert, city)

    def __str__(self) -> str:
        """
        Returns the sequence of cities and the distance in parentheses
        For example, "Melbourne -> Kuala Lumpur (6368 km)"
        :return: a string representing the itinerary.
        """
        itinerary_str = ""
        total_distance = 0
        
        if len(self.cities) == 0:
            return f"({total_distance} km)"

        for i in range(len(self.cities)):
            itinerary_str += self.cities[i].name
            if i != len(self.cities) - 1:
                itinerary_str += " -> "
            # total_distance = self.total_distance()
                # total_distance 
                # print(self.total_distance())

        return itinerary_str + " (" + str(self.total_distance()) + " km)"

# Example usage
if __name__ == "__main__":
    # Create a list of cities
    cities = create_example_cities()

    # Create an itinerary with two cities
    test_itin = Itinerary([get_cities_by_name("Melbourne")[0], get_cities_by_name("Kuala Lumpur")[0]])

    # Print the itinerary
    print(test_itin)

    # Add a city to the itinerary
    test_itin.append_city(get_cities_by_name("Baoding")[0])
    print(test_itin)

    # Insert a city into the itinerary
    test_itin.min_distance_insert_city(get_cities_by_name("Sydney")[0])
    print(test_itin)

    # Insert another city into the itinerary
    test_itin.min_distance_insert_city(get_cities_by_name("Canberra")[0])
    print(test_itin)

