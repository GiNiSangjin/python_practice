#list 만들기
sentence='hello'
print(sentence[0])

#비어있는 리스트 만들기1
[]
#비어있는 리스트 만들기2
list()

#리스트 만들기
print([90,80,70])

["홍길동", "김나나","이몽룡"]
print(["홍길동", "김나나","이몽룡"])

#여러 종류의 데이터로 리스트 만들기
['홍길동', 29, 1.75, True, [1,2,3]]
print(['홍길동', 29, 1.75, True, [1,2,3]])

#리스트 offset으로 값 가져오기
week = ['월', '화', '수', '목', '금', '토', '일']
print(week[0])
print(week[-1])
print(week[0:1])

#리스트에 항목 추가하기
week.append('일요일')
print(week)
week.insert(0, '일요일')
print(week)
del week[1]
print(week)
print(week.pop())
print(week)

my_list =['Mitch', [3,5,1], ['yellow',2,4]]
print(my_list[0])
print(my_list[1][0])

#리스트 + 연산
fruits=[]
fruits=list()
print(fruits)
fruits.append('apple')
print(fruits)
fruits.append('banana')
print(fruits)

others=['kiwi', 'melon']
fruits=fruits + others
print(fruits)