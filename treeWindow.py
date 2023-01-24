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