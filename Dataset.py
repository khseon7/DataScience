from typing import List

# 평균값
def mean(xs: List[float])->float:
    return sum(xs)/len(xs)

# 중앙값
def median(v: List[float])->float:
    return sorted(v)[len(v)//2] if len(v)%2==1 else mean([sorted(v)[len(v)//2],sorted(v)[len(v)//2-1]])
assert median([1,10,2,9,5])==5
assert median([1,10,2,9,])==5.5

# 분위 : 전체 자료를 특정 개수로 나눌때 그 기준이 되는 수
def quantile(xs: List[float],p:float)->float:
    p_index=int(p*len(xs))
    return sorted(xs)[p_index]

# 최빈값
from collections import Counter
def mode(x:List[float])->List[float]:
    return [m for m in Counter(x).keys() if Counter(x)[m]==max(Counter(x).values())]
print(set(mode([1,2,3,4,5,6,7,8,1,1,6,6])))

# 산포도
# 분위 범위 : 3/4 분위값 - 1/4 분위값
from Vector import sum_of_squares

def de_mean(xs: List[float])->List[float]:
    x_bar=mean(xs)
    return [x-x_bar for x in xs]

def variance(xs: List[float])->float:
    assert len(xs)>=2,"variance requires at least two elements"
    n=len(xs)
    deviations=de_mean(xs)
    return sum_of_squares(deviations)/(n-1)
    # n-1 instead of n when 표본 분산 구할 때

import math

def standard_deviation(xs: List[float])->float:
    return math.sqrt(variance(xs))
    # 표준편차

def interquartile_range(xs:List[float])->float:
    return quantile(xs,0.75)-quantile(xs,0.25)

# 공분산 구현
# 두 벡터가 독립이면 공분산 0
from Vector import dot  # dot 두 벡터 내적하는 함수
def covariance(xs: List[float],ys: List[float])->float:
    assert len(xs)==len(ys),"xs와 ys의 구성 성분 개수가 같아야한다."
    return dot(de_mean(xs),de_mean(ys))/(len(xs)-1)

# 상관계수
# 절대값은 최대 1
# 공분산/(두 벡터의 표준편차의 곱)
def correlation(xs: List[float],ys:List[float])->float:
    stdev_x=standard_deviation(xs)  #xs 벡터 표준편차
    stdev_y=standard_deviation(ys)  #ys 벡터 표준편차
    if stdev_x>0 and stdev_y>0:
        return covariance(xs,ys)/stdev_x/stdev_y
    else:
        return 0