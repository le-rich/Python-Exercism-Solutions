"""Module docstring here xD"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(time_in_oven):
    """Returns the bake time remaining"""
    return abs(EXPECTED_BAKE_TIME - time_in_oven)

def preparation_time_in_minutes(layers):
    """Returns the preparation time in minutes"""
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Returns the elapsed time in minutes given a number of layers and how much time has passed already"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
