import json
import random

def initializeDorms( jsonFile ):
    """ Given the path/name for a file that has dorm names -> dorm capacities,
    create a Dorm instance for each dorm and store it in a dictionary that maps
    the dorm name -> Dorm instance. Return this dictionary. """

    # use a JSON file
    with open( jsonFile, "r" ) as read_file:
        # parse the file into a dictionary
        # this is a dictionary that maps dorm name -> capacity
        dormCapacities = json.load( read_file)

    # create an empty dictionary that will hold the dorms
    # this will map dorm name -> Dorm instance
    dorms = {}

    # for each dorm read from the JSON file
    for dormName in dormCapacities:
        # create a new dorm and store it in the dictionary
        dorms[dormName] = dormCapacities[dormName]# YOUR CODE HERE
    print (dorms)
initializeDorms( "MHCDormCapacities.json" )