import xml.etree.ElementTree as ET
from xmlParser import *
from gui import *

XML_FOLDER = "compsciXml"
XML_FILE   = f"{XML_FOLDER}/compsci.xml"

def buildWindow(xmlTree,xmlRoot):
  sg.theme('DarkAmber')
  layout = [
    [sg.Table(values = [[xmlRoot.tag]],headings = ["Name"],max_col_width = 50, auto_size_columns = True,justification = 'center',key = "xmlTable",enable_events = True)],
    [sg.Button('Add'),sg.Button('Remove')],
    [sg.Button('Next'),sg.Button('Previous'),sg.Button("Exit")]
  ]
  window   = sg.Window('XML GUI',layout,element_justification = "c")
  xmlTable = window["xmlTable"]
  while True:
    event,values = window.read()
    value = values['xmlTable'] if values['xmlTable'] else ""
    if event == sg.WIN_CLOSED or event == 'Exit':
      break
    if event == "Add" and values['xmlTable']:
      newElement = addHandlerWindow()
      if newElement:
        insertElement(xmlTree,XML_FILE,xmlRoot,"".join(xmlTable.Values[value[0]]),newElement)
        xmlTree = ET.parse(XML_FILE)
        xmlRoot = xmlTree.getroot()
    if event == "Remove" and values['xmlTable']:
      if confirmWindow():
        removeElement(xmlTree,XML_FILE,xmlRoot,"".join(xmlTable.Values[value[0]]))
    if event == "Next" and values['xmlTable']:
      elements = getElements(xmlRoot,"".join(xmlTable.Values[value[0]]))
      if not elements:
        errorHandlerWindow(f"There are no more elements after {''.join(xmlTable.Values[value[0]])}!")
      else:
        xmlTable.update(elements)
  window.close()



def confirmWindow():
  layout = [
    [sg.Text("Do you want to remove?")],
    [sg.Button("Yes")],
    [sg.Button("No")]
  ]
  window = sg.Window("Confirmation",layout)
  while True:
    event,values = window.read()
    if event == "Yes":
      window.close()
      return True
    if event == "No" or event == sg.WIN_CLOSED:
      window.close()
      return False

def addHandlerWindow():
  layout = [
    [sg.Text("New Element Name:",font=16),sg.InputText(key = "addInput",font=16)],
    [sg.Button("Ok"),sg.Button("Cancel")]
  ]
  window  = sg.Window("Add New element!",layout)
  while True:
    event,values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
      window.close()
      return None
    if event == "Ok":
      if not values['addInput'].strip():
        errorHandlerWindow("Please input a valid name. Empty names are not allowed!")
      else:
        window.close()
        return values['addInput']
        



    


def main():
  sg.theme('DarkAmber')
  file = getFilenameWindow()
  #xmlTree = ET.parse(XML_FILE)
  #xmlRoot = xmlTree.getroot()
  #buildWindow(xmlTree,xmlRoot)

if __name__ == "__main__":
  main()