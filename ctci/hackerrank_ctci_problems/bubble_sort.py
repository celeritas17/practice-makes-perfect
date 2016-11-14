def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr):
    total_swaps = 0
    for i in range(len(arr)):
        swaps = 0
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                swaps += 1
        total_swaps += swaps
        if swaps == 0:
            break
    return total_swaps

n = int(input().strip())
a = [int(x) for x in input().strip().split(' ')]
total_swaps = bubble_sort(a)

print('Array is sorted in {0:d} swaps.'.format(total_swaps))
print('First Element: {0:d}'.format(a[0]))
print('Last Element: {0:d}'.format(a[len(a) - 1]))