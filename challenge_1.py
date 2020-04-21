# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read()) 

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system
def average(data, var_to_average):
    # takes a dataset and a variable name and finds its average across all stations
    total = 0    
    for station in data:
        ## each station is a dictionary
        ## add to sum the value attached to key variable in dict
        total+=station[var_to_average]

    av = total / len(data)
    return ('The average of ' + var_to_average + ' across all stations is ' + str(av))

    # https://docs.python.org/3/tutorial/datastructures.html#dictionaries 

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)
def total_bikes(data, bike_count_variables):
    # takes in set of all the variables that need to be summed to get total number of bikes
    # takes in dataset that holds bike_count_variables
    total_bike_count = 0
    for var in bike_count_variables:
        total_bike_count+=summation(data, var)
        
    return total_bike_count

def summation(data, var_to_sum):
    var_total = 0
    for station in data:
        var_total+=station[var_to_sum]
    return var_total

def ratio(data, var_rented, bike_count_variables):
    # takes in dataset and variable that counts num rented bikes
    ratio_rented = summation(data, var_rented) / total_bikes(data, bike_count_variables)
    return ratio_rented

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%
def add_variable(data):
    for station in data:
        total = station['num_bikes_disabled'] + station['num_docks_available'] + station['num_bikes_available']
        station['percent_bikes_remaining'] = round((station['num_bikes_available'] / total)*100, 2)
    
    # https://www.programiz.com/python-programming/methods/built-in/round
    return 

def main():
    # problem 1
    print(average(divvy_stations, 'num_docks_available'))
    print(average(divvy_stations, 'num_bikes_available'))
    
    # problem 2
    bike_count_variables = ['num_bikes_disabled', 'num_docks_available', 'num_bikes_available']
    print("The ratio of bikes currently rented to total bikes in the system is " + str(ratio(divvy_stations, 'num_docks_available', bike_count_variables)))
    
    # problem 3
    print(add_variable(divvy_stations))
    




