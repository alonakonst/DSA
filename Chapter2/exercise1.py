A=[31,41,59,26,41,58]
B=[6,5,4,3,2,1]
def insertion_sort(A):
    for i in range(len(A)):
        j=i
        while j>0 and A[j-1]>A[j]:
            mem=A[j] #how people usually call this variable
            A[j]=A[j-1]
            A[j-1]=mem
            j=j-1


    return A
#print(insertion_sort(A))

def insertion_decreasing(A):
    for i in range(len(A)):
        j=i
        while j>0 and A[j]>A[j-1]:
            mem=A[j]
            A[j]=A[j-1]
            A[j-1]=mem
            j=j-1

    return A
#print(insertion_decreasing(A))

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

def merge_sort(B,i,j):
    if i<j:
        m=(i+j)//2
        merge_sort(B,i,m)
        merge_sort(B,m+1,j)
        merge(B,i,m,j)
        print(B)

merge_sort(B,0,len(B)-1)