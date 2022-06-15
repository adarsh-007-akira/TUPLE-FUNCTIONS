#BINARY SEARCH
def binary_search(lst, a, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if lst[mid] == a:
            return mid
        elif lst[mid] < a:
            low = mid + 1
        else:
            high = mid - 1
    return -1
tup=(1, 2, 3, 4, 5, 6, 7)
lst = list(tup)
a = 4
print("The given list is", lst)
print("Element to be found is ", a)
index = binary_search(lst, a, 0, len(lst)-1)
if index != -1:
    print("The Index of the element is " + str(index))
else:
    print("Element Not found")
#LINEAR SEARCH
def linear_search(lst, n, key):  
    for i in range(0, n):  
        if (lst[i] == key):  
            return i  
    return -1  
lst = [1 ,3, 5, 4, 7, 9]  
key = 7  
  
n = len(lst)  
res = linear_search(lst, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)