#유저로부터 문장을 입력받고 그 문장을 공백기준 단어로 분리하여 출력하세요
sentence = input("문장을 입력하세요: ")
print(sentence.split())

#문자열을 입력 받고 모두 대문자로 변경하여 출력하세요
sentence = input("문장을 입력하세요: ")
print(sentence.upper())

#다음의 이메일 주소에서 이메일의 아이디 부분과 도메인 부분을 분리하여 출려하세요
email = 'cs_team@company.co.kr'
print(email.split('@'))

#다음 문장에서 앞의 so를 제거하고 뒤의 town을 제거한 문자열을 출력
sentence = 'So it is quite different, then, if in a mountain town'
sentence = sentence[2:-4]
print(sentence)