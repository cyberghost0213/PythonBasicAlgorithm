# 가장 긴 팰린드롬 부분 문자열
# 가장 긴 팰딘드롬 부분 문자열을 출력하라
# >>> "babad"
# "bad"
#
# >>> "cbbd"
# "bb"
#
# 중앙을 중심으로 확장하는 풀이
# 두 포인터가 중앙을 중심으로 확장하는 형태로 풀이
# 팰린드럼은 판별만 하면된 된다. 
# => 매칭이 될 때 중앙을 중심으로 점점 확장해 나가면서
# 가장 긴 팰린드럼을 판별하는 알고리즘을 구현하자

def longestPalindrome(self, s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s
