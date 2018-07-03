import zipfile
import xml.etree.ElementTree as ET

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'
CELL = WORD_NAMESPACE + 'tc'
TBL = WORD_NAMESPACE + 'tbl'
ROW = WORD_NAMESPACE + 'tr'


def apply_indent(elem, level=0):
    # tab = space * 2
    indent = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = indent + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
        for elem in elem:
            apply_indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = indent


def xml_string_tree(tree):
    for parent in tree.iter():
        for child in parent.findall('.//' + TBL + '/*'):  # 테이블 하위 태그 child 저장
            child.clear()

    tblCount = 0
    ptxt = ''
    # tree내 table 위치 파악과 일반 text 출력
    for root in tree.iter():
        # table 위치 파악
        if root.tag == TBL:
            tblCount += 1
            new_tbl = root.tag + '#' + str(tblCount)
            root.tag = new_tbl
            ptxt += new_tbl + '\n'

        # 일반 text 구문 출력
        else:
            if root.tag == PARA:
                tags = root.findall('.//' + TEXT)
                if tags:
                    texts = [element.text for element in tags]
                    result = ''.join(texts)
                    ptxt += result + '\n'
    return ptxt


def change_tag_to_xml(tree_string):
    for parent in tree_string.iter():
        for child in parent.findall('TABLE'):
            child.tag = TBL

    for parent in tree_string.iter():
        for child in parent.findall('P'):
            child.tag = PARA

    for parent in tree_string.iter():
        for child in parent.findall('ROW'):
            child.tag = ROW

    for parent in tree_string.iter():
        for child in parent.findall('CELL'):
            child.tag = CELL

    for parent in tree_string.iter():
        for child in parent.findall('CHAR'):
            child.tag = TEXT


def return_result(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    xmlstr = ET.tostring(root).decode('utf-8')
    tree = ET.fromstring(xmlstr)
    change_tag_to_xml(tree)

    node = xml_string_tree(tree)
    return node

