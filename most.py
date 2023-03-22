import sys
import re
text=[line for line in sys.stdin] # \n을 기준으로 텍스트를 분리
count=0
str_value=''
past_word=''
# result 딕셔너리 만들기 key는 word, value 값은 count(글자 수)로
# result의 key값을 텍스트의 모든 장:절을 추가
result={word:[count,str_value]
        for line in text
        for word in line.strip().split()
        if re.match("\d+:\d+",word)}
# 처음 기준이 되는 result값 0으로 초기화, 딕셔너리 맨 마지막에 추가
result[past_word]=[count,str_value]

for line in text:
    for word in line.strip().split():
        # 장:절 형식이 나오면 0으로 초기화하고 다음 장:절이 나올때까지 단어의 수를 count에 더해준다.
        if re.match("\d+:\d+",word):
            if result[past_word][0]<count:
                result[past_word][0]=count
                # 마지막 문장에서 backspace가 추가되어 있으므로 그것을 빼서 초반 문장과 맞게 해준다.
                str_value=str_value-" "
                result[past_word][1]=str_value
            past_word=word
            count=0
            str_value=''
        else:
            str_value=str_value+word+" " # 해당 행과절에 어떤 문자열이 있었는지 추가
            count+=len(word)
# 마지막에 추가한 ''을 삭제
result.pop('')

# result 딕셔너리의 value에서 count의 최댓값 찾는 함수(=max_value)
# result.values() -> [[int,str]]
def max_value(list_value):
    max_v=0
    for i in result.values():
        if max_v<i[0]:
            max_v=i[0]
    return max_v


for k,v in result.items():
    if v[0]==max_value(result.values()):
        print("가장 큰 절 : ", k)
        print("해당 절의 글자 수(공백 제외) : ",v[0])
        print("해당 절의 내용 : ",v[1])
        break