import random
import time

LENGTH = 200

def BubbleSort(nums):
    for i in range(nums.__len__()-1):
        for j in range(i, nums.__len__()-1):
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
    return nums

def FastSort(nums):
    if nums.__len__() == 0:
        return nums
    les = []
    geq = []
    mid = nums[0]
    for i in nums[1:]:
        if i < mid:
            les.append(i)
        else:
            geq.append(i)
    les = FastSort(les)
    geq = FastSort(geq)
    nums = les + [mid] + geq
    return nums

def RandomSort(nums):
    for i in range(nums.__len__() * nums.__len__() * nums.__len__()):
        a1 = random.randint(0, nums.__len__()-1)
        a2 = random.randint(0, nums.__len__()-1)
        if (nums[a1] > nums[a2] and a1 < a2) or (nums[a1] < nums[a2] and a1 > a2):
            tmp = nums[a1]
            nums[a1] = nums[a2]
            nums[a2] = tmp
    return nums

def check(nums):
    for i in range(nums.__len__()-1):
        if nums[i] > nums[i+1]:
            return False
    return True

nums = [i for i in range(LENGTH)]
random.shuffle(nums)
# print(nums)
t1 = time.time()
nums = BubbleSort(nums)
t2 = time.time()
# print(nums)
print("Bubble Sort time :" + str(t2-t1) + "s")
random.shuffle(nums)
# print(nums)
t1 = time.time()
nums = FastSort(nums)
t2 = time.time()
# print(nums)
print("Fast Sort time :" + str(t2-t1) + "s")
random.shuffle(nums)
# print(nums)
t1 = time.time()
nums = RandomSort(nums)
t2 = time.time()
# print(nums)
flag = check(nums)
print("Random Sort time :" + str(t2-t1) + "s, and its answer is " + str(flag))