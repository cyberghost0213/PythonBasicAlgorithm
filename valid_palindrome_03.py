# 유효한 팰린드럼 3
# 주어진 문자열이 팰린드럼인지 확인하라. 
# 대소문자를 구별하지 않고, 영문자와 숫자만을 대상으로한다.
# "A man, a plan, a canal: Panama" -> true
# "race a car" -> false

# 슬라이싱을 이용해 문제 풀기

import re

def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('^a-z0-9', '', s)

    return s == s[::-1] # 슬라이싱을 이용해서 리스트 뒤집기