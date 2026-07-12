#Functions

# def dayone():
#     print("Welcome to functions part")

# dayone()

#Functions with parameters
# def verify(age):
#     if age == 18:
#         print("Valid age to login")
#     else:
#         print("Invalid age, cant login")

# verify(42)
# verify(12)
# verify(18)

#Function with multiple parameters
# def age(user, valid):
#     if user >= valid:
#         print("User is valid ")
#     else:
#         print(f"User is invalid as his age is {user} and the minimum age is {valid}")

# age(12,18)
# age(18,18)
# age(25,18)

# def attempts(min,max):
#     return min < max
# result = attempts(1,3)
# print(result)
# if result == True:
#     print('try another attempt')
# else:
#     print('max attempts reached')

# def status(code, threshold=500):
#     if code == threshold:
#         print('connection success')
#     else:
#         print('connection failed')

# status(200)
# status(200,400)
# status(500)

# def status(code, threshold=500):
#     return code == threshold

# print(status(200))
# print(status(500))

# practice task

# def timing(response_time):
#     if response_time <= 2:
#         print('True')
#     else:
#         print('False')

#     return response_time <=2
# result1 = timing(1)
# result2 = timing(2)
# result3 = timing(3)

# print(f"The timing 1 is {result1}")
# print(f"The timing 2 is {result2}")
# print(f"The timing 3 is {result3}")
        
# def get_grade(marks):
#     print(marks >= 50)

# result = get_grade(75)
# print(result)

# Q3
# def is_valid_age(age):
#     if age >=18 and age<=60:
#         return True
#     else:
#         return False
# result = is_valid_age(25)
# print(result)
# def a(age):
#     if age >=18 and age<=60:
#         return 'valid age'
#     else:
#         return 'invalid age'
# result = a(50)
# print(result)
