#1. a,b,c,의 값은?
a = 5
b = a+2
a=1
c=b-a
print(a,b,c)

#2. 1부터 150까지의 합
print(sum(range(1, 151)))

#3. 유저가 입력한 숫자에 해당되는 구구단을 하는 프로그랩 작성
# x = input('단 입력 : ')
x = 3
x = int(x)
if x<=1 or x>=10 :
  print('1~9사이의 숫자를 입력하세요')
else :
  for y in range(1,10):
    print(x, "X", y, "=", x*y)

#4. 1부터 100까지의 출력하되, 3의 배수에는 박수라는 글자 출력
for i in range(1, 101) :
  if i % 3 == 0 :
    print("박수")
  else :
    print(i)

#5. 유저한테 6번 숫자를 입력 받고, 그 수들 중에 음수의 개수를 출력
# cnt = 0
# for x in range(6) :
#   num = int(input('정수 입력 : '))
#   if num < 0 :
#     cnt += 1
# print("음수의 개수 : ", cnt)

#6. 유저한테 6번 숫자를 입력 받고. 그 수를 입력한 역순으로 출력
# number_list= []
# for x in range(6) :
#   num = int(input('정수 입력 : '))
#   number_list.append(num)
# print(number_list)
# print(number_list[::-1])

#7. 총 10명의 학생 점수 70,60,55,75,95,90,80,80,85,76이 있다. 각 학생의 점수에서 7점씩 뺴시오
score_list =[70,60,55,75,95,90,80,80,85,76]
for i in range(len(score_list)) :
  score_list[i] = score_list[i] - 7
print(score_list)

#8. 유저가 -1을 입력하면 종료. 학점을 구하는 프로그램 작성
while True :
  score = int(input('점수 입력 : '))
  if score == -1 :
    break
  elif score >= 85 :
    print("A")
  elif score >= 75 :
    print("B")
  elif score >= 65 :
    print("C")
  elif score >= 0 :
    print("D")
  else :
    print("F")