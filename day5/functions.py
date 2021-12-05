# Module for Day 5

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])

def get_dangerous_point_count(field, min_overlap_count):
    """ Gets the count of dangerous points in the given field
        field: 2-d array of counts - each element is the number of vent lines at that point
        min_overlap_count: the minmum number of vent lines that is deemed dangerous
    """
    dangerous_point_count = 0
    for row in field:
        for cell in row:
            if cell >= min_overlap_count:
                dangerous_point_count += 1

    return dangerous_point_count

def is_horizontal(vent_line):
    """ Determines if the given line is horizontal """
    if vent_line[0].x == vent_line[1].x:
        return True

    return False

def is_vertical(vent_line):
    """ Determines if the given line is vertical """
    if vent_line[0].y == vent_line[1].y:
        return True

    return False

def update_field_with_vent_line(field, vent_line):

    # Get co-ordinates of first point
    x = vent_line[0].x
    y = vent_line[0].y

    # Get offset to second point
    x_offset = 0
    if vent_line[1].x > x:
        x_offset = 1
    elif vent_line[1].x < x:
        x_offset = -1

    y_offset = 0
    if vent_line[1].y > y:
        y_offset = 1
    elif vent_line[1].y < y:
        y_offset = -1

    finished = False
    while not finished:
        field[x][y] += 1
        if x == vent_line[1].x and y == vent_line[1].y:
            finished = True
        else:
            x += x_offset
            y += y_offset

    return
