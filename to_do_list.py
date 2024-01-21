class to_do_list:
	def add (task):
		file = open('todo.txt', 'a')
		file.write(task)
		file.write("\n")
		file.close()

	def show():
		file = open("todo.txt", 'r')
		for task in file:
			print(task)
		file.close()


	def clear():
		with open("todo.txt", 'w'):
			pass


	def delete (index):
		index = int(index)

		with open("todo.txt", 'r') as file:
			tasks = file.readlines()

		del(tasks[index])

		with open("todo.txt", 'w') as file:
			file.writelines(tasks)

	def complete(index):
		index = int(index)
		with open("todo.txt", "r") as file:
			tasks = file.readlines()
			tasks[index] = tasks[index].strip() + " ------ complete\n"
		with open("todo.txt", "w") as file:
			file.writelines(tasks)




	def index():
		with open('todo.txt', 'r') as file:
   			tasks = file.readlines()

		numbered_lines = [f"{i + 1}: {line}" for i, line in enumerate(tasks)]

		with open('todo.txt', 'w') as file:
    			file.writelines(numbered_lines)




def main():
    todo_list = to_do_list()

    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Clear Tasks\n4. Delete Task\n5. Complete Task\n6. Index Tasks\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add(task)
        elif choice == "2":
            print("\nTasks:")
            todo_list.show()
        elif choice == "3":
            todo_list.clear()
            print("Tasks cleared.")
        elif choice == "4":
            index = input("Enter the index of the task to delete: ")
            todo_list.delete(index)
        elif choice == "5":
            index = input("Enter the index of the task to mark as complete: ")
            todo_list.complete(index)
        elif choice == "6":
            todo_list.index()
            print("Tasks indexed.")
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
		



if __name__ == "__main__":
	main()






