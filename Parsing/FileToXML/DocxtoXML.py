import zipfile


# self == file_path
def make_xml(self):
    # read word file
    docx = zipfile.ZipFile(self)

    # xml 형태로 내용 읽기
    content = docx.read('word/document.xml').decode()
    return content