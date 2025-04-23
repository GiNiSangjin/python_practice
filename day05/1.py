score = [90, 45, 77, 83, 39]

score[0] = score[0] - 5
print(score[0])

for data in score :
  print(data)

new_list = []

for math in score :
  print(math-5)
  new_list.append(math-5)
print(new_list)

sentence = 'Hello World~'
for letters in sentence :
  print(letters)

fruits = ['apple', 'blueberries', 'mango' , 'watemelon']

new_list= []
for name in fruits :
  print(name.upper())
  new_list.append(name.upper())

my_phone = {'brand' : 'apple', 'model' : 'iPhone 12', 'color' :'red', 
          'year' : 2021}

for data in my_phone :
  print(data.upper())

#values 보여주기
my_phone.values()

for data in my_phone.values() :
  dataUpper = str(data).upper()
  print(dataUpper)

#key values를 tuple로 보여주기
for data in my_phone.items() :
  print(data)

#key values를 각각 가져와서 원하는 처리를 함
for key, value in my_phone.items() :
  print(key, value)

my_list = ["A", "B", "C"]
for data in my_list: 
  print(data)

for name in fruits :
    print(name)
    if name == 'mango' :
        break
    
range(10)
print(list(range(10)))
print(list(range(5,14+1)))

print(list(range(2,18+1,2)))

for data in range(3+1) :
  print("hello")

i = 0
while i < 3 :
  print("bye")
  i += 1

# while True :
#   sentence = input("문장을 입력하세요 : ")
#   if sentence == 'stop'or sentence == '그만' :
#     break
#   print(sentence)

for X in range(2, 9+1) :
  for Y in range(1, 9+1) :
    print(X, "X", Y, "=", X*Y)
  print('-----------------------')

my_list = [1, 2, 3, 4, 5]
new_list=[]
for data in my_list :
  new_list.append(data**2)

print(new_list)

my_list = [1,2,3,4,5,6,7,8,9,10]
my_list[1: : 2]
print(my_list[1: : 2])
new_list = []
for data in my_list[1: : 2] :
  new_list.append(data ** 2)

print(new_list)

my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for data in my_list :
  if data % 2 == 0 :
    new_list.append(data**2)
print(new_list)