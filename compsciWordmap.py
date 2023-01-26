import json


def getJsonString(file):
  with open(file,"r") as f:
    jsonString = f.readlines()
    data  = json.loads("".join(jsonString))
    return data

