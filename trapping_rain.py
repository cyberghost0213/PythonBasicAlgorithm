# 빗물 트래핑
# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산해라
# >>> [0, 1, 0, 2, 0, 1, 3, 2, 1, 2, 1]
#
# 투 포인터를 최대로 이동

from typing import List

def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
        # 더 높은 쪽을 향해 투 포인터를 이동
        if left_max <= right_max:
            volume += left_max - height[left] # 좌우 기둥 최대 높이와 현재 높이의 차 = 물 volume
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


