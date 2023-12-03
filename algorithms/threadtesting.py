import concurrent.futures


def fun(num, num2):
    if num % num2 == 0:
        return True
    else:
        return False
    

with concurrent.futures.ThreadPoolExecutor() as executor:
    nums = [1,2,3,4,5]
    nums2 = [1,3,5,8,2]
    results = []
    for num in executor.map(fun, nums, nums2):
        results.append(num)

    print(results)