#dictionaries and boolean dictionaries
my_phone = {'brand' : 'apple' ,'model': 'iPhone16 Pro Max', 'year':2025 }
print(my_phone)
print(my_phone['brand'])
print(my_phone['model'])
print(my_phone['year'])

my_phone.get('brand')
print(my_phone.get('brand'))

my_phone['model'] = 'iPhone 17 Pro Max'
print(my_phone)

my_phone['color']='Titanium Black'
print(my_phone)

#dictionary data delete
del my_phone['color']
print(my_phone)

#dictionary key값들만 가져오기
my_phone.keys()
print(my_phone.keys())

#dictionary value값들만 가져오기
my_phone.values()
print(my_phone.values())

#dictionary key, value 쌍으로 가져오기
my_phone.items()
print(my_phone.items())

#my_phone에 brand, model, year, color가 있는지 확인하기
print('brand' in my_phone)
print('model' in my_phone)  
print('year' in my_phone)
print('color' in my_phone)
print('color' not in my_phone)

my_list=[5,1,2,4]
print(my_list)
my_list.clear()
print(my_list)

print(len(my_phone))