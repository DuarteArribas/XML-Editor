import xml.etree.ElementTree as ET
from xmlParser import *
from welcomeWindow    import *
XML_FOLDER = "compsciXml"
XML_FILE   = f"{XML_FOLDER}/compsci.xml"

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
  print(welcomeWindow())
  #file = filePickerWindow()
  #xmlTree = ET.parse(XML_FILE)
  #xmlRoot = xmlTree.getroot()
  #buildWindow(xmlTree,xmlRoot)

if __name__ == "__main__":
  main()