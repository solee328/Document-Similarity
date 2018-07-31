import random

class TableCell:
    merge_final = False
    val = 1
    contents = ""

    def __init__(self):
        self.merge_final = True
        self.val = 0
        self.contents = " "

    def setMergeStart(self):
        self.merge_final = True

    def merge(self):
        self.merge_final = False

    def setGrid(self, val):
        self.val = val

    def setContents(self, content):
        self.contents = content

