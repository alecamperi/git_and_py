def shellSort(arr):
 
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = round(n/2)
    print(type(gap))
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
        gap = int(gap)
        for i in range(gap,n):
 
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
 
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap and arr[j-gap] >temp:
                print(j, gap,arr[j-gap], temp)
                arr[j] = arr[j-gap]
                j -= gap
 
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        # Le divide a gap en 2
        gap /= 2
 
 
# Driver code to test above
arr = [20, 30, 4, 8, 11, 14]
 
# n = len(arr)
# print ("Array before sorting:")
# for i in range(n):
#     print(arr[i]),
 
shellSort(arr)
 
# print ("\nArray after sorting:")
# for i in range(n):
#     print(arr[i]),
