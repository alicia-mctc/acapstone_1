classes = []

class_n = input('Enter class name? Or enter Q to quit   ')

while class_n:
    classes.append(class_n)
    class_n = input('Enter class name? Or enter Q to quit  ')

print(classes)   

for i in classes:
    print(i)