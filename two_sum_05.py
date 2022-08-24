# 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# >>> nums = [2, 7, 11, 15] , target = 9
# [0, 1]
#
# 투 포인터를 사용해서 풀어보자
# 투 포인터는 왼쪽 포인터와 오른쪽 포인터의 합이 
# 타겟보다 크다면 오른쪽 포인터를 왼쪽으로
# 왼쪽 포인터를 오른쪽으로 옮기면서 값을 조정한다.

def twoSum(self, nums, target):
    left, right = 0, len(nums) -1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

### nums가 정렬된 상태가 아니라서 투 포인터로 풀 수 없다.
### 인덱스를 찾는 문제에서 인덱스를 섞어버리면
### 원래의 인덱스를 찾기 더 힘들어진다.