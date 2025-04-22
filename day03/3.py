#Tuple -> data access는 list와 같지만, data update는 불가능하다.

tuple()
print(tuple())

my_tuple=(1,"hello", 3.14, True)
print(my_tuple)

#set -> data는 순서가 없다. set에는 동일한 값이 저장되지 않는다. set은 중괄호로 정의한다.
my_set = {1,2,3,2,2,1,2,3,32,3,2,32,2,1,2,3}
print(my_set)
my_set.add(4)
print(my_set)
my_set.add(10)
print(my_set)

event_A = set()
event_A.add(3)
event_A.add(100)
event_A.add(1)
event_A.add(2)
event_A.add(1)
print(event_A)

event_B = set()
event_B.add(100)
event_B.add(5)
event_B.add(7)
event_B.add(2)
print(event_B)

#합집합
print(event_A | event_B)

#교집합
print(event_A & event_B)

#차집합
print(event_A - event_B)