# 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# >>> nums = [2, 7, 11, 15] , target = 9
# [0, 1]
#
# 브루트 포스로 계산
# 배열을 2번 반복하면서 모든 조합을 더해서 
# 일일이 확인해보는 무차별 대입 방식

from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]