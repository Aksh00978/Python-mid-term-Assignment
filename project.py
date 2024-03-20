'''
   **(<<PYTHON PROJECT>>)**
   To-Do List         
'''
print('\n\n*(^o^)*')
print('To-Do List-->')
Tasks = {}

def add(task):
    index = len(Tasks) + 1
    Tasks[index] = task

def remove(index):
    if index in Tasks:
        del Tasks[index]
    else:
        print("Task does not exist!!!")

def display():
    if Tasks:
        print("Your Tasks:")
        for index, task in Tasks.items():
            print(f"{index}. {task}")
    else:
        print("Your list is empty.")

while True:
    print('''
    1. Add task
    2. Remove task
    3. Display tasks
    4. Exit\n''')
    user_ch = input("Enter your choice: ")

    if user_ch == "1":
        task = input("Enter the task: ")
        add(task)

    elif user_ch == "2":
        index = int(input("Enter the index of the task to remove: "))
        remove(index)

    elif user_ch == "3":
        display()

    elif user_ch == "4":
        print("**----___________________Exiting program___________________----**")
        break

    else:
        print("Invalid choice. Please try again .")

#End of the Program ;)
        