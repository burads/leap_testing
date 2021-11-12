from dimod import Binary, CQM, quicksum 
from dwave.system import LeapHybridCQMSampler 
import itertools 
import dwave.inspector

cost = [10, 24, 28, 26, 21]
profit = [30, 20, 25, 40, 32]
people = [1, 3, 4, 2, 2]
P = 5
B = 50
n = len(profit)

# Create the binary variables
x = [Binary(i) for i in range(n)]

# Construct the CQM
cqm = CQM()

# Add the objective
cqm.set_objective(quicksum(-profit[i]*x[i] for i in range(n)))

# Add the two constraints
cqm.add_constraint(quicksum(people[i]*x[i] for i in range(n)) <= P, label='max people') 
cqm.add_constraint(quicksum(cost[i]*x[i] for i in range(n)) <= B, label='max budget') 

# Submit to the CQM sampler
sampler = LeapHybridCQMSampler()
sampleset = sampler.sample_cqm(cqm) 
print(sampleset)
dwave.inspector.show(sampleset)
