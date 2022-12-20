import json
import pydot

def getJsonString(file):
  with open(file,"r") as f:
    jsonString = f.readlines()
    data  = json.loads("".join(jsonString))
    return data

def writeMindMap(data,g):
  if 'fieldName' not in data:
    return pydot.Node('Unknown', label='Unknown')
  if 'subfield' not in data or not data['subfield']:
    return pydot.Node(data['fieldName'], label=data['fieldName'])
  else:
    root = pydot.Node(data['fieldName'], label=data['fieldName'])
    g.add_node(root)
    for subfield in data["subfield"]:
      subfieldNode = writeMindMap(subfield,g)
      g.add_node(subfieldNode)
      edge = pydot.Edge(root, subfieldNode)
      g.add_edge(edge)
    return root

graph = pydot.Dot(graph_type='graph')
writeMindMap(getJsonString("compsciAreas.json"),graph)
graph.write_png('compsciMindMap.png')