import PySimpleGUI as sg
import sys
from rootPickerWindow import *
from errorWindow      import *
from xmlParser        import *
from newXmlFileWindow import *

def filePickerWindow():
  layout = [
    [[sg.Text("Choose an XML file: "),sg.Input(key = "xmlFile",font=16),sg.FileBrowse()]],
    [[sg.Button("Open")]],
    [[sg.Button("Go Back"),sg.Button("Exit")]]
  ]
  window = sg.Window("XML file chooser",layout,element_justification = "c")
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
      sys.exit(0)
    if event == "Open":
      xmlFileInput = values["xmlFile"]
      if not xmlFileInput:
        continue
      if _checkXmlFile(xmlFileInput):
        window.close()
        return xmlFileInput
      else:
        errorWindow("XML validation error",f"{xmlFileInput.split('/')[-1]} is not a valid xml file!")
    if event == "Go Back":
      window.close()
      return None

def _checkXmlFile(file):
  if file.split(".")[-1] != "xml":
    return False
  try:
    if os.stat(file).st_size == 0:
      raise FileNotFoundError
    with open(file,"r") as xmlFile:
      xmlString = "".join(xmlFile.readlines())
      return isXml(xmlString)
  except FileNotFoundError:
    createNewXMLFile(file,rootPickerWindow())
    return True