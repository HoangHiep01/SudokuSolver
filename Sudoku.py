from numpy import zeros

class Sudoku():

	def __init__(self):
		self.size = 9
		self.matrix = zeros(shape=(9,9), dtype="int")

	def isValid(self, row, col, num):
		# Kiểm tra trong dòng có số trùng với num không
	    # Nếu có thì return false
		for x in range(9):
			if self.matrix[row][x] == num:
				return False
	 
	    # Kiểm tra trong cột có số trùng với num không
	    # Nếu có thì return false
		for x in range(9):
			if self.matrix[x][col] == num:
				return False
	 
	    # Kiểm tra trong ma trận nhỏ 3x3
	    # Xem có số trùng với num không
	    # Nếu có thì return false
		startRow = row - row % 3
		startCol = col - col % 3
		for i in range(3):
			for j in range(3):
				if self.matrix[i + startRow][j + startCol] == num:
					return False
		return True # Khi tất cả điều kiện False không sảy ra

	def solveSuduko(self, row, col):

	    # Khi tới ô cuối cùng có tọa đọ logic là grid[8][8]
	    # Hàm mới được gọi với tọa độ logic là row = 8, col = 9
	    # Đây là khi ta hoành thành tính toán
	    # Nó chính là điều kiện kết thúc đệ quy
	    if (row == self.size - 1 and col == self.size):
	        return True
	       
	    # Khi row có giá trị thuộc khoảng từ [0,7]
	    # Mà col có giá trị là 9
	    # Thì lúc này ta đã xét hết hàng cần thực hiện việc xuống hàng mới
	    # row tăng 1 và col xét là từ đầu
	    if col == self.size:
	        row += 1
	        col = 0
	 
	    # Kiểm tra ô hiện tại
	    # Nếu có giá trị lên hơn 0, tức là ô có giá trị cho trước
	    # Thì thực hiện chuyển sang ô kế tiếp
	    if self.matrix[row][col] > 0:
	        return self.solveSuduko(row, col + 1)
	    for num in range(1, self.size + 1, 1):
	       
	        # Kiểm tra giá trị có thể điền
	        # Giá trị nằm trong khoảng từ 1 đền 9
	        # Sau khi điền thì ta tới ô tiếp theo
	        if self.isValid(row, col, num):
	           
	            # Coi giá trị vượt qua điều kiện hàm isSafe là đúng
	            # Và điền vào ô trống
	            self.matrix[row][col] = num
	 
	            # Kiểm tra tra ô tiếp theo
	            # Công việc này được lặp cho ô đó
	            # Trả về True khi xác nhận ô sau đó đã đúng
	            # Giá trị của True sẽ được trả khi đã giải ra Sudoku
	            if self.solveSuduko(row, col + 1):
	                return True
	 
	        # Khi giả định coi giá trị vượt qua isSafe là đúng đã sai
	        # Thử ta thử giả định giá trị tiếp theo
	        # Khi giá trị giả định tới 9
	        # Ta sẽ quay lại ô trước đó
	        # Và làm việc từ dòng 95 đã nói
	        self.matrix[row][col] = 0
	    # Khi ô tính toán đầu tiên trả về False
	    # Thì bài toán không có lời giải
	    return False

	def display(self):
		for i in range(self.size):
			for j in range(self.size):
				print (self.matrix[i][j], end=" ")
			print()

	def setCell(self, row ,column, num):
		self.matrix[row][column] = num

	def getCell(self, row ,column):
		return self.matrix[row][column]