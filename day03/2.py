#values 전부 곱한 값을 출력하는 코드
my_dict = {'data1':500,
           'data2':-10,
           'data3':300}
print(my_dict['data1'] * my_dict['data2'] * my_dict['data3'])

#각 학생별로 중간과 기말의 평균 점수를 구하시오
student_details = [
  {'student_id' : 1, 'subject' : 'math', 'midterm' : 60, 'final' : 85},
  {'student_id' : 2, 'subject' : 'math', 'midterm' : 80, 'final' : 78},
  {'student_id' : 3, 'subject' : 'math', 'midterm' : 90, 'final' : 85}
]
avg1 = (student_details[0]['midterm'] + student_details[0]['final']) / 2
avg2 = (student_details[1]['midterm'] + student_details[1]['final']) / 2
avg3 = (student_details[2]['midterm'] + student_details[2]['final']) / 2
print(avg1)
print(avg2)
print(avg3)

#위에서 구한 평균점수를 "Average"라는 키값으로 추가하여 출력하시오
student_details[0]['Average'] = avg1
student_details[1]['Average'] = avg2
student_details[2]['Average'] = avg3
print(student_details[0])
print(student_details[1])
print(student_details[2])

#각각의 숫자를 제곱한 값으로 바꾸세요.
dictionary = {'C1' : [10,20,30],
              'C2' : [20,30,40]}
dictionary['C1'][0] = dictionary['C1'][0] ** 2
dictionary['C1'][1] = dictionary['C1'][1] ** 2
dictionary['C1'][2] = dictionary['C1'][2] ** 2
dictionary['C2'][0] = dictionary['C2'][0] ** 2
dictionary['C2'][1] = dictionary['C2'][1] ** 2
dictionary['C2'][2] = dictionary['C2'][2] ** 2
print(dictionary['C1'])
print(dictionary['C2'])

#(1) 모든 키를 리스트로 출력하세요
#(2) 모든 밸류를 리스트로 출력하세요
#(3) 모든 밸류의 값을 다 더하세요
my_salary = {"alex": 25, "sally": 28, "dina": 30}
print(my_salary.keys())
print(my_salary.values())

print(my_salary.values())
print(list(my_salary.values()))

print(sum(my_salary.values()))
print(max(my_salary.values()))
print(min(my_salary.values()))

#(1)dictionary의 길이를 구하세요
#(2)나이에 대한 오름차순으로 정렬하세요
my_dict = {"sally": 23, "dina": 22, "holy": 50, "Joe": 10, "Peter": 44}
print(len(my_dict))
print(sorted(my_dict.items(), key=lambda x: x[1]))