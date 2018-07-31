#!/usr/bin/python
#-*-coding:utf8;-*-
import os
import codecs

from glob import glob
import os.path
from FileToXML import DocxtoXML, HwptoHWPML, DoctoDocx


# self == file_path
def get_extension(self):
    extension = self.rpartition(".")[-1]
    if extension == 'doc':
        doc(self)
    elif extension == 'docx':
        docx(self)
    elif extension == 'hwp':
        hwp(self)
    else:
        print("This file is not supported")
        exit(1)


# self == file_path
def doc(self):
    # Create list of paths to .doc files
    self = self.replace("/", "\\")
    paths = glob(self, recursive=True)

    for path in paths:
        DoctoDocx.save_as_docx(path)

    fn_ext = os.path.splitext(self)
    self = fn_ext[0] + '.docx'
    docx(self)


# self == file_path
def docx(self):
    file = DocxtoXML.make_xml(self)

    fn_ext = os.path.splitext(self)
    f = codecs.open(fn_ext[0] + '.xml', 'w', encoding='utf8')
    f.write(file)
    f.close()


def hwp(self):
    HwptoHWPML.make_xml(self)