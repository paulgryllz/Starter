import doctest


def average(L):
    """(list of str) -> float
    Given a list of strings of numeric values, return the
    average of the values as a float.
    >>> average(['1', '5', '10', '12'])
    7.0
    >>> average(['10', '12'])
    11.0
    """
    return sum(map(float, L)) / len(L)


def average_grade(L):
    """(list of list) -> list
    L is a list of lists. The first item in each
    sublist is a student name and the rest of the items in the
    sublist are grade values (float or int). Return a
    new list of lists where each sublist has length 2 of
    the form [student_name (str), average grade (float)]
    >>> average_grade([['Bob', 56, 80, 72, 90],\
    ['Alice', 60, 88, 44, 70], ['Joe', 44, 100, 80, 60, 50]])
    [['Bob', 74.5], ['Alice', 65.5], ['Joe', 66.8]]
    """
    ret = []
    for l in L:
        ret.append([l[0], average(l[1:])])
    return ret


def string_list(L):
    """(list of str) -> list of list
    Given a list of strings where each string has the format:
    'name, grade, grade, grade, ...' return a new list of
    lists where each inner list has the format :
    [name (str), grade, grade, grade, ...] where the name
    is a string and the grades are floats.

    >>> string_list(['Anna, 50, 90, 80',\
    'Bill, 60, 70', 'Cal, 98.5, 100, 95.5, 98'])
    [['Anna', 50.0, 90.0, 80.0], ['Bill', 60.0, 70.0],\
 ['Cal', 98.5, 100.0, 95.5, 98.0]]
    """
    ret = []
    for l in L:
        hold = l.split(', ')
        for y in range(1, len(hold)):
            hold[y] = float(hold[y])
        ret.append(hold)
    return ret


def string_avg(L):
    """(list of str) -> list of list
    Given a list of strings where each string has the format:
    'name, grade, grade, grade, ...' return a new list of
    lists where each inner list has the format :
    [name (str), average grade (float)]
    Requirement: This function should be 1 line long.

    >>> string_avg(['Anna, 50, 92, 80', 'Bill, 60, 70','Cal, 98.5,\
    100, 95.5, 98'])
    [['Anna', 74.0], ['Bill', 65.0], ['Cal', 98.0]]
    """
    ret = []
    for l in L:
        temp = l.split(', ')
        ret.append([temp[0], average(temp[1:])])
    return ret


def string_avg_update(L):
    """(list of str) -> NoneType
    Given a list of strings where each string has the format:
    'name, grade, grade, grade, ...' update  the given
    list of strs to be a list of floats where each item
    is the average of the corresponding numbers in the
    string. Note this function does NOT RETURN the list.
    >>> L = ['Anna, 50, 92, 80', 'Bill, 60, 70', 'Cal, 98.5, 100, 95.5, 98']
    >>> string_avg_update(L)
    >>> L
    [74.0, 65.0, 98.0]
    """
    for l in range(len(L)):
        temp = L[l].split(', ')
        L[l] = average(temp[1:])


if __name__ == '__main__':
    doctest.testmod(verbose=True)
