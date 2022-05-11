import random

################ FUNCTION DEFINITIONS GO HERE ################
def plantRandomSeeds( n ):
    string = ""
    """Given an int n that describes the number of spots,
    randomly plant seeds with a chance of 20%. Return a string of length
    n that has a space for no seed and an o for a seed."""
    for i in range(0,n):
        i = random.randint (1,5)
        if i == 1: string = string + "o"
        else: string = string + " "
    return string
        
a = plantRandomSeeds(9)
print(a)