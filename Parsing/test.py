import MeCab
import sys


def read_data(filename):
    data =''
    with open(filename, 'r') as f:
        for line in f.read().splitlines():
            data += line
    return data


def morph(string, m):
    morphtoken = m.parse(string)
    print(morphtoken)
    return morphtoken


def writefile(morph):
    fw = open('/mnt/c/Exception/Linux/mecabtest.txt', 'w', encoding='utf-8')
    fw.write(morph)
    fw.close()


def main(filedir):
    m = MeCab.Tagger('d /usr/local/lib/mecab/dic/mecab-ko-dic')
    text = read_data(filedir)
    morphtoken = morph(text, m)
    writefile(morphtoken)


if __name__ == "__main__" :
    main(sys.argv[1])
