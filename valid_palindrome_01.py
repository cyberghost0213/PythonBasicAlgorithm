# 유효한 팰린드럼
# 주어진 문자열이 팰린드럼인지 확인하라. 
# 대소문자를 구별하지 않고, 영문자와 숫자만을 대상으로한다.
# "A man, a plan, a canal: Panama" -> true
# "race a car" -> false

def isPalindrome(self, s: str) -> bool:
    strs = []

    for char in s:
        if char.isalnum():            # 영문자, 숫자 여부를 확인하는 함수
            strs.append(char.lower()) # 소문자로 바꿔준 후 strs 리스트에 넣어준다.

    while len(strs) > 1: 
        if strs.pop(0) != strs.pop(): # strs 리스트에서 첫번째요소와 마지막요소의 값이 다르면
            return False              # False

    return True                       # 같으면 True