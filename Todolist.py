#  Here is a to do list in python:

todo = []
with open("Saved.txt" , 'r') as f:
    lines = f.readlines()
    for i in lines:
        print(i)

def save_tasks():
    l =[]
    with open("Saved.txt" , 'a') as f:
        for i in todo:
            #l.append(i)
            f.write(i + "\n")

    
while True:
    print("1. Add Task ")
    print("2. View Task Number")
    print("3. View all tasks ")
    print("4. Remove Task")
    print("5. Exit")

    choice = int(input())

    if(choice ==1):
        task = input("Enter the task you want to add: ")
        todo.append(task)
        # with open("Saved.txt" , 'a') as f:
        #     f.write(task + "\n")
        save_tasks()
    elif(choice == 2):
        task_num = int(input("Enter which task number you want to enter: "))
        print(todo[task_num])
    elif(choice == 3):
        for i in todo:
            print(i)
    elif(choice == 4):
        if not todo:
            print("No tasks to remove: ")
        else:
            try:    
                rem_tsk = int(input("Which task you want to remove: "))
                todo.pop(rem_tsk)
                # with open("Saved.txt", 'a') as f:
                #     for i in todo:
                #         f.write(i + "\n")
                save_tasks()
            except ValueError:
                print("Enter a number!!!! ")
               
    elif(choice == 5):
        print("Have a nice day :) ")
        break
    else:
        print("Invalid choice ")
