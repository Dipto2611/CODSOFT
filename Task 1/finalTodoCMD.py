"""TASK 1"""

# TO-DO List using Cmd line

print("\n ------------------------------------ TO-DO Application --------------------------------------- \n")

Todo_task = []

#Add task :
def addtask(task):
        Todo_task.append(task)
        print(f"\nAdded -->> {task}\n")

#Del task :   
def deltask(task_ind):
        if 0 <= task_ind < len(Todo_task): #check index from start to end
            currtask = Todo_task.pop(task_ind)
            print(f"\nDeleted Task -->> {currtask}\n")
        else:
            print("\nInvalid task number.\n")

# Update task function
def updatetask(task_ind, new_task):
    if 0 <= task_ind < len(Todo_task):
        prevtask=Todo_task[task_ind]
        Todo_task[task_ind] = new_task #here new_task is assigned to that prev index and is updated
        print(f"\n{prevtask} is updated to {new_task}\n")
    else:
        print("\nInvalid task number.\n")

#Display task :
def displaytask():
        if not Todo_task:
            print("\nNo Task yet.\n")
        else:
            print("\nCurrent Tasks:\n")
            for index, task in enumerate(Todo_task, start=1): #As start will indicate the 0th index as 1st index thats why we didnt use index+1 case 
                print(f"{index}. {task}")
            print("")  #for printing a blank line we've used it


def main():
    while True:
        print("\n1. Add Task\n2. Delete Task\n3. Display Tasks\n4. Update Task\n5. Exit\n")
        
        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                task = input("Enter the task: ")
                addtask(task)
            
            elif choice == 2:
                if not Todo_task: ##if len(task)==0 then no output
                    print("\nNo tasks to delete.\n")
                else:
                    displaytask()
                    try:
                        task_ind = int(input("Enter task number to delete: ")) - 1
                        if 0 <= task_ind < len(Todo_task):
                            deltask(task_ind)
                        else:
                            print("\nInvalid task number.\n")
                    except ValueError:
                        print("\nPlease enter a valid number.\n")
                
            elif choice == 3:
                displaytask()
            
            elif choice == 4:
                if not Todo_task:
                    print("\nNo tasks to update.\n")
                else:
                    displaytask()
                    try:
                        task_ind = int(input("Enter task number to update: ")) - 1
                        if 0 <= task_ind < len(Todo_task):
                            new_task = input("Enter new task: ")
                            updatetask(task_ind, new_task)
                        else:
                            print("\nInvalid task number.\n")
                    except ValueError:
                        print("\nPlease enter a valid number.\n")
                
            elif choice == 5:
                print("\nExiting..\n")
                break
            
            else:
                print("\nInvalid choice. Please select a number between 1 and 5.")
        
        except ValueError:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

#call main
main()