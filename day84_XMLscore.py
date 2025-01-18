import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    total = len(node.attrib)
    for child in node:
        total += get_attr_number(child)
    return total;
    

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
