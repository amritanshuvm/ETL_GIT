"""
Docstring for numpy_handson
https://www.youtube.com/watch?v=QUT1VHiLmmI
"""

import numpy as np

a = np.array([1, 3, 6])
b = np.array([4,2,8])
print(a*b)

# 2-d array (list in the list)
c = np.array([[1,3,5,],[7,2,9]])
print("c is a 2-d array =",c)
print("a is a 1-d array =",a)
print("b is a 1-d array =",b)
#get dimension

print("dimension of c is ",c.ndim)
print("dimension of a is ",a.ndim)

# get shape
print("shape of b is ",b.shape)
print("shape of c is ",c.shape)

#get type
print("data type of c is ",c.dtype)
print("data type of a is ",a.dtype)

#Indexing in numpy
new_array = np.array([[1,3,5,7,9,11],[2,4,6,8,10,12]])
print("Consider a numpy 2-d array as:\n",new_array)
print("Size of numpy array in memory:", new_array.itemsize)
print("Total size of numpy array in bytes:", new_array.nbytes)
print("Size of numpy array:", new_array.size)


#Accessing, Changing element rows, columns
print("Accessing, Changing element rows, columns")
new_array = np.array([[1,2,3,4,5,6,7],
                      [8,9,10,11,12,13,14]])
print(new_array)

# Get a specific element 1st row, 4th column 
print(new_array[1,5])
# Get all elements from 2nd row
print("All elements from 2nd row: ",new_array[1:])
# Get all elements from 1st column
print("All elements from 1st column: ",new_array[:1])
#Chnaging value at index (row,cloumn)
new_array[1,5]=20
print(new_array)


# Creating a 3-d array (depth, rows, column)

arr = np.array([
    [[1,  2,  3],
     [4,  5,  6]],

    [[7,  8,  9],
     [10, 11, 12]]
])

print(arr)
print(arr.shape)

arr[0, 0, 1] = 99
print(arr)

# All 0's matrix
print(np.zeros((2,3)))

print("3×4 zeros matrix\n",np.zeros((3,4)))

#All 1's matrix 
print(np.ones((4,2,2)))

#Any other number
print(np.full((2,2),99,dtype='int32'))

#Any other number (full_like)
print(np.full_like(new_array,4))

#Random decimal numbers
"""
Generates floats in [0, 1)
Takes each dimension as a separate argument, not a low/high range
No restriction like low < high
"""

print(np.random.rand(4,2,3))

#Random integer values with all values in matrix less than 7     

print(np.random.randint(4,7,3))
"""
low → minimum value (inclusive)
high → maximum value (exclusive)
size → number of elements (or shape of array)
"""

#Random integer values with all values in matrix ranging from 2 to 9     
print("Random integer values in matrix with values raging from 2 to 9 ")
arr=np.random.randint(2,9, size=(3,3))
print(arr)

print("Random integer values in matrix with values raging from -3 to 6 ")
arr=np.random.randint(-3,6, size=(3,3))
print(arr)

# Identity Matrix -> Square matrix

"""
An identity matrix is a square matrix where:
All diagonal elements = 1
All other elements = 0
It is like the number 1 in matrix math.
"""

print("\n\nThis is a identity square matrix of 5")
print(np.identity(5))

# Diagonal matrix

"""
A diagonal matrix is a square matrix where:
Non-diagonal elements = 0
Diagonal elements can be ANY number
"""

Diagonal_matrix = np.diag([2,5,-1,7,4])
print("\n\nThis is a diagonal matrix:\n",Diagonal_matrix)

# Scalar matrix
"""
A scalar matrix is a special diagonal matrix where:
All diagonal elements are the same number
All non-diagonal elements are 0
"""

# Approach 1 using diagonal matrix:
scalar_matrix = np.diag([7, 7, 7])
print("\n\nThis is a scalar matrix created using diagonal matrix:\n")
print(scalar_matrix)

# Approach 2 using eye:
"""
It is called eye (I) creates because it creates an identity matrix:
Square matrix
1s on the main diagonal
0s everywhere else
"""

scalar_matrix = 5 * np.eye(3)
print("\n\nThis is a scalar matrix using eye:\n")
print(scalar_matrix)

# Repeating the array 3 times
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3, axis= 0)
print(r1)


output=np.ones((5,5))
print(output)
z = np.zeros ((3,3))
z[1,1]=9
print(z)

output[1:4,1:4] = z
print(output)

# Copying the array with using copy()
a=np.array([1,2,3])
b=a
b[0]=200
print(a)  #  Does not retain original value. It's value at [0] also gets updated
print(b)  # Value at b[0] is updated to 200

# Copying the array without using copy()
a=np.array([1,2,3])
b=a.copy()
b[0]=200
print(a)  # Retains original value
print(b)  # Value at b[0] is updated to 20

# Mathematics

a = np.array([1,2,3,4])
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)

b = np.array([1,0,1,0])
print(a * b)

# Trigonometric operations
print(np.sin(a))
print(np.cos(a))

# Linear Algebra
a=np.ones((2,3))   #  It wil create 2 by 3 matrix of all 1's 
print(a)

b=np.full((3,2),2)   # 3 by 2 matrix of value 2.
print(b)

# Matrix multiplication
print(np.matmul(a,b))

#Find determinant of a matrix. linalg stands for linear algebra

input_matrix = np.array([[1,3,5,],
              [7,2,9],
              [4,6,1]])
print("\n\n\nThe 3 X 3 input matrix is: \n", input_matrix)
det = np.linalg.det(input_matrix)
print("The determinant is",det)

identity_matrix=np.identity(5)
print("\n\nThis is a identity square matrix of 5")
print(identity_matrix)
det=np.linalg.det(identity_matrix)
print("It's determinant is:",det)

scalar_matrix = np.diag([7, 7, 7])
print("This is a scalar matrix: \n", scalar_matrix)
det=np.linalg.det(scalar_matrix)
print("The determinant is:",det)

# Statistics

input_matrix = np.array([[13,142,63],[34,-25,89],[7,37,66]])
print(input_matrix)
print(np.min(input_matrix))             # Print minimum number of matrix
print(np.max(input_matrix))             # Print maximum number of matrix
print(np.sum(input_matrix))             # Print sum of all numbers of matrix

# Reorganizing arrays
before = np.array([[1,2,3,4,],[5,6,7,8]])
print(before)
after1=before.reshape((4,2))
print(after1)
after2=before.reshape((8,1))
print(after2)
after3=before.reshape((2,2,2))
print(after3)

# Vertically stacking vectors

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2,v2,v1]))

# Horizonatl stacking vectors

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
c = np.array([[9, 10],
              [11, 12]])

result = np.hstack((a,b,c))
print(result)

# Miscellaneous (Load data from file)

filedata = np.loadtxt('C:/Users/WindowS-10/Desktop/Python_AI_ML/numbers.txt')
print(filedata)

print("######################################################################################################")

filedata = np.genfromtxt('C:/Users/WindowS-10/Desktop/Python_AI_ML/comma_seperated_numbers.txt',delimiter=',')
print(filedata.astype('int32'))

# Boolean Masking and Advanced Indexing

print((filedata > 50 ) & (filedata  < 100))                     # It will show whether true or false
print(filedata[filedata >= 50])              # It will also point out the index

a = np.array([31,46,23,77,18,48,37,99,12])
print(a[[1,2,8]])   # Print value  at first, second and last spot

# Understanding aix in numpy
"""
In NumPy, an axis refers to a dimension along which operations are performed. Think of a NumPy array as a multi-dimensional grid:
1D array: just a list → axis 0 is the only axis.
2D array: like a table → axis 0 is rows, axis 1 is columns.
3D array: like a cube → axis 0, 1, 2 correspond to different directions in the cube.

Key idea:
axis=0 → "go down along rows" (vertical)
axis=1 → "go across columns" (horizontal)

axis 0 → along rows (collapse rows, operate column-wise)
axis 1 → along columns (collapse columns, operate row-wise)
"""

import numpy as np

a = np.array([1, 2, 3, 4])
print(a.sum())        # sum of all elements
print(a.sum(axis=0))  # same thing, axis 0 is the only axis


b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])


"""
axis 0 ↓
1 2 3
4 5 6
7 8 9

axis 1 → 
1 2 3
4 5 6
7 8 9

"""

print("Sum along axis 0:", b.sum(axis=0))  # sum down each column
print("Sum along axis 1:", b.sum(axis=1))  # sum across each row

c = np.array([[[1,2],[3,4]],
              [[5,6],[7,8]]])

"""
Shape: (2, 2, 2) → think of it as 2 matrices of size 2×2.
axis 0 → collapse along first dimension (between the two matrices)
axis 1 → collapse rows inside each matrix
axis 2 → collapse columns inside each row
"""
print("Sum along axis 0:\n", c.sum(axis=0))
print("Sum along axis 1:\n", c.sum(axis=1))
print("Sum along axis 2:\n", c.sum(axis=2))

print("\n\n\n\n#####################################################################\n#####################################################################\n#####################################################################")


"""
Tutorial 4 - Numpy and Inbuilt Functions Tutorial
Krish Naik
Refer Link: https://www.youtube.com/watch?v=vh525RjO6C0&list=PLZoTAELRMXVNUL99R4bDlVYsncUNvwUBB&index=7
"""

my_list=[1,2,3,4,5]
arr=np.array(my_list)
print(arr)
print("Type of array is: ",type(arr))
print("Shape of array is: ",arr.shape)      # Using in-built shape function

# Converting above 1-D array into 2-D array using reshape function

# Creating three lists and will convert it into array
my_list1=[1,2,3,4,5]
my_list2=[2,3,4,5,6]
my_list3=[9,7,6,8,9]

arr=np.array([my_list1,my_list2,my_list3])
print(arr)
print("Shape of array is: ",arr.shape)  
print("This is a 2-d array with 3 rows and 5 columns")

# Reshaping the above array into 5 by 3

reshaped_array=arr.reshape(5,3)   # Using in-built shape function
print("Reshaping above array: \n",reshaped_array) 
print("Shape of array is: ",reshaped_array.shape)  

# Indexing in 2-D array
print("Indexing in 2-D array")
print(arr)
print(arr[0:2,0:2])
print(arr[1:3,3:5])

# Understanding arange function

print(np.arange(2,10))
print(np.arange(2,22,3))
print(np.arange(5,10,0.5))

# Understanding lin space function
"""
np.linspace() creates a NumPy array of evenly spaced numbers between two values, including both ends.
That including both ends part is the key difference from arange.
Number of values (num) = 50 (default)
"""
print(np.linspace(2,10))     # Here NumPy generates 50 evenly spaced numbers between 2 and 10, including both 2 and 10.
print(np.linspace(0, 10, 5))

# Understanding copy function

a = np.array([1, 2, 3])
b = a.copy()                  # real copy

b[0] = 99
print(a)
print(b)

# Using random distribution
arr_ex=np.random.rand(4,4)    # It will create a  5 by 5 matrix with random data with value between 0 and 1 
print(arr_ex)      
import seaborn as sns
import pandas as pd
print(sns.displot(pd.DataFrame(arr_ex.reshape(16,1))))

 # Create an array with 6 random integers between 2 and 20 and then reshape it into 3 by 2 matrix
print(np.random.randint(2,20,6).reshape(3,2))