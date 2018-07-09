from FileToXML import FileChange
from ParseXML import getTags
file_path = ""


def get_file():
    global file_path
    file_path = input("Input file path(.doc/ .docx/ .hwp) >> ")
    FileChange.get_extension(file_path)


def parse():
    global file_path
    getTags.get_extension(file_path)