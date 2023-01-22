import PySimpleGUI as sg
import os
from rootPickerWindow import *
from errorWindow      import *

def newXMLFileWindow():
  layout = [
    [[sg.Text("File name: "),sg.Input(key = "newFileName",font = 16,default_text = "myFile.xml")]],
    [[sg.Text("Choose a location: "),sg.Input(key = "xmlLocation",font=16),sg.FolderBrowse()]],
    [[sg.Button("Go"),sg.Button("Exit")]]
  ]
  window = sg.Window("New File",layout,element_justification = "c")
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
      break
    if event == "Go":
      if not values["newFileName"] or not values["xmlLocation"]:
        continue
      xmlName = values["newFileName"]
      xmlDir  = values["xmlLocation"]
      newRoot = rootPickerWindow()
      newFilePath = generateNewFilePath(xmlDir,xmlName)
      createNewXMLFile(newFilePath,newRoot)
      window.close()
      return newFilePath
    window.close()
  

def createNewXMLFile(filename,root):
  with open(filename,"w") as newXmlFile:
    newXmlFile.write(f"<{root}>\n</{root}>")

def generateNewFilePath(xmlDir,xmlName):
  if xmlName.split(".")[-1] == "xml":
    xmlName = xmlName.split(".")[-2]
  newFilePathTemp = xmlDir + "/" + xmlName
  count = 2
  while os.path.exists(newFilePathTemp + ".xml"):
    if count == 2:
      newFilePathTemp = newFilePathTemp + f" ({count})"
    else:
      newFilePathTemp = newFilePathTemp.split(" ")[0] + f" ({count})"  
    count += 1
  return newFilePathTemp + ".xml"