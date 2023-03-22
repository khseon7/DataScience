import sys
import re
text=[line for line in sys.stdin] # \n을 기준으로 텍스트를 분리
count=0
past_word=''
# result 딕셔너리 만들기 key는 word, value 값은 count(글자 수)로
# result의 key값을 텍스트의 모든 장:절을 추가
result={word:count
        for line in text
        for word in line.strip().split()
        if re.match("\d+:\d+",word)}
# 처음 기준이 되는 result값 0으로 초기화, 딕셔너리 맨 마지막에 추가
result[past_word]=count

for line in text:
    for word in line.strip().split():
        # 장:절 형식이 나오면 0으로 초기화하고 다음 장:절이 나올때까지 단어의 수를 count에 더해준다.
        if re.match("\d+:\d+",word):
            if result[past_word]<count:
                result[past_word]=count
            past_word=word
            count=0
        else:
            count+=len(word)
# 마지막에 추가한 ''을 삭제
result.pop('')

for k,v in result.items():
    if v==max(result.values()):
        print("가장 큰 절 : ", k)
        print("해당 절의 글자 수(공백 제외) : ",v)
        break

