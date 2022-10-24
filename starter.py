# print('hello world')
# first_name= 'Chris'
# last_name= 'Langley'


# age= 14

# if age >= 18:
#     print('I am a adult')
# elif age < 13: 
#     print('I am an infant')
# else:
#     print('I am a aliean')

# favorite_numbers = [1,2,3,4,True,'hello',23.4]
# print(favorite_numbers)

# for number in favorite_numbers:
#     print(number)

# def sum(num_1,num_2):
#     return num_1 + num_2

# print(sum(2,4))
   


open_file= open('FinalGrades.csv')
# total_a = 0
# total_b = 0
# total_c = 0


# for line in open_file:
#     line = line.strip()
#     values = line.split(',')
#     for value in values:
#         if value == "A":
#             total_a +=1
#         elif value == "B":
#             total_b +=1
#         elif value == "C":
#             total_c += 1

# print(total_a)
# print(total_b)
# print(total_c)

for line in open_file:
    line = line.strip()
    values = line.split(',')
    print(values[2: 5])



