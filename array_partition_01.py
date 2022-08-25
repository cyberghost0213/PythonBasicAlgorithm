# 배열 파티션
# n개의 페어를 이용한 min(a, b)의 합으로
# 만들 수 있는 가장 큰 수를 출력하라
# >>> [1,4,3,2]
# 4
#
# 오름차순 풀이

from typing import List

def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort() # nums 배열의 요소를 정렬

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n) # pair리스트에 n요소 추가
        if len(pair) == 2: # pair리스트의 길이가 2가 되면
            sum += min(pair) # pair의 작은 수를 sum에 더해준다. 
            pair = [] # pair 리스트를 비어준다.

    return sum