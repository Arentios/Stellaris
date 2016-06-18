import json
import logging
import constants

logging.basicConfig(filename=constants.LOG_FILE, level=logging.INFO)

class TechTree:
    def _init__(self, tree = "", techs = []):
        self.tree = tree
        self.techs = techs

class Technology:
    def __init__(self, name = "",  type = "", cost = 0, discovery = "None", children = []):
        self.name = name
        self.type = type
        self.cost = cost
        self.discovery = discovery
        self.children = children
    
   
##Need to recursively load a tech tree since it's an object containing a list of objects which themselves can contain a list of objects
def tech_tree_decoder(obj):
    pass


def load_tech_trees():
    with open(constants.PHYSICS_FILE, 'r') as physicsFile:
        physicsTree = json.load(physicsFile)
        



