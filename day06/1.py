def fahr_to_kelvin(temp) :
  result = (temp - 32) * 5 / 9 + 273.15
  return result

print(fahr_to_kelvin(100))

def print_hello() :
  print("hello")
  print("world")

print_hello()

def squared(number) :
  result = number ** 2
  return result

print(squared(3))

def pow_times(number, times) :
  result = number ** times
  return result
print(pow_times(2, 3))

def my_funct(number1, number2) :
  result1 = number1 // number2
  result2 = number1 % number2
  return result1, result2

print(my_funct(10, 3))

def say_hello(name, age) :
  print("제이름은 {}이고 나이는 {}살 입니다.".format(name, age))

say_hello("홍길동", 20)