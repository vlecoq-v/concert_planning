from typing import Union


class IllegalArgumentError(ValueError):
    pass


def find_sum(target_sum: int, elems: list[int]) -> Union[list[int], None]:
    """Finds a list of 3 integers within @arg list that have a sun of @arg target_sum.
    """

    elems_size = len(elems)
    if elems_size < 3:
        raise IllegalArgumentError

    print(f"size = {elems_size}")

    first = 0
    while first < elems_size - 2:
        print(f"first = {first}")
        second = first + 1
        while second < elems_size - 1:
            print(f"second = {second}")
            third = second + 1
            while third < elems_size:
                print(f"third = {third}, {elems[third]}")
                if elems[third] == target_sum - (elems[first] + elems[second]):
                    return [first, second, third]
                print(target_sum - (elems[first] + elems[second]))
                third += 1
            second += 1
        first += 1
        print(first < elems_size - 3)
    print(f"finished {[first, second, third]}")

    return
