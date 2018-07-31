import random
import operator

class Similarity:
    def __init__(self, word1_index, word2_index, value):
        self.word1_index = word1_index
        self.word2_index = word2_index
        self.value = value

    def __repr__(self):
        return repr((self.word1_index, self.word2_index, self.value))

    @staticmethod
    def keyfunc1(c):
        return c.value


def calculate_similarity_level(list_word1, list_word2):
    sum_similarity = 0

    # 완전히 겹치는 값 구함
    for word1 in list_word1:
        if word1 in list_word2:
            sum_similarity += 1

    # 겹치지 않는 값들
    temp_list_word1 = set(list_word1)
    list_word1 = [x for x in list_word1 if x not in list_word2]
    list_word2 = [x for x in list_word2 if x not in temp_list_word1]

    similarity_list = []

    for word1_index in list_word1:
        for word2_index in list_word2:
            temp = Similarity(word1_index, word2_index, calculate_similarity_word(word1_index, word2_index))
            similarity_list.append(temp)

    # 최소 신장 트리 알고리즘 사용
    similarity_list.sort(key=operator.attrgetter('value'))

    select_word1_index = []
    select_word2_index = []

    min_num = min(len(list_word1), len(list_word2))
    num_select = 0
    index = len(similarity_list) - 1
    similarity_list.sort(key=lambda Similarity : Similarity.value)

    while num_select < min_num:
        if similarity_list[index].word1_index not in select_word1_index:
            if similarity_list[index].word2_index not in select_word2_index:
                sum_similarity += similarity_list[index].value
                select_word1_index.append(similarity_list[index].word1_index)
                select_word2_index.append(similarity_list[index].word2_index)
                num_select += 1
        index -= 1

    return sum_similarity


def calculate_similarity_word(word1, word2):
    return random.random()
