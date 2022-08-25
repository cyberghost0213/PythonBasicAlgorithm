# 세 수의 합
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라
# >>> nums = [-1, 0, 1, 2, -1, -4]
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
# 브루트 포스로 계산

from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort() # nums 배열을 정렬 해준다.

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i -1]:
            continue
        for j in range (i + 1, len(nums) -1):
            if j > j + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])
    return results