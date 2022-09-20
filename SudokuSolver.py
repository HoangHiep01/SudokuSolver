from tkinter import Tk, Entry, Button, messagebox, END, LabelFrame
from Sudoku import Sudoku
from numpy import zeros

root = Tk()
root.title("Sudoku Solver")
root.geometry("300x300")
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
frame1 = LabelFrame(root)
frame1.grid(row=0, column=0, padx=5, pady=5)

frame2 = LabelFrame(root)
frame2.grid(row=0, column=1, padx=5, pady=5)

frame3 = LabelFrame(root)
frame3.grid(row=0, column=2, padx=5, pady=5)

frame4 = LabelFrame(root)
frame4.grid(row=1, column=0, padx=5, pady=5)

frame5 = LabelFrame(root)
frame5.grid(row=1, column=1, padx=1, pady=1)

frame6 = LabelFrame(root)
frame6.grid(row=1, column=2, padx=1, pady=1)

frame7 = LabelFrame(root)
frame7.grid(row=2, column=0, padx=1, pady=1)

frame8 = LabelFrame(root)
frame8.grid(row=2, column=1, padx=1, pady=1)

frame9 = LabelFrame(root)
frame9.grid(row=2, column=2, padx=1, pady=1)

for i in range(9):
	for j in range(9):
		if i < 3:
			if j < 3:
				cell = Entry(frame1, width=3)
			elif j < 6:
				cell = Entry(frame2, width=3)
			else:
				cell = Entry(frame3, width=3)
		elif i < 6:
			if j < 3:
				cell = Entry(frame4, width=3)
			elif j < 6:
				cell = Entry(frame5, width=3)
			else:
				cell = Entry(frame6, width=3)
		else:
			if j < 3:
				cell = Entry(frame7, width=3)
			elif j < 6:
				cell = Entry(frame8, width=3)
			else:
				cell = Entry(frame9, width=3)

		cell.grid(row=i%3, column=j%3, padx=2, pady=2)
		matrix.append(cell)


solvebtn = Button(root, text="Solve", command=solver)
solvebtn.grid(row=9, column=0, columnspan=1)

clearbtn = Button(root, text="Clear", command=clear)
clearbtn.grid(row=9, column=2, columnspan=1)


root.mainloop()