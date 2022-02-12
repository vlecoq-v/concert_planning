from typing import Union


class IllegalArgumentError(ValueError):
    pass


def find_sum(target_sum: int, int_list: list[int]) -> Union[list[int], None]:
    """Finds a list of 3 integers within @arg list that have a sun of @arg target_sum.
    """

    int_list_size = len(int_list)
    if int_list_size < 3:
        raise IllegalArgumentError

    int_list.sort()

    # compare first element with two others (first + 1 and last element)
    # as list is sorted our second and third element will converge to a pertinent value or reach each other
    # if so no sum was found and the second element becomes the basis of our triplet
    for first in range(0, int_list_size - 2):
        second = first + 1
        third = int_list_size - 1

        while (second < third):
            current_sum = int_list[first] + int_list[second] + int_list[third]
            if current_sum == target_sum:
                return [first, second, third]
            elif current_sum < target_sum:
                second += 1
            else:
                third -= 1

    return
