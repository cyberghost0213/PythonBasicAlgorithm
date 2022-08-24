# 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# >>> nums = [2, 7, 11, 15] , target = 9
# [0, 1]
#
# 조회 구조 개선
# 두개로 나누어져있던 for문 두개를 합치자

def twoSum(self, nums, target):
    nums_map = {}
    
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [i, nums_map[target - num]]
        nums_map[num] = i