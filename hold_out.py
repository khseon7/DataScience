import random
from typing import TypeVar, List, Tuple 
X=TypeVar('X') # generic type to represent a data point

def split_data(data:List[X],prob:float)->Tuple[List[X],List[X]]:
    # float 값을 기준으로 data 리스트 나누기
    return data[:int(prob*len(data))],data[int(prob*len(data)):]
    
data = [n for n in range(1000)]
train, test=split_data(data,0.75)
    
    
assert len(train) == 750
assert len(test) == 250

assert sorted(train + test) == data