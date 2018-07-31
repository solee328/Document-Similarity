from EmbedWord import FastText
import os
from gensim.test.utils import get_tmpfile


def read_data(filename):
    tokenized_text = []
    line_count = 1
    word_list = []
    with open(filename, "r", encoding='utf-8', errors='ignore') as f:
        # contents = f.read()         # 크기 : 100,000,000바이트
        while True:
            line = f.readline()
            if not line : break
            tokenized_text += line.split(' ')

    return tokenized_text


file = 'C:/Exception/Download/'
file_list = [ 'C:/Exception/Download/1.txt',
              'C:/Exception/Download/2.txt',
              'C:/Exception/Download/3.txt',
              'C:/Exception/Download/4.txt',
              'C:/Exception/Download/5.txt',
              'C:/Exception/Download/6.txt',
              'C:/Exception/Download/7.txt',
              'C:/Exception/Download/8.txt',
              'C:/Exception/Download/9.txt',
              'C:/Exception/Download/10.txt',
              'C:/Exception/Download/11.txt',
              'C:/Exception/Download/12.txt'
]
similarity_list = []

file_path = input("Input file path(.doc/ .docx/ .hwp) >> ")
model = FastText.make_model('C:/Exception/Download/words.txt')


fn_ext = os.path.split(file_path)
file_name = get_tmpfile(fn_ext[0]+'\wordsModel')

for file in file_list:
    similarity = model.n_similarity(
        read_data(file_path), read_data(file))
    similarity_list.append(similarity)

m = similarity_list.index(max(similarity_list))

print(similarity_list)
