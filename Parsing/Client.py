import Parsing
from AnalyMorph import TextPOS
from TableSimilarity import calculateSimilarity

file_list = []
form_file_list = []

class Form_Similairity:
    file_name = ""
    similarity = 0


while(True):
    print("=================================MENU================================")
    print("(A) Add file (F) Add Form file (L) List of file (U) Usage of table")
    option = input()

    if option == 'A' or option == 'a':
        file_list.append(input("Input file path(.doc/ .docx/ .hwp)"))
    elif option == 'F' or option == 'f':
        form_file_list.append(input("Input form file path(.doc/ .docx/ .hwp)"))
    elif option == 'L' or option == 'l':
        print("==========File============")
        index = 0
        for file_index in file_list:
            print("(%d) : %s " % (index+1, file_index))
            index += 1
        print("========Form File========")
        index = 0
        for file_index in form_file_list:
            print("(%d) : %s " % (index+1, file_index))
            index += 1
    elif option == 'U' or option == 'u':
        print("==========File============")
        index = 0
        for file_index in file_list:
            print("(%d) : %s " % (index + 1, file_index))
            index += 1
        print(">>Select the number of files to compare.")
        current_file = file_list[int(input()) - 1]
        print("Similarity with [%s]" % (current_file))
        list_similarity = []
        for form_file_index in form_file_list:
            temp = Form_Similairity()
            temp.file_name = form_file_index
            temp.similarity = calculateSimilarity.calculate_form(current_file, form_file_index)
            list_similarity.append(temp)
        list_similarity.sort(key=lambda Form_Similairity : Form_Similairity.similarity)
        print("          Form name            |            Similarity            ")
        print("================================================================")
        for similarity_list in list_similarity:
            print(" %22s  | %20f %% " % (similarity_list.file_name, similarity_list.similarity))
        print("\n[%s] file used [%s]\n" % (current_file, list_similarity[0].file_name))
    else:
        print("Error")
