A=[
    [3,1,5],
    [2,18,8],
    [1,1,90]
]


def peaks_of_matrix(A):
    max=0

    for row in range(len(A)):
        for column in range(len(A[row])):
            if A[row][column]>max:
                max=A[row][column]
    return(max)

print(peaks_of_matrix(A))