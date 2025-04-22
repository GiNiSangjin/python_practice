#print함수
sentence="안녕하세요"
print(sentence)

name="홍길동"
age=55
print('이름은 {}이고 나이는 {}세입니다.'.format(name, age))

#user input
name=input('이름을 입력하세요: ')
age=input('나이를 입력하세요: ')
print('이름은 {}이고 나이는 {}세입니다.'.format(name, age))

#형변환
number1 = input('첫 번째 숫자를 입력하세요: ')
number2 = input('두 번째 숫자를 입력하세요: ')
number1 = int(number1)
number2 = int(number2)
print('두 숫자의 합은 {}입니다.'.format(number1 + number2))

print(int(number1))
print(float(number1))
print(str(number1), str(123))