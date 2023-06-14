import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
def convert_yolo_to_xml(yolo_annotations_dir, output_dir, classes):
    for filename in os.listdir(yolo_annotations_dir):
        if filename.endswith(".txt"):
            image_name = os.path.splitext(filename)[0]
            yolo_annotation_path = os.path.join(yolo_annotations_dir, filename)
            xml_output_path = os.path.join(output_dir, image_name + ".xml")
            with open(yolo_annotation_path, "r") as file:
                lines = file.readlines()
            root = Element("annotation")
            folder = SubElement(root, "folder")
            folder.text = "YourFolderName"
            filename = SubElement(root, "filename")
            filename.text = image_name + ".jpg"
            size = SubElement(root, "size")
            width = SubElement(size, "width")
            height = SubElement(size, "height")
            depth = SubElement(size, "depth")
            img_width = 1920
            img_height = 1080
            img_depth = 23
            width.text = str(img_width)
            height.text = str(img_height)
            depth.text = str(img_depth)
            for line in lines:
                class_index, x, y, w, h = map(float, line.split())
                class_name = classes[int(class_index)]
                xmin = int((x - (w / 2)) * img_width)
                ymin = int((y - (h / 2)) * img_height)
                xmax = int((x + (w / 2)) * img_width)
                ymax = int((y + (h / 2)) * img_height)
                obj = SubElement(root, "object")
                name = SubElement(obj, "name")
                name.text = class_name
                bndbox = SubElement(obj, "bndbox")
                xmin_tag = SubElement(bndbox, "xmin")
                ymin_tag = SubElement(bndbox, "ymin")
                xmax_tag = SubElement(bndbox, "xmax")
                ymax_tag = SubElement(bndbox, "ymax")
                xmin_tag.text = str(xmin)
                ymin_tag.text = str(ymin)
                xmax_tag.text = str(xmax)
                ymax_tag.text = str(ymax)
            xml_data = parseString(tostring(root)).toprettyxml(indent="\t")
            with open(xml_output_path, "w") as xml_file:
                xml_file.write(xml_data)
                
                
                
yolo_annotations_dir = "test/labels"
output_dir = "test/xml"
classes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']

convert_yolo_to_xml(yolo_annotations_dir, output_dir, classes)
