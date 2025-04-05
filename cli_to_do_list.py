import os

# Define the file path inside the "tasks" folder
# FOLDER_PATH = os.getcwd() # Autmoatic find the current path
FOLDER_PATH = "tasks"
FILENAME = os.path.join(FOLDER_PATH, "tasks.txt")


def ensure_folder_and_file_exist():
    """Create the 'tasks' folder if it does not exist."""
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
    
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()


def load_task():

    ensure_folder_and_file_exist()

    try:
       with open(FILENAME,"r") as file :
           tasks=file.read().splitlines()       # Read line by line
       return tasks
    
    except Exception as e:                   # Return an empty list on unexpected errors
        print("Error loading task😒: ", e)
        return []


def save_tasks(tasks):

    ensure_folder_and_file_exist() 

    try:
        with open(FILENAME,"w") as file:
            for task in tasks:
                file.write(task+"\n")
    
    except Exception as e:         
        print("\nError Saving task😒: ", e)

def display_tasks(tasks):

    if not tasks:
        print("\nTask list is Empity.🤔")
    else:
        print("\nTo-Do-List:\n")
        for index,task in enumerate(tasks,start=1):
            print(f"{index}. {task}")


def add_task(tasks):
    try:
        new_task =input("Enter the task to add: ").strip()  
        if new_task:        # not empity
            tasks.append(new_task)
            save_tasks(tasks)
            print("\nTask added successfully😊")
        else:
            print("\nTask cannot be empty. Please enter a valid task.")
        
    except Exception as e:
        print("Unable to add task due to error😶", e)

def update_task(tasks):
    try:
        display_tasks(tasks)
        if not tasks:
            return  # Return if no tasks are available

        index = int(input("Enter the task number to update: ")) - 1
        if index < 0 or index >= len(tasks):
            raise IndexError("Invalid task number❌.")

        new_task = input("Enter the new task description: ").strip()
        if new_task:
            tasks[index] = new_task  # Update the task
            save_tasks(tasks)  # Save updated tasks
            print("\nTask updated successfully!😊")
        else:
            print("\nTask description cannot be empty😶.")

    except ValueError:
        print("\nPlease enter a valid number.")
    except IndexError as e:
        print(e)
    except Exception as e:
        print("\nError updating task:", e)


def remove_task(tasks):
    
    try:
        display_tasks(tasks)
        if not tasks:
            return  # Return if no tasks are available

        index = int(input("Enter the task number to remove: ")) - 1
        if index < 0 or index >= len(tasks):
            raise IndexError("\nInvalid task number❌.")

        removed_task = tasks.pop(index)  # Remove the task
        save_tasks(tasks)  # Save updated tasks
        print(f"\nTask '{removed_task}' removed successfully!")

    except ValueError:
        print("\nPlease enter a valid number.")
    except IndexError as e:
        print(e)
    except Exception as e:
        print("\nError removing task:", e)



def show_menu():
    print("\n------ Advanced Calculator ------")
    print("1. Add task ")
    print("2. update task")
    print("3. Remove task")
    print("4. Display task")
    print("5. Exit")
    print("\n---------------------------------")


def main():

    ensure_folder_and_file_exist()

    tasks =load_task()

    while True:

        show_menu()
    
        try:
            choice = int(input("Choose operation (5 to exit): "))

            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                update_task(tasks)
            elif choice == 3:
                remove_task(tasks)
            elif choice == 4:
                display_tasks(tasks)
            elif choice == 5:
                print("\nExiting the To-Do List Application. Goodbye!👋")
                break  # Exit the loop
            else:
                print("\nInvalid choice😤. Please enter a number between 1 and 5.")
        
        except ValueError:
            print("\nPlease Enter a valid number📛. ")

if __name__ == "__main__":
    main()
