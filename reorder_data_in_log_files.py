# 로그 파일 재정렬
# 로그의 가장 앞 부분은 식별자다.
# 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
# 숫자 로그는 입력 순서대로 한다.
#
# >>> logs = ["dig1 8 1 5 1", "let1 art can", "dig 2 3 6", "let2 own kit dig", "let3 art zero"]
# >>> ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1, 8, 1, 5, 1", "dig  2, 3, 6"]
#
# 람다와 + 연산자를 이용

def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit(): # 첫번째 요소가 문자열인지 확인
            digits.append(log)       # 숫자열이면 digits 리스트에 추가
        else:
            letters.append(log)      # 문자열이면 letters 리스트에 추가

    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits