import PySimpleGUI as sg
import xml.etree.ElementTree as ET
from xmlParser import *

XML_FOLDER = "compsciXml"
XML_FILE   = f"{XML_FOLDER}/compsci.xml"

def buildWindow(xmlTree,xmlRoot):
  sg.theme('DarkAmber')
  layout = [
    [sg.Table(values = [[xmlRoot.tag]],headings = ["Name"],max_col_width = 50, auto_size_columns = True,justification = 'center',key = "xmlTable",enable_events = True)],
    [sg.Button('Add'),sg.Button('Remove')],
    [sg.Button('Next'),sg.Button('Previous'),sg.Button("Exit")]
  ]
  window = sg.Window('XML GUI',layout,element_justification = "c")
  xmlTable = window["xmlTable"]
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
      break
    if event == "Next" and values['xmlTable']:
      value = values['xmlTable']
      elements = getElements(xmlRoot,"".join(xmlTable.Values[value[0]]))
      if not elements:
        errorHandlerWindow(f"There are no more elements after {''.join(xmlTable.Values[value[0]])}!")
      else:
        xmlTable.update(elements)
  window.close() 

def errorHandlerWindow(message):
  layout = [
    [sg.Text(message,size=(len(message),1),font=16)],
    [sg.Button("Ok")]
  ]
  window = sg.Window("Oopsie!",layout)
  while True:
    event,values = window.read()
    if event == 'Ok' or event == sg.WIN_CLOSED:
      window.close()
      break

def main():
  xmlTree = ET.parse(XML_FILE)
  xmlRoot = xmlTree.getroot()
  #print(getElements(xmlRoot,"Computer_Science"))
  buildWindow(xmlTree,xmlRoot)

if __name__ == "__main__":
  main()