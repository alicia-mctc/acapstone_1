yourname = input("What is your name?")
your_birthday = input("What month were you born in?") 
print(f'Hello, {yourname}!')

if your_birthday.lower() == 'august':
    print("Happy birthday to YOU!")

print(f'There are {len(yourname)} characters in your name.')