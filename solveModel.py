from pyvrp.stop import MaxIterations, MaxRuntime

def solveModel(model):
    result = model.solve(stop=MaxIterations(10000),seed=42,display=True)
    return result