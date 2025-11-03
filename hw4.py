##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts and returns
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

from functools import reduce

def count_simba(input_list):
    number_simba = map(lambda s: s.count("Simba"), input_list)
    return reduce(lambda a, b: a + b, number_simba, 0)

sentences = [
    "Simba and Nala are lions.",
    "I laugh in the face of danger.",
    "Hakuna matata",
    "Timon, Pumba and Simba are friends, but Simba could eat the other two."
]

print(count_simba(sentences))

import datetime as dt
import pandas as pd

# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

def get_day_month_year(date_list):
    build_df = map(lambda d: {'day': d.day, 'month': d.month, 'year': d.year}, date_list)
    return pd.DataFrame(build_df)


dates = [
    dt.date(2025, 3, 23),
    dt.date(1978, 11, 21),
    dt.date(2015, 12, 7)
]

print(get_day_month_year(dates))


# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#
from geopy.distance import geodesic

def compute_distance(coordinates):
    return list(map(lambda pair: round(geodesic(pair[0], pair[1]).km,2), coordinates))

test_coord = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
print(compute_distance(test_coord))


#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#

def sum_general_int_list(input_list):
    return reduce(lambda total, element: total + (element if isinstance(element, int) else sum_general_int_list(element)), input_list, 0)

list_1 = [[2], 3, [[1, 2], 5]]
print(sum_general_int_list(list_1))