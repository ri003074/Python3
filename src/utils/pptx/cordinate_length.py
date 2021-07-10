import math
from icecream import ic

a1 = (1, 2)
a2 = (5, 3)
a3 = (10, 10)

reference_arr = []
reference_arr.append(a1)
reference_arr.append(a2)
reference_arr.append(a3)


b1 = (6, 2)
b2 = (2, 3)
b3 = (12, 10)

target_arr = []
target_arr.append(b1)
target_arr.append(b2)
target_arr.append(b3)

ic(math.sqrt((a2[0] - a1[0]) ** 2 + (a2[1] - a1[1]) ** 2))


for target_data in target_arr:
    distance_list = []
    for reference_data in reference_arr:
        distance = math.sqrt(
            (reference_data[0] - target_data[0]) ** 2
            + (reference_data[1] - target_data[1]) ** 2
        )
        ic(distance)
        distance_list.append(distance)

    min_value = min(distance_list)
    min_index = distance_list.index(min_value)
    ic(min_value)
    ic(min_index)
