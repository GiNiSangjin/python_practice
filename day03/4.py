#Hello Chanel, you are 26 years old!
my_tuple=('Chanel', 26)
print("Hello {}, you are {} years old!".format(my_tuple[0], my_tuple[1]))

#(1) 모든 튜플 출력 (2) 마지막 값 출력 (3) 첫 번째와 두 번째 출력
my_tuple = ("chanel", "mitch", "sarah", "cynthia", "diane", "steeve")
print(my_tuple)
print(my_tuple[-1])
print(my_tuple[0:2])

#(1) 튜플의 길이 구하기 (2) 타입 확인하기
my_tuple = ("Ryan", "ahmed", 25)
print(len(my_tuple))
print(type(my_tuple))

#(1) 40출력하기 (2) "world" 출력하기 (3) 25 출력하기 (4) 두번째 요소로 저장되어 있는 리스트 출력 (5) 맨 마지막 요소인 튜플 출력
my_tuple = ("hello", [87, 40, 60], "world", (10, 25, 30))
print(my_tuple[1][1])
print(my_tuple[2])
print(my_tuple[-1][1])
print(my_tuple[1])
print(my_tuple[-1])

#(1) python 있는지 확인 (2) Python 있는지 확인 (3) physics 있는지 확인
my_tuple = ('math','science','science','python','english')
print('python' in my_tuple)
print('Python' in my_tuple)
print('physics' in my_tuple)

#동일한 값들을 제거하여 유니크한 값들의 리스트로 만들기
my_list = ["2", 50, "2", 50, 4, 6, 9, 9]
my_list = list(set(my_list))
print(my_list)

#내 이름을 추가하고 출력하기
my_set = {"sara", "mike", "jon", "jon", "mike"}
my_set.add("sangjin")
print(my_set)