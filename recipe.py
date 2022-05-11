# Your code goes here
# ONLY PRESS RUN IF ENTERING "q" STOPS YOUR PROGRAM!!!
# Your code goes here
# ONLY PRESS RUN IF ENTERING "q" STOPS YOUR PROGRAM!!!
def initializeIngredientDict (ingredientList) :
    """Initialize the ingredient dictionary.

    Parameter:  ingredientList - a list of ingredients.
    Return:  a dictionary where the keys are the ingredients in the
      ingredient list, and the associated value is an empty list.
    """
    dict = {}
    for ingredient in ingredientList:
        dict[ingredient] = []
    return dict
def addRecipeToIndex (ingredientDict, recipeName, recipe) :
    """ Adds the recipe to the ingredient dictionary.  The recipe
    is added to the list for each ingredient in the dictionary
    that the recipe contains

    Parameters:
    ingredientDict - the ingredient dictionary
    recipeName - the name of a recipe
    recipe - the text of the recipe
    """
    recipeList = []
    for ingredient in ingredientDict:
        if ingredient in recipe:
            recipeList.append(recipeName)
            ingredientDict[ingredient] = recipeList
    return ingredientDict
def getRecipesWith( ingredient, recipeFinder ):
    """ Look up the recipes with a specific ingredient.

    Parameters:
      ingredient - the ingredient to look up
      recipeFinder - the ingredient dictionary

    Return:  a list of recipe names that use the ingredient.
      Returns an empty list if the ingredient is not known
      or if there are no recipes with that ingredient.
    """
    
    for ing in recipeFinder:
        if ingredient == ing:
            return recipeFinder[ingredient]
        else: 
            return []
def getRecipe( recipeName, recipes ):
    """ Look up a recipe given its name.  This should properly
    support getting the recipe regardless of case (upper or lowercase).

    Parameters:
      recipeName - the name of a recipe
      recipes - the recipe dictionary

    Return: the dictionary or "No recipe found" if it is
      not in the dictionary.
    """
    recipeNameUppercase = recipeName.upper()
    if recipeNameUppercase in recipes:
        return recipes[recipeNameUppercase]
    else:
        return "No recipe found."
def readRecipes( file ):
    """ Reads the recipes from a file and creates the recipe
    dictionary.  Assumes recipes in the file start with the
    RECIPE NAME (IN CAPS) on its own line, with the recipe to follow.

    Parameter:  file - the name of the file to read from
    Return: a dictionary mapping each recipe name to the recipe text """
    text = ""
    name = ""
    dict = {}
    with open(file, "r") as reader:
        for line in reader:
            line = line.strip()
            if line.isupper():
                #line = line.strip()
                #recipeNameList1.append(line)
                # check if i found the start of recipe na,e
                if name!= "":
                    #print(name)
                    dict[name] = text
                    #print(name)
                    name = line
                    #print(name)
                    text = "" 
                else:
                    name = line
                    #print(name)
                    text = "" 
            else: 
                #print(line)
                text = text +line + "\n" + " "
                #print(text)
    # save the last ones
        print(name)
        dict[name] = text
             
        
    return dict
def createRecipeFinder( ingredientsList, recipes ):
    """ Initializes the ingredient dictionary and then puts
    the recipes into the ingredient dictionary and returns it.

    Parameters:
      ingredientsList - the list of ingredients to put in the dictionary
      recipes - the recipe dictionary

    Returns: the completed ingredient dictionary """
    recipeDict = {}
    listRecipe = []
    for ingredient in ingredientsList:
        for name in recipes:
            if ingredient in recipes[name]:
                listRecipe.append(name)
                recipeDict[ingredient] = listRecipe
            else: recipeDict[ingredient] = listRecipe
        listRecipe = []
    return recipeDict
def main () :
    recipeDict = readRecipes("recipe.txt")
    ingredientsList = ["molasses", "boiling water", "caramel", "buttermilk", "vinegar"]
    ingredientDict = createRecipeFinder( ingredientsList, recipeDict)

    userIngredient = input("What ingredient do you want recipes for? (Enter q to quit)")
    if not(userIngredient in ingredientsList): 
        return "No such entry"
    while userIngredient in ingredientsList  or userIngredient!= "q" :
        recipeNameList = getRecipesWith( userIngredient, ingredientDict )
        print (recipeNameList)
        userRecipeName = input("Which recipe do you want to see?")
        recipeText = getRecipe( userRecipeName, recipeDict )
        print (recipeText)
#print(readRecipes("shorterrecipe.txt"))
print(main())
