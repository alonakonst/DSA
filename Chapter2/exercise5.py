A=[5,2,6,-9,8,9,10,-2]

def two_sum(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if i!=j and A[i]+A[j]==0:
                return True
    return False
print(two_sum(A))

def merge_sort(A,i,j):
    if i<j:
        m=(i+j)//2
        merge_sort(A,i,m)
        merge_sort(A,m+1,j)
        merge(A,i,m,j)

def merge(B,p,q,r):
    L=[]
    R=[]
    #sizes of the left and right lists
    n_left=q-p+1
    n_right=r-q

    #new arrays
    for i in range(n_left):
        L.append(B[p+i])

    for j in range(n_right):
        R.append(B[q + j+1])

    #indeces of smallest elements in left and right
    smallest_l = 0
    smallest_r = 0
    k = p

    while smallest_l<n_left and smallest_r<n_right:
        if L[smallest_l]<=R[smallest_r]:
            B[k]=L[smallest_l]
            smallest_l=smallest_l+1
        else:
            B[k]=R[smallest_r]
            smallest_r=smallest_r+1
        k=k+1

    while smallest_l<n_left:
        B[k]=L[smallest_l]
        smallest_l=smallest_l+1
        k=k+1

    while smallest_r < n_right:
        B[k] = R[smallest_r]
        smallest_r = smallest_r + 1
        k = k + 1


merge_sort(A, 0, len(A) - 1)
print(A)
def two_sum_binary(A):

    for i in range(len(A)-1):
        if binary_search(A,0,len(A)-1,-A[i]):
            return True

    return False
def binary_search(A,left,right,x):
        if left>right:
            return False
        m = (left + right) // 2
        if A[m] == x:
            return True
        elif A[m] < x:
            return binary_search(A, m + 1, right,x)
        else:
            return binary_search(A, left, m-1, x)

print(two_sum_binary(A))
