import PySimpleGUI as sg
from tagValidation import *
from errorWindow   import *

def addHandlerWindow():
  layout = [
    [sg.Text("New Element Name:",font=16),sg.InputText(key = "addInput",font=16)],
    [sg.Text("Attribute:",font=16),sg.InputText(key = "attrib",font=16),sg.Text("Value:",font=16),sg.InputText(key = "value",font=16),sg.Button("Add")],
    [sg.Text("Attributes to add:",font=16),sg.Listbox(values = [],key = "attributeList",font = 11),sg.Button("Remove")],
    [sg.Button("Ok"),sg.Button("Cancel")]
  ]
  window  = sg.Window("Add New element",layout)
  attributeList = window["attributeList"]
  attributes = {}
  while True:
    event,values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
      window.close()
      return None,None
    if event == "Ok":
      if not values["addInput"].strip():
        errorWindow("Input Error","Please input a valid name. Empty names are not allowed!")
      else:
        if not validateTag(values["addInput"]):
          errorWindow("Tag Error",f"{values['addInput']} contains invalid characters for xml tags! Check naming rules at https://www.w3schools.com/xml/xml_elements.asp#midcontentadcontainer")
          continue
        window.close()
        return values["addInput"].replace(" ","__"),attributes
    if event == "Add" and values["attrib"] and values["value"]:
      attributes[values["attrib"]] = values["value"]
      attributeList.update(_getListOfAttributes(attributes))
    if event == "Remove" and values["attributeList"]:
      key = "".join(values["attributeList"]).split(": ")[1].split("=")[0]
      del attributes[key]
      attributeList.update(_getListOfAttributes(attributes))


def _getListOfAttributes(attributesDictionary):
  attributesList = []
  for attribute,value in attributesDictionary.items():
    attributesList.append(f"Attribute {len(attributesList) + 1}: {attribute}=\"{value}\"")
  return attributesList