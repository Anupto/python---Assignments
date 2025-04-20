
name = input("Enter the Student's name: ")

MarkList = {"Anoop": 95, "Anish": 91, "Neeraj": 85, "Anand": 82}

if name in MarkList:
    print(f'{name}\'s marks: {MarkList[name]}')
else:
    print('Student not found.')




