

def todo_list():
    tasks = []



    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")



        choice = input("Choose an option: ")


        if choice == "1":
            task = input("Enter a new task: ")
            
            tasks.append(task)
            
            print("Task added!")
            
            
        elif choice == "2":
            
            
            print("\nYour Tasks:")
            
            for i, task in enumerate(tasks, start=1):
                
                print(f"{i}. {task}")
                
        elif choice == "3":
            
            task_num = int(input("Enter the task number to remove: ")) - 1
            
            if 0 <= task_num < len(tasks):
                
                
                removed = tasks.pop(task_num)
                
                print(f"Task '{removed}' removed!")
                
                
            else:
                print("Invalid task number.")
                
                
        elif choice == "4":
            
            print("Goodbye!")
            
            
            
            break
        else:
            print("Invalid choice. Please try again.")

todo_list()
