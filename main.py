import create_model_from_data
import import_model 
import solveModel
import graph_model

modelData = "X-n247-k50"

Instance = import_model.createInstance(modelData)

model = create_model_from_data.createModel(Instance)

res = solveModel.solveModel(model)
print(res)

generator = graph_model.GraphGenerator(modelData,Instance,model,res)
generator.genAllGraphs()

#27591

print("FINISHED")