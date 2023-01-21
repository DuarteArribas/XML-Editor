import xml.etree.ElementTree as ET
import xml.etree

def isXml(xmlString):
  try:
    ET.fromstring(xmlString)
  except ET.ParseError:
    return False
  return True

def getElements(root,name):
  if root.tag == name:
    return [elements.tag for elements in root]
  for element in root:
    if element.tag == name:
      return [subelements.tag for subelements in element]
  for element in root:
    el = getElements(element,name)
    if el:
      return el

def insertElement(tree,fileName,root,name,newElementName):
  for element in root:
    if element.tag == name:
      tmpEl = xml.etree.ElementTree.Element(newElementName)
      tmpEl.text = " "
      element.insert(1,tmpEl)
      tree.write(fileName)
      return True
  for element in root:
    el = insertElement(tree,fileName,element,name,newElementName)
    if el:
      return el

def removeElement(tree,fileName,root,name):
  for element in root:
    if element.tag == name:
      element.clear()
      root.remove(element)
      tree.write(fileName)
      return True
  for element in root:
    el = removeElement(tree,fileName,element,name)
    if el:
      return el