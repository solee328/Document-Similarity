from gensim.models import FastText
from gensim.test.utils import get_tmpfile
import os
from os.path import splitext


# MemoryError를 방지하기 위해 word_list를 추가하였다
# tokenized_text의 길이가 1억을 넘게되면 word_list에 추가한 후 다시 단어를 이어 받도록 항
def read_data(filename):
    tokenized_text = []
    line_count = 1
    word_list = []
    with open(filename, "r", encoding='utf-8', errors='ignore') as f:
        # contents = f.read()         # 크기 : 100,000,000바이트
        while True:
            line = f.readline()
            if not line:
                break
            tokenized_text += line.split(' ')

            if len(tokenized_text) > 100000000:
                word_list.append(tokenized_text)
                tokenized_text.clear()

            line_count += 1

    word_list.append(tokenized_text)
    return word_list


def make_model(file_path):
    fn_ext = os.path.split(file_path)
    file_name = get_tmpfile(fn_ext[0]+'\wordsModel')
    model_counter = 0

    words = read_data(splitext(file_path)[0] +'.txt')
    # tokens = [[t] for t in words]

    if os.path.isfile(fn_ext[0] + '\wordsModel'):
        for word in words:
            model = FastText.load(file_name)
            model.build_vocab(word, update=True)
            model.train(word, total_examples=model.corpus_count, epochs=model.iter,
                        hs=0, negative=5, iter=10, alpha=0.1, sg=1, word_ngrams=1, min_count=1,
                        size=100, window=5, workers=3)
            model.save(file_name)

    else:
        for word in words:
            if model_counter == 0:
                model = FastText(word, hs=0, negative=5, iter=10, alpha=0.1, sg=1,
                                 word_ngrams=1, min_count=1, size=100, window=5, workers=3)
                model.save(file_name)
                model_counter += 1
            else:
                model = FastText.load(file_name)
                model.build_vocab(word, update=True)
                model.train(word, total_examples=model.corpus_count, epochs=model.iter,
                            hs=0, negative=5, iter=10, alpha=0.1, sg=1, word_ngrams=1, min_count=1,
                            size=100, window=5, workers=3)
                model.save(file_name)