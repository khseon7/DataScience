from typing import List

Vector=List[float]

def add(v:Vector,w:Vector)->Vector:
    assert len(v)==len(w),"같은 차원이 아닙니다."
    # "len(v)==len(w)"가 벡터 v, w가 다른 차원일 경우 AssertError를 발생시켜
    # ""안에 있는 내용을 출력한다.
    return [v_i+w_i for v_i,w_i in zip(v,w)]

def substract(v:Vector,w:Vector)->Vector:
    assert len(v)==len(w),"같은 차원이 아닙니다."
    return [v_i-w_i for v_i,w_i in zip(v,w)]

print(add([1,2],[1,2]))
# add에서 AssertError가 발생할 경우 스탑이 걸려
# 밑에 있는 substract 함수가 작동하지 않는다.
print(substract([3,2],[1,1]))

# 벡터 리스트가 입력이 되었을 때 그것들의 합 벡터 구하기
# 1. 빈 벡터를 하나 만들어서(입력되는 리스트들과 차원이 같아야 한다.) 벡터 리스트들을 하나씩 더해준다.
# 2. 벡터 리스트에 있는 첫번재 벡터에 뒤에 것들을 하나씩 더해준다.

def vector_sum1(vectors: List[Vector])->Vector:
    assert all(len(vectors[0])==len(vectors[i]) for i in range(len(vectors))),"차원이 다른 벡터가 존재합니다."
    res=[0]*len(vectors[0]) #입력된 벡터들과 차원이 같은 벡터 생성
    for i in range(len(vectors)):   #새로 만든 벡터에 리스트 내의 벡터들을 하나씩 더해주는 함수
        res=add(res,vectors[i])
    return res

def vector_sum2(vectors: List[Vector])->Vector:
    assert all(len(vectors[0])==len(vectors[i]) for i in range(len(vectors))),"차원이 다른 벡터가 존재합니다."
    for i in range(1,len(vectors)): #입력된 벡터들중 리스트의 첫번째에 있는 벡터에 나머지를 더해 줌으로 range 범위는 1부터 시작
        vectors[0]=add(vectors[0],vectors[i])
    return vectors[0]

print(vector_sum1([[1,2,3,4],[0,1,2,3],[1,2,4,5]]))
print(vector_sum2([[1,2,3,4],[0,1,2,3]]))

# 벡터의 상수배 구하기
def scalar_multiply(c:float,v:Vector)->Vector:
    return[c*v_i for v_i in v] # 각 성분(v_i)에 c를 곱해준다.

print(scalar_multiply(5,[1,2,3,4,5]))

# 벡터의 성분별 평균
def vector_mean(vectors:List[Vector])->Vector:
    assert all(len(vectors[0])==len(vectors[i]) for i in range(len(vectors))),"차원이 다른 벡터가 존재합니다."
    return scalar_multiply(1/len(vectors),vector_sum1(vectors))
    # 위의 vector_sum1 or vector_sum2 함수를 사용하여 각 성분의 합을 구한 후
    # scalar_multiply를 이용하여 리스트의 길이만큼 나누어 준다.

print(vector_mean([[1,2,3,4],[3,4,5,6]]))