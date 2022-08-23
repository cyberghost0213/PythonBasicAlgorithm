# 유효한 팰린드럼 2
# 주어진 문자열이 팰린드럼인지 확인하라. 
# 대소문자를 구별하지 않고, 영문자와 숫자만을 대상으로한다.
# "A man, a plan, a canal: Panama" -> true
# "race a car" -> false
# 데크로 명시적으로 선언해서 속도를 더 높일 수 있다.

import collections

def isPalindrome(self, s: str) -> bool:
    
    strs: Deque = collections.deque()     # 데크를 명시적으로 선언

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft(0) != strs.pop(): # 리스트의 Pop(0)는 O(n) 데크의 PopLeft()은 O(1)
            return False                  # 많은 성능 차이가 난다.

    return True