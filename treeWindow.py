import PySimpleGUI as sg
import textwrap
from addElementWindow import *
from errorWindow      import *
from xmlParser        import *

def treeWindow(xmlTree,xmlRoot,xmlFile):
  layout = [
    [sg.Table(values = [[xmlRoot.tag.replace("__"," ")]],headings = ["Name"],max_col_width = 150,auto_size_columns = True,justification = 'center',key = "xmlTable",enable_events = True)],
    [sg.Button('Add'),sg.Button('Remove')],
    [sg.Button('Next'),sg.Button('Previous'),sg.Button("Exit")]
  ]
  window   = sg.Window('XML Tree',layout,element_justification = "c")
  xmlTable = window["xmlTable"]
  while True:
    event,values = window.read()
    value = values['xmlTable'] if values['xmlTable'] else ""
    if event == sg.WIN_CLOSED or event == 'Exit':
      break
    if event == "Add" and values['xmlTable']:
      newElement,newElementDesc = addHandlerWindow()
      if newElement:
        insertElement(xmlTree,xmlFile,xmlRoot,"".join(xmlTable.Values[value[0]]),newElement,newElementDesc)
        xmlTree = ET.parse(xmlFile)
        xmlRoot = xmlTree.getroot()
    #if event == "Remove" and values['xmlTable']:
    #  if confirmWindow():
    #    removeElement(xmlTree,XML_FILE,xmlRoot,"".join(xmlTable.Values[value[0]]))
    if event == "Next" and values['xmlTable']:
      elements = getElements(xmlRoot,"".join(xmlTable.Values[value[0]]))
      if not elements:
        errorWindow("Element Error",f"There are no more elements after {''.join(xmlTable.Values[value[0]])}!")
      else:
        elementsWithSpaces = [
          textwrap.wrap(elementWithoutSpaces.replace("__"," "),len(elementWithoutSpaces.replace("__"," "))) for elementWithoutSpaces in elements
        ]
        xmlTable.update(elementsWithSpaces)
  window.close()