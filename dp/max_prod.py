def max_product(arr):

    mx = [0]*len(arr)
    mn = [0]*len(arr)

    mx[0] = arr[0]
    mn[0] = arr[0]

    for i in range(1,len(arr)):
        el = arr[i]
        mx[i] = max(el, el*mn[i-1], el*mx[i-1])
        mn[i] = min(el, el*mn[i-1], el*mx[i-1])
    
    return max(mx)

print(max_product([2,3,-2,4]))