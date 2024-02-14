'''
Find Peaks Let A = [2, 3, 3, 7, 3, 11, 1, 5, 7, 10] be an array. Solve the following exercises
'''

A = [2, 1, 3, 7, 3, 11, 1, 5, 7, 10]
peaks=[]

#Specify all peaks in A: peak element if it's not smaller than its neighbors
#Method 1: linear search

for i in range(len(A)):
    if i == 0:
        if A[i]>A[i+1]:
            peaks.append(A[i])
    elif i ==len(A)-1:
        if A[i]>A[i-1]:
                peaks.append(A[i])
    else:
        if A[i]>A[i-1] and A[i]>A[i+1]:
            peaks.append(A[i])

print(f'method 1 peaks: {peaks}')

#Method 2: modified binary search 'Divide and Conquer':
def find_peak(A):
    left = 0
    right = len(A)-1
    while left<right:
        mid = left+(right-left)//2
        if A[mid]>A[mid+1]:
            right=mid
        else:
            left=mid+1
        return A[left]

print("method 2 peaks:", find_peak(A))

def find_peaks(num, peaks_2):
    n = len(num)
    if n == 0:
        return
    elif n == 1:
        peaks_2.append(num[0])
        return
    elif n == 2:
        peaks_2.append(max(num))
        return

    mid = (n // 2)-1
    if num[mid] >= num[mid - 1] and num[mid] >= num[mid + 1]:
        peaks_2.append(num[mid])
    find_peaks(num[:mid], peaks_2)
    find_peaks(num[mid+1:], peaks_2)

peaks_2 = []
find_peaks(A, peaks_2)
print("method 3 peaks:", peaks_2)

def second_linear_method(A):
    max=0
    for i in range(len(A)-1):
        if (A[i] >= A[max]):
           max=i
    return A[max]

print("Second linear method:", second_linear_method(A))

#list(map(int,input().split()))