import numpy
import pandas
import csv

def tri_diagonal_matrix_algorithm(A, B):
	N = len(A)
	X = numpy.empty((N, 1), dtype=numpy.float32)
	
	for i in range(N):
		if i == 0:
			B[i] = B[i] / A[i, i]
			A[i, i+1] = A[i, i+1] / A[i, i]
			A[i, i] = 1.0
		elif i == N - 1:
			B[i] = (B[i] - A[i, i-1] * B[i-1]) / (A[i, i] - A[i-1, i] * A[i, i-1])
			A[i, i-1] = 0.0
			A[i, i] = 1.0
		else:
			B[i] = (B[i] - A[i, i-1] * B[i-1]) / (A[i, i] - A[i-1, i] * A[i, i-1])
			A[i, i+1] = A[i, i+1] / (A[i, i] - A[i-1, i] * A[i, i-1])
			A[i, i-1] = 0.0
			A[i, i] = 1.0
	
	for i in reversed(range(N)):
		if i == N - 1:
			X[i] = B[i]
		else:
			X[i] = B[i] - A[i, i+1] * X[i + 1]
	
	return X

def load_matrix(file_name : str):
	matrix = numpy.array(pandas.read_csv(file_name, header=None), dtype=numpy.float32)
	
	return matrix

def print_2d_matrix(matrix):
	rows = len(matrix)
	columns = len(matrix[0, :])
	
	for i in range(rows):
		for j in range(columns):
			print("{:>10.5f} ".format(matrix[i, j]), end="")
		print("")

def main():
	print("Tri-Diagonal Matrix Algorithm")
	print("A X = B")
	print("")
	
	file_name_A = input("file name (A) = ")
	file_name_B = input("file name (B) = ")
	print("")
	
	A = load_matrix(file_name_A)
	B = load_matrix(file_name_B)
	
	print("Input:")
	print("A:")
	print_2d_matrix(A)
	print("B:")
	print_2d_matrix(B)
	print("")
	
	X = tri_diagonal_matrix_algorithm(A, B)
	
	print("Output:")
	print("X:")
	print_2d_matrix(X)

if __name__ == "__main__":
	main()
