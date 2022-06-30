from tkinter import Tk, Entry, Button, messagebox, END
from Sudoku import Sudoku
from numpy import zeros

root = Tk()
root.title("Sudoku Solver")
root.geometry("250x250")
matrix = []


def messageBox(title, message, sign):

	if sign == True:
		message = "Successful"
		messagebox.showinfo(title, message)
	elif sign == False:
		message = "No solution  exists!\nMay be you fill wrong in somewhere."
		messagebox.showerror(title, message)

def get_puzzle(obj):

	size = obj.getSize()
	for i in range(size):
		for j in range(size):

			loc = i*(size+1) + j - i
			if matrix[loc].get() == "":
				obj.setCell(i,j,0)

			elif matrix[loc].get() != "":
				if int(matrix[loc].get()) >= 1 and int(matrix[loc].get()) <= size:
					obj.setCell(i,j,int(matrix[loc].get()))

				elif int(matrix[loc].get()) < 1 or int(matrix[loc].get()) > size:
					messageBox("Out of range 1 to 9!", "Vulue out of 1 to 9",False)
					return False
	return True

def answer(obj):

	size = obj.getSize()
	if obj.solveSuduko(0,0) == False:
		messageBox("Sudoku Solver", "False", False)
		return
	else:
		messageBox("Sudoku Solver", "Successful", True)
		i , j = 0, 0
		for cell in matrix:

			if j == size:
				i, j = i+1, 0
			cell.delete("0", END)
			cell.insert("0", obj.getCell(i,j))
			j = j + 1

def solver():

	obj = Sudoku()

	if not(get_puzzle(obj)):
		return
	answer(obj)

def clear():		

	for cell in matrix:
		cell.delete("0", END)

# make screen
for i in range(9):
	for j in range(9):
		cell = Entry(root, width=3)
		cell.grid(row=i, column=j, padx=2, pady=2)
		matrix.append(cell)


solvebtn = Button(root, text="Solve", command=solver)
solvebtn.grid(row=9, column=1, columnspan=3)

clearbtn = Button(root, text="Clear", command=clear)
clearbtn.grid(row=9, column=5, columnspan=3)


root.mainloop()