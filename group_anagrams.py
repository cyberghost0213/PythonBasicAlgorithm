# 그룹 애너그램
# 문자열 배열을 받아 애너그램 단위로 그루핑하라
# >>> ["eat", "tea", "tan", "ate", "nat", "bat"]
# >>> {
# >>>       ["ate", "eat", "tea"],
# >>>       ["nat", "tan"],
# >>>       ["bat"]
# >>> }
# 
# 정렬하여 딕셔너리에 추가
# 애너그램 관계의 단어들을 정렬하면 같은 값을 가지기 때문에 정렬해서 비교한다.
# 정렬한 후 join() 함수로 합쳐준 다음에 이 값을 키로 사용한다.

import collections
from typing import List

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values()) # 딕서녀리의 값을 리턴

groupAnagrams()