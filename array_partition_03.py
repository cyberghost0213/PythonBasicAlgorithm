# 배열 파티션
# n개의 페어를 이용한 min(a, b)의 합으로
# 만들 수 있는 가장 큰 수를 출력하라
# >>> [1,4,3,2]
# 4
#
# 파이썬다운 방식
# 슬라이싱을 사용해서 풀기

from typing import List

def arrayPairSum(sef, nums:List[int]) -> int:
    return sum(sorted(nums)[::2]) # sorted()로 정렬된 nums 리스트 요소를 
                                  # 2칸씩 건너뛰면서 더해준다.