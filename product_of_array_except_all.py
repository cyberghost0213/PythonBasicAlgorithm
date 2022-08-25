# 자신을 제외한 배열의 곱
# 배열을 입력받아 output[i]가 자신을 제외한 
# 나머지 요소의 곱셈 결과가 되도록 출력하라
# 주의) 나눗셈을 하지 않고 O(n)에 풀이하라
# >>> [1,2,3,4]
# [24,12,8,6]
#
# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈

from typing import List

nums = [1,2,3,4]

def productExceptSelf(self, nums:List[int]) -> List[int]:
    out = []
    p = 1
    # 왼쪽곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i] # 반복문 다 들어갔을때 out = [1, 1, 2, 6]
    p = 1
    # 왼쪽 곱셈 결과에 오른족 값을 차례대로 곱셈
    for i in range(len(nums) -1, 0 -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out