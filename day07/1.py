#난수 생성하기
import random
print(random.random())

print (random.randint(1, 10))
print(random.uniform(1,5))


print(random.randint(1,10))

noodle_list = ['너구리', '신라면', '진라면', '왕뚜껑', '오징어짬뽕']
print(random.choice(noodle_list))

# random.shuffle(noodle_list)
# print(noodle_list)

random.sample(noodle_list, len(noodle_list))
print(noodle_list)

data = [6, 4, 5, 2, 2, 1, 6, 6, 3]

import statistics
print(statistics.mean(data))
print(statistics.median(data))

data.append(8)
sorted(data)

from datetime import date
print(date.today())

some_day = date(2023, 10, 31)
print(some_day)