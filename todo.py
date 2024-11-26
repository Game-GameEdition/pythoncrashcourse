with open("todos.txt", "r") as f:
    content = f.read()
    my_list = content.split("\n")
    print(f"Current todos: {my_list}")

user_active = True
completed_tasks = []
tobe_tasks = []

for task in my_list:
    user_input = input(f"Did you complete: {task} ? (y/n/skip)")
    cleaned_user = user_input.lower().strip()
    if cleaned_user == "y":
            completed_tasks.append(task)
    elif cleaned_user == "n":
        pass
    elif cleaned_user == "skip":
        break
    else:
        print("inputs 'y','n' accepted ONLY.")

for completed_task in completed_tasks:
    if completed_task in my_list:
        my_list.remove(completed_task)

while user_active:
    tobe_task = input("Add another task or quit with q: ")
    if tobe_task == "q":
        print("Okay. Saving new tasks to file.")
        user_active = False
        break
    else:
        tobe_tasks.append(tobe_task)
        continue

for tobe_task in tobe_tasks:
    my_list.append(tobe_task)

with open("todos.txt", "w") as f:
    output = "\n".join(my_list)
    f.write(output)