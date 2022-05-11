import random
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



def growGarden (plantedSeeds, numberOfLevels):
    """ Given an initial string of planted seeds, generate numberOfLevels growth.
    Return a string with each level of growth on a new line. The "bottom" line
    should be the initial plantedSeeds, with each subsequent level "above" as in
    the sketch."""
    level1 = growNextLevel(plantedSeeds)
    
    garden = level1 + "\n" + plantedSeeds
    
    if numberOfLevels == 1: return level1 + "\n" + plantedSeeds
    else: 
        levels = level1
        for i in range(2,numberOfLevels):
            levels = growNextLevel(levels)
            return levels + "\n" +  garden
print (growGarden("ooxox",3))
     

