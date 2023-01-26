import xml.etree.ElementTree as ET
import xml.etree
from lxml import etree

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

def getParentElement(root,name,parentElement):
  if root.tag == name:
    return None
  for element in root:
    if element.tag == name:
      return parentElement
  for element in root:
    el = getParentElements(element,name,element.tag)
    if el:
      return el
      
def getParentElements(root,name,parentElements):
  if root.tag == name:
    return None
  for element in root:
    if element.tag == name:
      return parentElements  
  for element in root:
    el = getParentElements(element,name,[e.tag for e in root])
    if el:
      return el

def insertElement(tree,filename,root,name,newElementName,newElementAttributes):
  if root.tag == name:
    tmpEl = xml.etree.ElementTree.Element(newElementName)
    if newElementAttributes:
      tmpEl.attrib = newElementAttributes
    tmpEl.text = " "
    root.insert(1,tmpEl)
    tree.write(filename)
    return True
  for element in root:
    if element.tag == name:
      tmpEl = xml.etree.ElementTree.Element(newElementName)
      if newElementAttributes:
        tmpEl.attrib = newElementAttributes
      tmpEl.text = " "
      element.insert(1,tmpEl)
      tree.write(filename)
      return True
  for element in root:
    el = insertElement(tree,filename,element,name,newElementName,newElementAttributes)
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

def getXMLFilePaths(file):
  root = None
  with open(file,"r") as f:
    root = etree.fromstring("".join(f.readlines()))
  tree = etree.ElementTree(root)
  filePaths = []
  for e in root.iter():
    filePaths.append([tree.getpath(e),list(e.attrib.keys())[0],e.attrib[list(e.attrib.keys())[0]]])
  return filePaths