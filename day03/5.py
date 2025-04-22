lang1 = ["C", "C++", "Java"]
lang2 = ["Python", "JavaScript", "Go"]

langs = lang1 + lang2
nums = [1,2,3,4,5,6,7]

print(max(nums))
print(min(nums))
print(sum(nums))

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest)
print(''.join(interest))
print(' '.join(interest) )
print('?'.join(interest))
print('!!!@'.join(interest))
print('/'.join(interest))
print('\n'.join(interest))

string = "삼성전자/LG전자/Naver"
string = string.split('/')
print(string)

data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))