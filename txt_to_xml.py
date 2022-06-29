from pathlib import Path
import xml.etree.cElementTree as ET
from PIL import Image
import os

# this file generates xml files for the tensorflow object detection api out of txt files

"""PARAMETER"""
TXT_DIR = "../../generated/txt/"       # controls where the programm searches for the txt files
IMG_DIR = "../../generated/"           # controls where the programm makes the xml directory for the xml files
    IMG_WIDTH = 640 # the width of the used pictures
    IMG_HEIGHT = 640 # the heigth of the used pictures
"""PARAMETER"""

cwd = os.getcwd()
os.mkdir(cwd + "/" + IMG_DIR + "xml")
OUTPUT_DIR = "../../generated/xml/"


pathlist = Path(TXT_DIR).glob('*.txt')
for path in pathlist:
    path_in_str = str(path)
    with open(path_in_str) as f:
        print(path_in_str)
        contents = f.readlines()
    annotation = ET.Element("annotation")
    folder = ET.SubElement(annotation, "folder").text = ""
    filename = ET.SubElement(annotation, "filename").text = path_in_str[20 : -4] + ".png"
    path = ET.SubElement(annotation, "path").text = path_in_str[20 : -4] + ".png"
    source = ET.SubElement(annotation, "source")
    database = ET.SubElement(source, "database").text = ""
    
    size = ET.SubElement(annotation, "size")
    width = ET.SubElement(size, "width").text = str(IMG_WIDTH)
    height = ET.SubElement(size, "height").text = str(IMG_HEIGHT)
    depth = ET.SubElement(size, "depth").text = str(3)
    
    segmented = ET.SubElement(annotation, "segmented").text = "0"
    
    for c in contents:
        x = c.split()
    
        object = ET.SubElement(annotation, "object")
        name = ET.SubElement(object,"name").text = x[4]
        pose = ET.SubElement(object, "pose").text = "Unspecified"
        truncated = ET.SubElement(object, "truncated").text = "0"
        difficult = ET.SubElement(object, "difficult").text = str(x[5])
        occluded = ET.SubElement(object, "occluded").text = str(0)
        
        bndbox = ET.SubElement(object, "bndbox")
        xmin = ET.SubElement(bndbox, "xmin").text = str(x[0])
        ymin = ET.SubElement(bndbox, "ymin").text = str(x[1])
        xmax = ET.SubElement(bndbox, "xmax").text = str(x[2])
        ymax = ET.SubElement(bndbox, "ymax").text = str(x[3])
        tree = ET.ElementTree(annotation)
        
    tree.write(OUTPUT_DIR + path_in_str[20 : -4] + ".xml")
    


