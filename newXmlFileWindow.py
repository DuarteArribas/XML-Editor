def newXMLFile():
  layout = [
    [[sg.Text("What is the root element of the new xml file?"),sg.Input(key = "rootEl",font=16)]],
    [[sg.Button("Go"),sg.Button("Cancel")]]
  ]
  window   = sg.Window("XML root chooser",layout,element_justification = "c")
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
      break
    if event == "Go":
      if not values["rootEl"]:
        continue
      return values["rootEl"]
  window.close()

def createNewXMLFile(filename,root):
  with open(filename,"w") as newXmlFile:
    newXmlFile.write(f"<{root}>\n</{root}>")