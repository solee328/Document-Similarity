Document-Similarity
=========================

문서 유사도 판단 시스템

__FileToXML__  
Word(.doc/ .docx)와 한글(.hwp)파일이 입력으로 주어지며 이를 OOXML(.doc/ .docx)과 HML(.hwp)파일로 만드는 과정이다.



__GetTags__  
FileToXML을 통해 변경된 OOXML과 HML에서 태그 값을 가져오는 과정이다.
현재 인식 가능하게 처리한 태그는 아래와 같다.
1. TABLE/ tbl
2. P/ p
3. ROW/ tr
4. CELL/ tc
5. CHAR/ t

왼쪽의 태그가 한글의 HML, 오른쪽 태그가 워드의 OOXML 태그이며 태그들을 하나로 합치기 위해 워드의 OOXML 태그의 형식을 HML 태그의 형식으로 바뀌었다.

CHAR 태그의 경우 P 태그 안에 포함되는 태그로 P 태그가 문장 별로 나타나, CHAR 태그는 피요없다 판단하여 CHAR 태그 안에 표현되던 텍스트 값을 CHAR 태그를 제거한 후 P 태그 안에 포함되도록 구현되어져 있다.
