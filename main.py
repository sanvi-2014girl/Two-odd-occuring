def twooodd(arr):
    res = 0
    for i in arr:
        res = res ^ i
        div = res & -res 
        odd1 , odd2 =0,0
        for i in arr:
            if i & div:
                odd1 = odd1 ^ i
            else:
                odd2 = odd2 ^ i
        return odd1,odd2
arr = [1,2,3,2,3,1,5,7]
odd1,odd2 = twooodd(arr)
print(odd1,odd2)