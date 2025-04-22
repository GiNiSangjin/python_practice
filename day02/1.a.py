#문자열 만들기
sentnece ='''내가 말했다. \n"빨리 출발해"'''
print(sentnece)

#3개의 단일 부호로 문자열을 만들 수 있다. 
poem = '''So "it is" quite different, then, if in a mountain town
the mountains are close, rather than far. Here

they are far, their distance away established,
consistent year to year, like a parent’s

or sibling’s. They have their own music.
So I confess I do not know what it’s like,

listening to mountains up close, like a lover,
the silence of them known, not guessed at.'''
print(poem)

#문자열에서 +기호 사용하기
first_name="Mitch"
last_name="Hedberg"
full_name=first_name+' '+last_name
print(full_name)

#대소문자로 변경 가능
full_name=full_name.upper()
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(full_name.capitalize())

#문자열을 원하는 기준으로 나누기
print(full_name.split())
print(full_name.split('H'))
print(full_name.split('H',1))
print(full_name.split('H',2))
print(full_name.split('H',3))

#문자열 추출
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[-1])
print(letters[-3])
print(letters[0:3])
print(letters[1:-1])
print(letters.replace('a','A'))

#문자열 일부 추출하기
# abcde 를 가져오시오
print(letters[0:5])
print(letters[:5])
# 뒤에서 세번째부터 끝까지 가져오시오
print(letters[-3:])
# 홀수번쨰 있는 문자만 추출하기
print(letters[::2])

# 문자열 길이 구하기
print(len(letters))

#공백 자르기
email = '     hello@naver.com'
print(email)
email = email.strip()
print(email)
email=email.strip('h')
print(email)

#문자열 위치 찾기
print(poem.find('year'))
print(poem.rfind('year'))

#문자열의 갯수 파악
print(poem.count('year'))
print(poem.count('banana'))

#있니? 없니??? 로 파악하는 방법
print('year' in poem)
print('banana' in poem)
print('banana' not in poem)
text='안녕하세요? 오늘 날씨가 좋네요.'
print(text.startswith('안녕하세요'))
print(text.endswith('안녕하세요'))