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

def solver():

	obj = Sudoku()

	for i in range(9):
		for j in range(9):

			if matrix[i*10+j-i].get() == "":
				obj.setCell(i,j,0)

			elif matrix[i*10+j-i].get() != "":
				if int(matrix[i*10+j-i].get()) >=1 and int(matrix[i*10+j-i].get()) <=9:
					obj.setCell(i,j,int(matrix[i*10+j-i].get()))

				elif int(matrix[i*10+j-i].get()) < 1 or int(matrix[i*10+j-i].get()) > 9:
					messageBox("Out of range 1 to 9!", "Vulue out of 1 to 9",False)
					return
	if obj.solveSuduko(0,0) == False:
		messageBox("Sudoku Solver", "False", False)
		return
	messageBox("Sudoku Solver", "Successful", True)
	i , j = 0, 0
	for cell in matrix:

		if j==9:
			i, j = i+1, 0
		cell.delete("0", END)
		cell.insert("0", obj.getCell(i,j))
		j = j + 1

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