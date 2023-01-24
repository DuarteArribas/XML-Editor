import PySimpleGUI as sg
import textwrap
import sys
import os
from confirmationWindow import *
from addElementWindow   import *
from errorWindow        import *
from xmlParser          import *

def treeWindow(xmlTree,xmlRoot,xmlParent,xmlFile):
  layout = [
    [sg.Table(values = [[xmlRoot.tag.replace("__"," ")]],headings = ["Name"],max_col_width = 150,auto_size_columns = True,justification = 'center',key = "xmlTable",enable_events = True)],
    [sg.Button('Add'),sg.Button('Remove')],
    [sg.Button('Next'),sg.Button('Previous'),sg.Button("Exit")]
  ]
  window   = sg.Window('XML Tree',layout,element_justification = "c")
  xmlTable = window["xmlTable"]
  while True:
    #print(xmlParent)
    event,values = window.read()
    value = values['xmlTable'] if values['xmlTable'] else ""
    if event == sg.WIN_CLOSED or event == 'Exit':
      sys.exit(0)
    if event == "Add" and values['xmlTable']:
      newElement,newElementDesc = addHandlerWindow()
      if newElement:
        if newElement in getAllElements(xmlRoot):
          errorWindow("Element Error",f"{newElement.replace('__',' ')} already exists!")
          continue
        insertElement(xmlTree,xmlFile,xmlRoot,"".join(xmlTable.Values[value[0]]),newElement,newElementDesc)
        xmlTree = ET.parse(xmlFile)
        xmlRoot = xmlTree.getroot()
    if event == "Remove" and values['xmlTable']:
      xmlElToRemove = "".join(xmlTable.Values[value[0]])
      if confirmWindow(xmlElToRemove):
        removeElement(xmlTree,xmlFile,xmlRoot,xmlElToRemove.replace(" ","__"))
        if os.stat(xmlFile).st_size == 0:
          break
        xmlTable.update(getElements(xmlRoot,xmlParent))
    if event == "Next" and values['xmlTable']:
      elements = getElements(xmlRoot,"".join(xmlTable.Values[value[0]]))
      if not elements:
        errorWindow("Element Error",f"There are no more elements after {''.join(xmlTable.Values[value[0]])}!")
      else:
        elementsWithSpaces = [
          textwrap.wrap(elementWithoutSpaces.replace("__"," "),len(elementWithoutSpaces.replace("__"," "))) for elementWithoutSpaces in elements
        ]
        xmlParent = ''.join(xmlTable.Values[value[0]])
        xmlTable.update(elementsWithSpaces)
  window.close()