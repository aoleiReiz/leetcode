def mergeSort(array):
    # Write your code here.
    def merge_sort(a, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        merge(a, left, right, mid)

    def merge(a, left, right, mid):
        aux = a[left: right + 1][:]
        k = left
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if aux[i - left] <= aux[j - left]:
                a[k] = aux[i - left]
                i += 1
            elif aux[i - left] > aux[j - left]:
                a[k] = aux[j - left]
                j += 1
            k += 1
        while i <= mid:
            a[k] = aux[i - left]
            i += 1
            k += 1
        while j <= right:
            a[k] = aux[j - left]
            j += 1
            k += 1

    if len(array) <= 1:
        return array
    merge_sort(array, 0, len(array) - 1)
    return array


arr = [ 1, -3, 2, 5, 9, 4, 3, 2]
print(mergeSort(arr))