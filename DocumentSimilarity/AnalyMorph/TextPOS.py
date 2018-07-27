# -*- coding:utf-8 -*-
import os
import spacy
import os.path
from os.path import splitext

# 한국어 품사 list
F = ['SL']  # 한자 SH
posLetter = ['SN', 'SY', 'SC', 'XR']

# 영어 명사 list
E_Noun = ['PROPN', 'NOUN', 'NUM', 'PRON']

nlp = spacy.load('en_core_web_sm')


# 특정 품사만 가져와  단어 파일을 만든다.
def make_pos(file_path):

    os.system("C:/Exception/Linux/test.bat /mnt/c/Exception/Linux/txt.txt")
    dir = 'C:/Exception/Linux/'
    data = read_data(dir + 'mecabtest.txt')
    word_list = split_morph(data)
    analysis_word = token_analysis(word_list)
    write_data(file_path, analysis_word)


# fn_ext[0] : directory except file_name
# fn_ext[1] : file_name include extension
# fn_ext[2] : extension
def write_data(file_path, word_data):
    fn_ext = os.path.split(file_path)

    if os.path.isfile(fn_ext[0]+'\words.txt'):
        file_name = open(fn_ext[0]+'\words.txt', 'a', encoding='utf-8')
    else:
        file_name = open(fn_ext[0]+'\words.txt', 'w', encoding='utf-8')

    file_name.write(word_data)
    file_name.close()

    file_text = open(splitext(file_path)[0] +'.txt', 'w', encoding='utf-8')
    file_text.write(word_data)
    file_text.close()

    print(word_data)


def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines() if line != 'EOS']
    return data


def split_morph(data):
    words = []
    for row in data:
        morph = row[1].split(',')
        words += [(row[0], morph[0])]
    return words


def token_analysis(words):
    tokens = ''

    for word, part in words:
        # 동사
        if part[0] == 'N' or part[0] == 'V' or part[0] == 'M':
            tokens += word + ' '

        elif part in posLetter:
            tokens += word + ' '

        # 영어
        elif part in F:
            t_word = nlp(word)
            for t in t_word:
                # 영어 명사, 동사, 형용사, 부정적 의미만
                if t.pos_ in E_Noun or t.pos_ == 'VERB' or t.pos_ == 'ADJ' or t.pos_ == 'X' or t.dep_ == 'neg':
                    tokens += t.text + " "
    return tokens
