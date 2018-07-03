from FileToXML import Extension

file_path = ""


def get_file():
    global file_path
    file_path = input("Input file path(.doc/ .docx/ .hwp) >> ")
    Extension.get_extension(file_path)


def parse():
    print("parse from parsing")