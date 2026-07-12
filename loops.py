#Loops:
# 
#  for i in range (5,10):
#     print(i)

# list in example

# test_cases = ['TC001','TC002','TC003']

# for i in test_cases:
#     print(i)

# range and len in loops

# test_case = ['vk1','vk2','vk3']

# for i in range(len(test_case)):
#     print(i, test_case[i])

# for loop with if condition
# results = [200,400,500,800,250,300]
# for code in results:
#     if code == 250:
#         print(f"{code}: Pass")
#     else:
#         print(f'{code}: Fail')

#own example
# results = [200,400,500,800,250,300]
# for code in results:
#     if code == 800:
#         print(f'{code}: Pass')
#     elif code==400:
#         print(f"{code}: Error")
#     else:
#         print(f"{code}: Fail")


# #practice Task (ill create my own names and timings)
# response_time = [2.0,1.1,4.8,3.6,1.9,2.3,2.0,5.5]

# for time in response_time:
#     if time > 4:
#         print(f"{time}: Slow")
#     elif time>2:
#         print(f"{time}: Ok")
#     else:
#         print(f"{time}: Fast")

#Write a for loop that goes through this list: scores = [85, 45, 92, 38, 67] and prints "Pass" if the score is 50 or above, and "Fail" if it's below 50.
scores = [85,45,92,38,67]
for mark in scores:
    if mark > 50:
        print('Pass')
    else:
        print('fail')