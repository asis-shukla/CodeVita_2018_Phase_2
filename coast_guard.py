"""This is a program for Obstacle problem
which is asked in TCS CodeVita phase 2 2018
This is written by Ashish Shukla on 9-08-2018"""

str_input = input()
l, m, k = map(int, str_input.split(","))
print(l, m, k)   # for check

boats_points = []    # boats points contain tuples of coordinates
for _ in range(k):   # taking all input points of boats
    str_input = input()
    boats_points.append(tuple(map(int, str_input.split(","))))

print(boats_points)    # for check


def is_uncontrollable(i, j):
    min_distance_from_all_boats = []
    for boat_point_index in range(k):
        min_distance_from_all_boats.append(min_distance(boats_points[boat_point_index], i, j))
    return len(min_distance_from_all_boats) != len(set(min_distance_from_all_boats))


def min_distance(boat_point_tuple, i, j):
    min_distance_from_this_boat = abs(boat_point_tuple[0]-i) + abs(boat_point_tuple[1]-j)
    return min_distance_from_this_boat


number_of_uncontrollable_points = 0
uncontrollable_points_list = []
for i in range(l):
    for j in range(m):
        if is_uncontrollable(i, j):
            number_of_uncontrollable_points += 1
            t = (i, j)
            uncontrollable_points_list.append(t)
        else:
            pass

print(number_of_uncontrollable_points)
print(uncontrollable_points_list)

