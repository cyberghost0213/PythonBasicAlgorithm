# 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# >>> nums = [2, 7, 11, 15] , target = 9
# [0, 1]
#
# 첫번째 수를 뺀 결과 키 조회
# 시간 복잡도를 개선해보자
# 비교나 탐색 대신 한번에 정답을 맞출수는 없을까?
#
# 타겟에서 첫 번째 수를 뺴면 두 번째 수를 바로 알아 낼 수 있다.
# 두 번째 수를 키로 하고 기존의 인덱스는 값으로 바꿔서 딕셔너리에 저장하면
# 두 번쨰 수를 키로 조회해서 정답을 바로 찾아낼 수 있다.
# 딕셔너리는 해시테이블로 구현되어있고 
# 조회는 평균적으로 O(1) 최악은 O(n) 분할상환분석에 따르면 O(1)

def twoSum(self, nums, target):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장 // 딕셔너리 nums_map의 키는 num 값은 i
    for i, num in enumerate(nums):
        nums_map[num] = i 

    # 타겟으로 첫 번째 수를 뺀 결과를 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i !=nums_map[target - num]:
            return [i, nums_map[target - num]] 



