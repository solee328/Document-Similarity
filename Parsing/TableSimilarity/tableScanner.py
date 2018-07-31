from operator import eq
from TableSimilarity import tableCell

TAG = ['TABLE', 'ROW', 'CELL', 'MERGE', 'GRID', 'SCRIPT', 'TEXT', 'P', 'SCRIPT']


def scan_table(table):
    table_list = []
    table = table.split()
    table.append("<END>")
    if not eq(table[0], "<TABLE>"):
        print("Fomatting Error")
        return;

    col = 0
    row = 0
    word_index = 1
    while word_index < len(table) - 1:
        if eq(table[word_index], "<ROW>"):
            word_index += 1
            if eq(table[word_index], "<CELL>"):
                col = 0
                temp_table = []
                word_index += 1
                repeat = 1
                temp_cell = tableCell.TableCell()
                while True:
                    if eq(table[word_index], "<GRID>"):
                        word_index += 1
                        repeat = int(table[word_index])
                        word_index += 1

                    if eq(table[word_index], "<MERGE>"):
                        word_index += 1
                        if eq(table[word_index], "restart"):
                            temp_cell.merge_final = True
                        elif eq(table[word_index], "None"):
                            temp_cell.merge_final = True
                            flag = False
                            #아래꺼 고쳐야함!~!~!
                            for goTop in range(row-1, -1, -1):
                                if table_list[goTop][col].merge_final:
                                    flag = True
                                    table_list[goTop][col].merge_final = False
                                    temp_cell.contents = table_list[goTop][col].contents
                            if not flag:
                                print("테이블 형식 오류입니다")
                                return;

                    if eq(table[word_index], "<P>"):
                        word_index += 1
                        if not eq(table[word_index][0], "<"):
                            while not eq(table[word_index][0], "<"):
                                temp_cell.contents += ' ' + table[word_index]
                                word_index += 1
                        else:
                            temp_cell.contents += ' '

                    if eq(table[word_index], "<CELL>") or eq(table[word_index], "<ROW>") or eq(table[word_index], "<END>"):
                        for re in range(0, repeat):
                            temp_table.append(temp_cell)
                            col += 1
                        temp_cell = tableCell.TableCell()
                        repeat = 1
                    if eq(table[word_index], "<ROW>") or eq(table[word_index], "<END>"):
                        break
                    word_index += 1
        table_list.append(temp_table)
        row += 1

    return table_list
