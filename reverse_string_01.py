# 문자열 뒤집기
# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며,  
# 리턴 없이 리스트 내부를 직접 조작하라.
# >>> ["h","e","l","l","o"]
# >>> ["o","l","l","e","h"]
#
# >>> ["H","a","n","n","a","h"]
# >>> ["h","a","n","n","a","H"]
#
# 투 포인터 이용한 스왑
# 2개의 포인터를 이용해 범위를 조정해가면서 풀이

def reverseString(self, s:List[str]) -> None:
    left, right = 0, len(s) - 1               # left와 right을 리스트 인덱스의 첫번째와 마지막을 할당
    while left < right:                       # 엇갈릴때까지 반복
        s[left], s[right] = s[right], s[left] # 두 포인터를 인덱스로 가지는 요소들을 바꿔준다. 
        left += 1
        right -= 1