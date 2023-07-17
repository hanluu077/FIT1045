# TASK 4 - MAP PLOTTING [COMPLETED]
"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It allows plotting an Itinerary as the picture of a map.

@file map_plotting.py
"""
from mpl_toolkits.basemap import Basemap #have to do 'pip install basemap'
import matplotlib.pyplot as plt
from itinerary import Itinerary
from city import City

def plot_itinerary(itinerary: Itinerary, projection = 'robin', line_width=2, colour='b') -> None:
    """
    Plots an itinerary on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.

    :param itinerary: The itinerary to plot.
    :param projection: The map projection to use.
    :param line_width: The width of the line to draw.
    :param colour: The colour of the line to draw.
    """
    #TODO

    # fig = plt.figure(figsize=(8, 4.5))
    # plt.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.00)
    # map = Basemap(projection='robin',lon_0=0,resolution='c')
    # map.fillcontinents(lake_color='white')
    # map.drawcoastlines()
    # plt.savefig('world.png',dpi=75)

    # Get the latitude and longitude coordinates of all the cities in the itinerary
    lats = [city.coordinates[0] for city in itinerary.cities]
    lons = [city.coordinates[1] for city in itinerary.cities]

    # Set the figure size and adjust the subplots
    fig = plt.figure(figsize=(8, 4.5))
    plt.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.00)

    # Set up the Basemap object
    map = Basemap(projection=projection, lon_0=0, resolution='c')
    map.fillcontinents(lake_color='white')
    map.drawcoastlines()

    # Convert the latitude and longitude coordinates to the Basemap projection
    x, y = map(lons, lats)

    # Plot the cities
    map.plot(x, y, 'bo', markersize=8)

    # Plot the itinerary as a line connecting the cities
    map.plot(x, y, color=colour, linewidth=line_width)

    # Save the plot to a file
    filename = 'map_' + '_'.join([city.name for city in itinerary.cities]) + '.png'
    plt.savefig(filename)
    plt.show()
    
    
   
    

if __name__ == "__main__":
    # create some cities
    city_list = list()

    city_list.append(City("Melbourne", (-37.8136, 144.9631), "primary", 4529500, 1036533631))
    city_list.append(City("Sydney", (-33.8688, 151.2093), "primary", 4840600, 1036074917))
    city_list.append(City("Brisbane", (-27.4698, 153.0251), "primary", 2314000, 1036192929))
    city_list.append(City("Perth", (-31.9505, 115.8605), "1992000", 2039200, 1036178956))
    # city_list.append(City("Tokyo", (35.6839, 139.7744), "primary", 39105000, 1392685764))
    # # Tokyo       (35.6839, 139.7744)  primary    39105000    1392685764

    # plot itinerary
    plot_itinerary(Itinerary(city_list))

