
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1

new_list.append(add_1)

#List comprehension

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

name = "Angela"
new_list = [letter for letter in name]
print(new_list)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]
print(result)

with open ("file1.txt") as file1:
    file1_data = file1.readlines()
    
with open ("file2.txt") as file2:
    file2_data = file2.readlines()
    
file12 = [int(number) for number in file1_data if number in file2_data]
print(file12)

#dictionary comprehension

import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)
passed_students = {student:score for (student, score) in students_scores.items() if score >= 80}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
print(weather_c)
print(weather_f)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

import pandas
student_df = pandas.DataFrame(student_dict)
print(student_df)

# for (key, value) in student_df.items():
#     print(value)

#Loop through rows of a data frame
for (index, row) in student_df.iterrows():
    print(row.student)


