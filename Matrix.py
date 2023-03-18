# 행렬 : 2차원으로 구성된 숫자의 집합, list of list로 구현
from typing import List
from typing import Tuple
Vector=List[float]
Matrix=List[List[float]]

# 행렬의 행과 열 구하기
def shape(A:Matrix)->Tuple[int,int]:
    return (len(A),len(A[0]))
    # len(A)로 행의 개수를, len(A[0])으로 열의 개수
print(shape([[1,2,3],[4,5,6]]))

# i번째 행 얻기
def get_row(A: Matrix,i: int)->Vector:
    return A[i]
    # A의 i 번째 있는 행 return
print(get_row(([[1,2,3,4],[5,6,7,8]]),1))

# j번째 열 얻기
def get_col(A: Matrix,j: int)->Vector:
    return [A_i[j] for A_i in A]
    # A의 각 행의 j 번째 있는 열 return
print(get_col([[1,2,3,4],[5,6,7,8]],2))

# 행렬 만들기
# A[i,j] 값을 f(i,j)로 생성하는 함수
# 행과 열을 인수로 하는 함수 f를 만족하는 행렬 A 만들기
from typing import Callable
def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int,int],float])->Matrix:
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]
    # 처음 i가 선택될때 i 행의 모든 성분에 변화하는 j 값에 따른 함수값을 넣어주고 i가 1씩 증가하면서 행렬 완성
print(make_matrix(5,3,lambda i,j:i+j))

# 단위행렬(주대각선의 성분이 1, 그 외 성분은 0인 정사각행렬) 만들기
def identity_matrix(n: int)-> Matrix:
    # n은 단위행렬의 크기
    return make_matrix(n,n,lambda i,j:1 if i==j else 0)
    # entry_fn = 각 행과 열이 같은 경우 1을 다를 경우 0을 입력한다.
print(identity_matrix(5))

