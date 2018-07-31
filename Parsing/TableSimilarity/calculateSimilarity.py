import Parsing
from operator import eq
from TableSimilarity import tableScanner
from TableSimilarity import calculate_MN
from scipy.special import ndtri

def calculate_form(current_file, form_file):

    space_list = [' ', '  ', " ", "  "]

    #각각 행과 열에 대한 헤더를 레벨 별로 저장하는 list
    table_row_list = []
    table_col_list = []
    form_row_list = []
    form_col_list = []

    table = Parsing.get_file(current_file)
    form = Parsing.get_file(form_file)

    table_list = tableScanner.scan_table(table)
    form_list = tableScanner.scan_table(form)

    #테이블과 폼을 레벨별로 나눔
    for table_row_index in range(0, len(table_list)):
        space = 0
        temp_header = []
        for table_col_index in range(0, len(table_list[table_row_index])):
            if eq(form_list[table_row_index][table_col_index].contents, '  ') or eq(form_list[table_row_index][table_col_index].contents, " ") \
                    or eq(form_list[table_row_index][table_col_index].contents, ' '):
                space += 1
            elif table_list[table_row_index][table_col_index].merge_final:
                temp_header.append(table_list[table_row_index][table_col_index].contents)
        if space < 2:
            temp_header = list(set(temp_header))
            table_row_list.append(temp_header)

    for table_col_index in range(0, len(table_list[0])):
        space = 0
        temp_header = []
        for table_row_index in range(0, len(table_list)):
            if eq(form_list[table_row_index][table_col_index].contents, '  ') or eq(form_list[table_row_index][table_col_index].contents, " ") \
                    or eq(form_list[table_row_index][table_col_index].contents, ' '):
                space += 1
            elif table_list[table_row_index][table_col_index].merge_final:
                temp_header.append(table_list[table_row_index][table_col_index].contents)
        if space < 2:
            temp_header = list(set(temp_header))
            table_col_list.append(temp_header)

    for table_row_index in range(0, len(form_list)):
        space = 0
        temp_header = []
        for table_col_index in range(0, len(form_list[table_row_index])):
            if eq(form_list[table_row_index][table_col_index].contents, '  ') or eq(form_list[table_row_index][table_col_index].contents, " ") \
                    or eq(form_list[table_row_index][table_col_index].contents, ' '):
                space += 1
            elif form_list[table_row_index][table_col_index].merge_final:
                temp_header.append(form_list[table_row_index][table_col_index].contents)
        if space < 2:
            temp_header = list(set(temp_header))
            form_row_list.append(temp_header)

    for table_col_index in range(0, len(form_list[0])):
        space = 0
        temp_header = []
        for table_row_index in range(0, len(table_list)):
            if eq(form_list[table_row_index][table_col_index].contents, '  ') or eq(form_list[table_row_index][table_col_index].contents, " ") \
                    or eq(form_list[table_row_index][table_col_index].contents, ' '):
                space += 1
            elif form_list[table_row_index][table_col_index].merge_final:
                temp_header.append(form_list[table_row_index][table_col_index].contents)
        if space < 2:
            temp_header = list(set(temp_header))
            form_col_list.append(temp_header)

    sum_similarity = 0
    min_row_level = (len(table_row_list)) if len(table_row_list) < len(form_row_list) else len(form_row_list)
    min_col_level = (len(table_col_list)) if len(table_col_list) < len(form_col_list) else len(form_col_list)

    for level_index in range(min_row_level-1, -1, -1):
        level_similarity = calculate_MN.calculate_similarity_level(table_row_list[level_index], form_row_list[level_index])
        gravity = ndtri(0.51 + (0.48 / min_row_level) * (level_index + 1))
        sum_similarity += level_similarity * gravity

    for level_index in range(min_col_level-1, -1, -1):
        level_similarity = calculate_MN.calculate_similarity_level(table_col_list[level_index], form_col_list[level_index])
        gravity = ndtri(0.51 + (0.48 / min_col_level) * (level_index + 1))
        sum_similarity += level_similarity * gravity

    return sum_similarity
