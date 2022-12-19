helloworld = input("Hello World")
first_name = input('Enter your First Name: ')
last_name = input('Enter your Last Name: ')
user_phone = input('Enter your Phone No.: ')
user_phone = int(user_phone)
user_email = input('Enter your Email: ')
user_email = str(user_email)
age = input('Enter your Age: ')
if age.isdigit():
    age = int(age)
    if age>=18:
        print('You are an Adult')
    elif age>=10 and age<18:
        print("You are a Teenager")
    elif age>3 and age<10:
        print("You are a Child")
else:
    print(f'{age} is not a Digit. Please enter Integer Values')
currentyear = 2021
birthyear = input("Enter your year of Birth (YYYY): ")
birthyear = int(birthyear)
user_age = currentyear - birthyear
print(f"Your age is {user_age}")
user_city = input('Enter you City: ')
user_state = input('Enter your State: ')
user_country = input('Enter your Country: ')
user_hobby = input("Enter your Hobby (Any Two): ")



print(f'Your First Name is {first_name} ')
print(f'Your Last Name is {last_name} ')
print(f'Your Phone No is {user_phone}')
print(f'Your Email is {user_email}')
print(f'Your Age is {age}')
print(f'Your City is {user_city}')
print(f'Your State is {user_state }')
print(f'Your Country is {user_country}')
print(f'Your Hobby is {user_hobby}')
