import gurobipy as gp
import pandas as pd
import itertools

##################################
######## GLOBAL PARAMETERS #######
##################################

global M
global T 

M = 1000000
T = 55


##################################
########## LOADING DATA ##########
##################################

# the following data will be loaded into lists, named as follows:
    # - D
    # - P
    # - O 
    # - O_current
    # - Mode
    # - U


# the following data will be loaded into dataframes, named and indexed as follows:
    # - a_demand[product, DC]
    # - a_capacity[product, DC]
    # - a_FTL[product]

    # - c_sea[product, port]
    # - c_truck[product, port, DC, mode, urgency]
    # - c_moving[port]

    # - t_sea[port]
    # - t_congestion[port]
    # - t_land[port, DC, mode, urgency]

def load_data():
    pass



##################################
######## BUILDING MODEL ##########
##################################

# now that our input data is in a workable form, we can create the model with gurobi
model = gp.Model('routing-model')

### DECISION VARIABLES ###

def create_index(iterables:list):
    # we want a list of tuples of every combination in iterables
    # itertools.product can do this for us

    return list(itertools.product(*iterables))

x = model.addVars(create_index([P,O,D,Mode,U]), name="x", vtype=gp.GRB.INTEGER)
y = model.addVars(create_index([P,O,D,Mode,U]), name="y", vtype=gp.GRB.BINARY)
z = model.addVars(create_index([P,O,D,U], name="z", vtype=gp.GRB.INTEGER))
p = model.addVars(create_index([O]), name="p", vtype=gp.GRB.BINARY)



### OBJECTIVE FUNCTION ###
model.setObjective()