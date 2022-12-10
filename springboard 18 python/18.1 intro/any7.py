def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    for num in nums:
        if num == 7:
            return True

    return False


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))


#my solution bc i take things too literally 

def any7(nums):
    if nums == 7:
        print("should be true")
    else:
        print("should be false")
