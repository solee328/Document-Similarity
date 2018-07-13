import os
import spacy

# 한국어 품사 list
Noun = ['NNG', 'NNP', 'NNB', 'NNBC', 'NR', 'NP']
Verb = ['VV']
Adj = ['VA']
Adv = ['MAG', 'MAJ']
Dtm = ['MM']
F = ['SL']  # 한자 SH
Num = ['SN']
ETC = ['SY', 'SC']

# 영어 명사 list
E_Noun = ['PROPN', 'NOUN', 'NUM', 'PRON']

nlp = spacy.load('en_core_web_sm')


# 특정 품사만 가져와 만든다.
def make_pos():
    os.system("C:/Exception/Linux/test.bat /mnt/c/Exception/Linux/txt.txt")
    dir = 'C:/Exception/Linux/'
    data = read_data(dir + 'mecabtest.txt')
    word_list = split_morph(data)
    analysis_word = token_analysis(word_list)

    print(analysis_word)


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
        if part in Verb:
            tokens += word + ' '

        # 명사
        elif part in Noun:
            tokens += word + ' '

        # 형용사
        elif part in Adj:
            tokens += word + ' '

        # 부사
        elif part in Adv:
            tokens += word + ' '

        # 관형사
        elif part in Dtm:
            tokens += word + ''

        # 영어
        elif part in F:
            t_word = nlp(word)
            for t in t_word:
                if t.pos_ in E_Noun or t.pos_ == 'VERB' or t.pos_ == 'ADJ' or t.pos_ == 'X' or t.dep_ == 'neg':  # 영어 명사, 동사, 형용사, 부정적 의미만
                    tokens += t.text + " "

        # 숫자
        elif part in Num:
            tokens += word + ' '

        # 특수 기호
        elif part in ETC:
            tokens += word + ' '

    return tokens