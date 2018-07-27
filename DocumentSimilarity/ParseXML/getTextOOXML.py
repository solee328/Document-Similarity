import zipfile
import xml.etree.ElementTree as ET

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'
CELL = WORD_NAMESPACE + 'tc'
TBL = WORD_NAMESPACE + 'tbl'
ROW = WORD_NAMESPACE + 'tr'


class docx():
    def make_xml(string):
        # read word file
        docx = zipfile.ZipFile(string)
        # xml 형태로 내용 읽기
        content = docx.read('word/document.xml').decode('utf-8')
        docx.close()
        return content

    def xml_string_tree(tree):
        for parent in tree.iter():
            for child in parent.findall('.//TABLE/*'):  # 테이블 하위 태그 child 저장
                child.clear()

        tblCount = 0
        ptxt = ''
        # tree내 table 위치 파악과 일반 text 출력
        for root in tree.iter():
            # table 위치 파악
            if root.tag == 'TABLE':
                tblCount += 1
                new_tbl = root.tag + '#' + str(tblCount)
                root.tag = new_tbl
                ptxt += new_tbl + '\n'

            # 일반 text 구문 출력
            else:
                if root.tag == 'P':
                    tags = root.findall('.//TEXT')
                    if tags:
                        texts = [element.text for element in tags]
                        result = ''.join(texts)
                        ptxt += result + ' '
        return ptxt

    def xml_table_tree(tree):
        paras = []

        # table 태그 검색후 안의 텍스트 내용 출력
        for a in tree.iter('CELL'):
            for para in a.iter('P'):
                texts = [node.text
                         for node in para.iter('TEXT')
                         if node.text]
                if texts:
                    paras.append(''.join(texts))
        return '\n'.join(paras)

    # parsing에 필요한 tag를 hwpml의 형식으로 change
    def change_tag_to_hwpml(tree):
        for parent in tree.iter():
            for child in parent.findall(TBL):
                child.tag = 'TABLE'

        for parent in tree.iter():
            for child in parent.findall(PARA):
                child.tag = 'P'

        for parent in tree.iter():
            for child in parent.findall(ROW):
                child.tag = 'ROW'

        for parent in tree.iter():
            for child in parent.findall(CELL):
                child.tag = 'CELL'

        for parent in tree.iter():
            for child in parent.findall(TEXT):
                child.tag = 'TEXT'


def return_result(file_path):
    tree = ET.parse(file_path)
    docx.change_tag_to_hwpml(tree)
    node = docx.xml_string_tree(tree)
    return node

