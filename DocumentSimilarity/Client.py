import Parsing
from AnalyMorph import TextPOS
from EmbedWord import FastText
file_path = ""

file_path = Parsing.get_file()
Parsing.parse(file_path)

TextPOS.make_pos(file_path)

# text 파일
FastText.make_model(file_path)
