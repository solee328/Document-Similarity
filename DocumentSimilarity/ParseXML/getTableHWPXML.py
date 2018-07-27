from xml.etree.ElementTree import parse

# 필요한 태그 값만 가져오기 위함
TAG = ['TABLE', 'ROW', 'CELL', 'SCRIPT', 'TEXT', 'P', 'CHAR']


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


# 필요한 태그만 가져오며 태그 사이에 글이 있다면 같이 가져오도록 함
def get_tag(parse_result):
    tag = ''
    for node in parse_result.iter('TABLE'):
        tag += '<TABLE> '
        for elem in node.iter():
            if not elem.tag == node.tag:
                tmp = elem.text

                if tmp is not None and tmp[0] == '\n':
                    tmp = ''

                if elem.tag in TAG:
                    # TEXT 태그는 출력하지 않는다(SCRIPT와 CHAR로 구별)
                    if elem.tag == 'TEXT':
                        continue
                    else:
                        tag += "<{}> {} ".format(elem.tag, tmp)
    return tag


def return_result(file_path):
    tree = parse(file_path)
    result = get_tag(tree)
    return result
