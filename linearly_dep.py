import numpy as np # imports numpy library

def calculate_linear_dependency(vectors): # defining the formulae

    matrix = np.array(vectors).T # Converts the vectors into matrix and .T does Transpose to convert into columns
    rank = np.linalg.matrix_rank(matrix) # counts the number of linearky independent columns in the matrix
    number_vectors = len(vectors) # counts the number of vectors

    if rank == number_vectors: # if rank and number of taotalvectors are equal then all vectors are linearly independent 
        print("The matix is Linearly independent")
    else:
        print("The matix is Linearly dependent")

#example vector

vectors1 = [         #Linearly dependent vectors
    [1,5,8],
    [2,10,16],
    [4,7,9]
    ]

vectors2 = [         #Linearly independent vectors
    [3,6,4],
    [2,0,1],
    [8,2,6]
    ]

calculate_linear_dependency(vectors1)
calculate_linear_dependency(vectors2)
