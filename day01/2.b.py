#유저한테 kmh값을 받으면 그에 맞는 mph값을 계산하는 코드를 만드세요.
kmh = input('kmh를 입력하세요: ')
kmh = int(kmh)
mph = kmh * 0.6214
print('mph:', mph)

#유저한테 년도와 월을 입력받으세요. 그리고나서 해당 년도와 월을 출력하는 코드를 만드세요
import calendar
year = input('년도를 입력하세요: ')
month = input('월을 입력하세요: ')
year = int(year)
month = int(month)
print(calendar.month(year, month))

#유저한테 두개의 float을 입력받아서 두 수의 곱과 합을 출력하는 코드를 만드세요
number1 = input('첫 번째 숫자를 입력하세요: ')
number2 = input('두 번째 숫자를 입력하세요: ')
number1 = float(number1)
number2 = float(number2)
print('두 숫자의 합은 {}입니다.'.format(number1 + number2))
print('두 숫자의 곱은 {}입니다.'.format(number1 * number2))