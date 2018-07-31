from FileToXML import FileChange
from ParseXML import getTags


def get_file(file_path):
    FileChange.get_extension(file_path)
    result = getTags.get_extension(file_path)
    return result