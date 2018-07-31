from FileToXML import FileChange
from ParseXML import getTags


def get_file():
    file_path = input("Input file path(.doc/ .docx/ .hwp) >> ")
    FileChange.get_extension(file_path)
    return file_path


def parse(file_path):
    getTags.get_extension(file_path)