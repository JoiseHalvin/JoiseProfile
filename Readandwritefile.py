choice = 0
while choice != 4:
	print("(1) Read the notebook")
	print("(2) Add note")
	print("(3) Empty the notebook")
	print("(4) Quit")

	choice = int(input("Please select one: "))
	if choice == 1:
		file = open("notebook.txt", "r")
		notes = file.read()
		print(notes)
		file.close()
	elif choice == 2:
		file = open("notebook.txt", "a")
		n1 = input("Write a new note: ")
		file.write(n1)
		file.close()
	elif choice == 3:
		file = open("notebook.txt", "w")
		print("Notes deleted.")
		file.close()
	elif choice == 4:
		print("Notebook shutting down, thank you.")
	else:
		print("Incorrect selection.")
