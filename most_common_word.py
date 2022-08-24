# 가장 흔한 단어
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분을 하지않으며, 구두점(마침표, 쉼표) 또한 무시한다.
# >>> paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
# >>> banned = ["hit"]
# ball
#
# 리스트 컴프리핸션, Counter객체 이용
# 입력값에는 대소문자, 쉼표,구두점등이 존재한다.
# 데이터 클렌징 (Data cleansing)이라 불리는 입력값에 대한 전처리 과정이 필요하다.
import collections
import re

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    word = [word for word in re.sub(r'[^\w]', ' ', paragraph) # 리스트 컴프리핸션
        .lower().split()
            if word not in banned]

    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 리턴
    return counts.most_common(1)[0][0] 
