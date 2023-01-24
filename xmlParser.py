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

def getAllElements(root):
  return [elem.tag for elem in root.iter()]

def insertElement(tree,filename,root,name,newElementName,newElementDesc):
  if root.tag == name:
    tmpEl = xml.etree.ElementTree.Element(newElementName)
    if newElementDesc:
      tmpEl.attrib = {"Description":newElementDesc}
    tmpEl.text = " "
    root.insert(1,tmpEl)
    tree.write(filename)
    return True
  for element in root:
    if element.tag == name:
      tmpEl = xml.etree.ElementTree.Element(newElementName)
      if newElementDesc:
        tmpEl.attrib = {"Description":newElementDesc}
      tmpEl.text = " "
      element.insert(1,tmpEl)
      tree.write(filename)
      return True
  for element in root:
    el = insertElement(tree,filename,element,name,newElementName,newElementDesc)
    if el:
      return el

def removeElement(tree,filename,root,name):
  if root.tag == name:
    with open(filename,"w") as f:
      f.write("")
    return True
  for element in root:
    if element.tag == name:
      element.clear()
      root.remove(element)
      tree.write(filename)
      return True
  for element in root:
    el = removeElement(tree,filename,element,name)
    if el:
      return el