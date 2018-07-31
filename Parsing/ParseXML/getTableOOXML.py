from xml.etree.ElementTree import parse
import xml.etree.ElementTree as ET

# namespace
WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'
CELL = WORD_NAMESPACE + 'tc'
MERGE = WORD_NAMESPACE + 'vMerge'
GRID = WORD_NAMESPACE + 'gridSpan'
TBL = WORD_NAMESPACE + 'tbl'
ROW = WORD_NAMESPACE + 'tr'

# 필요한 태그 값만 가져오기 위함
TAG = ['TABLE', 'ROW', 'CELL', 'MERGE', 'GRID', 'SCRIPT', 'TEXT', 'P', 'SCRIPT']


def apply_indent(elem, level=0):
    # tab = space * 2
    indent = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = indent + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
        for elem in elem:
            apply_indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = indent


def change_tag_to_hwpml(tree_string):
    for parent in tree_string.iter():
        for child in parent.findall(TBL):
            child.tag = 'TABLE'

    for parent in tree_string.iter():
        for child in parent.findall(PARA):
            child.tag = 'P'

    for parent in tree_string.iter():
        for child in parent.findall(ROW):
            child.tag = 'ROW'

    for parent in tree_string.iter():
        for child in parent.findall(CELL):
            child.tag = 'CELL'

    for parent in tree_string.iter():
        for child in parent.findall(MERGE):
            child.tag = 'MERGE'

    for parent in tree_string.iter():
        for child in parent.findall(GRID):
            child.tag = 'GRID'

    for parent in tree_string.iter():
        for child in parent.findall(TEXT):
            child.tag = 'TEXT'


# 전체 string에서 필요한 태그만 가져오며 태그 사이에 글이 있다면 같이 가져오도록 함
def get_tag(parse_result):
    tag = ''
    for node in parse_result.iter('TABLE'):
        tag += '<TABLE> '
        for elem in node.iter():
            if not elem.tag == node.tag:
                tmp = elem.text

                if tmp is not None and tmp[0] == '\n':
                    tag += ''

                if elem.tag in TAG:
                    if elem.tag == 'P':
                        tags = elem.iter('TEXT')
                        if tags is not None and tags is not '':
                            text_string = ''.join([element.text for element in tags])
                            tag += "<{}> {} ".format(elem.tag, text_string)

                    elif elem.tag == 'TEXT':
                        continue

                    elif elem.tag == 'CELL' or elem.tag == 'ROW':
                        tag += "<{}> ".format(elem.tag)

                    elif elem.tag == 'MERGE' or elem.tag == 'GRID':
                        tag += "<{}> {} ".format(elem.tag, elem.get(WORD_NAMESPACE+'val'))

                    else:
                        tag += "<{}> {}".format(elem.tag, tmp)
    return tag


def return_result(file_path):
    tree = ET.parse(file_path)

    root = tree.getroot()
    apply_indent(root)

    xmlstr = ET.tostring(root, encoding='utf8', method='xml').decode()

    tree_string = ET.fromstring(xmlstr)
    change_tag_to_hwpml(tree_string)

    result = get_tag(tree_string)
    return result