Document-Similarity
=========================

문서 유사도 판단 시스템

__FileToXML__  
Word(.doc/ .docx)와 한글(.hwp)파일이 입력으로 주어지며 이를 OOXML(.doc/ .docx)과 HML(.hwp)파일로 만드는 과정이다.
<br><br>


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
<br><br>


__AnalyMorph__
일반 텍스트와 테이블을  분리하여 형태소 분석과정을 진행한다.

현재는 일반 텍스트만 진행된 상태이다.
GetTags를 통해 배치파일과 저장된 일반 텍스트 문서위치 값을 인자로 주어 CMD 창을 통해 리눅스에서 meCab()을 실행한 결과 값을 다시 일반 텍스트 파일로 저장한다.
저장된 일반 텍스트 파일을 열어 Tagging된 형태소를 제거한 후 space를 단위로 단어를 나누어 한줄로 만든 string을 return한다.
