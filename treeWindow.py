import PySimpleGUI as sg
import textwrap
import random
import sys
import os
from pickFolderOfPathWindow import *
from confirmationWindow     import *
from addElementWindow       import *
from errorWindow            import *
from xmlParser              import *

def treeWindow(xmlTree,xmlRoot,xmlParent,xmlFile):
  layout = [
    [sg.Table(values = [[xmlRoot.tag.replace("__"," ")]],headings = ["Name"],max_col_width = 150,auto_size_columns = True,justification = 'center',key = "xmlTable",enable_events = True)],
    [sg.Button('Add'),sg.Button('Remove')],
    [sg.Button("Generate File Path"),sg.Button("Show Tree")],
    [sg.Button('Next'),sg.Button('Previous'),sg.Button('Top'),sg.Button('Random'),sg.Button("Exit")]
  ]
  window   = sg.Window('XML Tree',layout,element_justification = "c")
  xmlTable = window["xmlTable"]
  while True:
    event,values = window.read()
    value = values['xmlTable'] if values['xmlTable'] else ""
    if event == sg.WIN_CLOSED or event == 'Exit':
      sys.exit(0)
    if event == "Add" and values['xmlTable']:
      newElement,newElementAttributes = addHandlerWindow()
      if newElement:
        if newElement in getAllElements(xmlRoot):
          errorWindow("Element Error",f"{newElement.replace('__',' ')} already exists!")
          continue
        insertElement(xmlTree,xmlFile,xmlRoot,"".join(xmlTable.Values[value[0]]),newElement,newElementAttributes)
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
        xmlParent = ''.join(xmlTable.Values[value[0]])
        xmlTable.update(_getElementsWithSpaces(elements))
    if event == "Previous" and values['xmlTable']:
      elements = getParentElements(xmlRoot,"".join(xmlTable.Values[value[0]]),[xmlRoot.tag])
      if not elements:
        break
      else:
        xmlTable.update(_getElementsWithSpaces(elements))
    if event == "Top":
      xmlTable.update([xmlRoot.tag])
    if event == "Random":
      allElements   = getAllElements(xmlRoot)
      randomEl      = random.choice(allElements)
      parentElement = getParentElement(xmlRoot,randomEl,xmlRoot.tag)
      if not parentElement:
        xmlTable.update([xmlRoot.tag])
      else:
        xmlTable.update(_getElementsWithSpaces(getElements(xmlRoot,parentElement)))
    if event == "Generate File Path":
      initialFolder = pickFolderOfPathWindow()
      if not initialFolder:
        continue
      xmlFilePaths = getXMLFilePaths(xmlFile)
      _generateFilePaths(initialFolder,xmlFilePaths)
  window.close()

def _getElementsWithSpaces(elementsWithoutSpaces):
  return [
    textwrap.wrap(elementWithoutSpaces.replace("__"," "),len(elementWithoutSpaces.replace("__"," "))) for elementWithoutSpaces in elementsWithoutSpaces
  ]

def _generateFilePaths(initialFolder,xmlFilePaths):
  for path in xmlFilePaths:
    newPath = initialFolder + path
    if not os.path.exists(newPath):
      os.makedirs(newPath)