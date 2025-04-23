# 하나의 수를 함수의 입력으로 받고 그 수까지의 짝수만 리스트로 만드는 함수
def make_even(num) :
  return list(range(2, num+1,2 ))
print(make_even(10))

#두 수를 입력받아서 두 수의 합을 구하여 리턴하는 함수
def sum(num1, num2) :
  result = num1 + num2
  return result
print(sum(10, 20))

#과일 등급을 반환하는 함수를 작성하시오.
def fruit_grade(size) :
  if 1<= size <= 10 :
    return "C등급"
  elif 11<= size <= 20 :
    return "B등급"
  elif 21<= size <= 30 :
    return "A등급"
  
grade = fruit_grade(15)
print(grade)