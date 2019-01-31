import random

def PAL(distance, battle):
    """
    Returns PAL depending on activity level of dragon.

    Distance: distance the dragon flew in a day.
    Battle: bool, 1 for war time, 0 for peace time.
    """
    PAL = (distance/235.29) + 0.3*battle
    return PAL

def BMR(weight, k):
    """
    Returns BMR of the dragon.

    Weight: weight of the dragon.
    k: from 2/3 to 3/4.
    """
    bmr = weight/68
    bmr = bmr ** k
    bmr *= 1624 
    return bmr

def E_out(weight, k, distance, battle):
    """
    Calculates E_out.

    Weight: weight of the dragon.
    k: from 2/3 to 3/4.
    Distance: distance the dragon flew in a day.
    Battle: bool, 1 for war time, 0 for peace time.
    """
    return BMR(weight, k)*PAL(distance, battle)

def E_in(weight, calories, current_season_index, fed):
    """
    Returns E_in.

    Calories: calories the dragon intakes.
    """
    dwdt = 1/((0.798/weight)+(2.08/(88000-weight))-(3.53*0.0001)+(5.12*0.00000001*weight))
    output = 4250*dwdt*(1/365) + 1624*1.7*((weight/68)**0.708)
    next_current_season, next_season_index = climate_randomizer(current_season_index)
    return output

def growth(calories, weight, k, distance, battle, c, climate, fed): #maybe also health
    """
    Returns the growth multiplication factor of a dragon.

    Calories: calories the dragon intakes.
    Weight: weight of the dragon.
    k: from 2/3 to 3/4.
    Distance: distance the dragon flew in a day.
    Battle: bool, 1 for war time, 0 for peace time.
    c: conversion factor.
    climate: the current season. Takes the value of season_index.
    fed: is the dragon fed by humans. (bool, 1 fof fed, 0 for not fed.)
    """
    E_diff = E_in(calories, climate, fed) - E_out(weight, k, distance, battle)
    return (E_diff * c)


#calculates the current season


SEASONS = ['summer','fall','winter','spring']

def climate_randomizer(season_index):
    """
    Gives climate a .3 chance to change to the next season. Returns the season, and season_index.
    """
    current_season = SEASONS[season_index]
    random_var = random.randint(0,10)
    if season_index%4 == 0 or season_index%4 == 2:
        if random_var < 3:
            season_index += 1
            current_season = SEASONS[season_index%4]
    else:
        season_index += 1
        current_season = SEASONS[season_index%4]
    return current_season, season_index
