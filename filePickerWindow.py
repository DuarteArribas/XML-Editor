import PySimpleGUI as sg
from rootPickerWindow import *
from newXmlFileWindow import *
from errorWindow      import *
from xmlParser        import *

def filePickerWindow():
  layout = [
    [[sg.Text("Choose an XML file: "),sg.Input(key = "xmlFile",font=16),sg.FileBrowse()]],
    [[sg.Button("Open"),sg.Button("Exit")]]
  ]
  window = sg.Window("XML file chooser",layout,element_justification = "c")
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
      break
    if event == "Open":
      xmlFileInput = values["xmlFile"]
      if not xmlFileInput:
        continue
      if _checkXmlFile(xmlFileInput):
        return xmlFileInput
      else:
        errorWindow("XML validation error",f"{xmlFileInput} is not a valid xml file!")
  window.close()

def _checkXmlFile(file):
  if file.split(".")[-1] != "xml":
    return False
  try:
    with open(file,"r") as xmlFile:
      xmlString = "".join(xmlFile.readlines())
      return isXml(xmlString)
  except FileNotFoundError:
    createNewXMLFile(file,rootPickerWindow())
    return True