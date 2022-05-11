import random
print( "\nGARDEN 3")
random.seed( 1837 )
# write code that "plants" random seeds using 25 spots by invoking your plantRandomSeeds function
# write code that generates 14 levels from those random seeds
# There should be 15 rows in total, one row for the seeds and 14 for the 14 levels of growth
# above them.


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
def growNextLevel( currentLevel ):
    """ Given a string of the currentLevel of growth, generate the next level of
    growth.  Return a string with the same length that has a space for no leaf
    and an o for a leaf.  A leaf grows in the next level if exactly one neighbor
    in the current level has a leaf. If the parameter contains an empty string, then
    return an empty string"""
    print (currentLevel)
    if currentLevel == "": return ""
    #else: 
   
    upperLevel = currentLevel[1]
        
    for i in range(1,len(currentLevel)-1):
        if (currentLevel[i-1] == "o") ^ (currentLevel[i+1] == "o"): 
            upperLevel += "o"
        else: 
            upperLevel += " "
    upperLevel = upperLevel + currentLevel[len(currentLevel)-2] 
    return upperLevel



def growGarden( plantedSeeds, numberOfLevels ):
    """ Given an initial string of planted seeds, generate numberOfLevels growth.
    Return a string with each level of growth on a new line. The "bottom" line
    should be the initial plantedSeeds, with each subsequent level "above" as in
    the sketch."""
    level1 = growNextLevel(plantedSeeds)
    
    garden = level1 + "\n" + plantedSeeds
    
    if numberOfLevels == 1: return level1 + "\n" + plantedSeeds
    else: 
        levels = level1
        for i in range(1,numberOfLevels):
            levels = growNextLevel(levels)
            garden = levels + "\n" + garden
        return garden

spot = plantRandomSeeds(25)

randomGarden = growGarden(spot,14)
print (randomGarden)
