'''
# 剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
'''

class Solution(object):
    def minArray(self, numbers) -> int:
        low = 0
        high = len(numbers)-1

        while low < high:
            mid = low + (high - low) // 2
            print(numbers[low: high+1])
            print('low={},mid={},high={}'.format(numbers[low],numbers[mid],numbers[high]))
            if numbers[mid] > numbers[high]:
                low = mid + 1
            elif numbers[mid] < numbers[high]:
                high = mid
            else:
                high = high - 1
        return numbers[high]

def er(nums, num):
    low = 0
    high = len(nums)-1
    while low < high:
        mid = low + (high - low) // 2
        print(nums[mid])
        if nums[mid] > num:
            high = mid
        elif nums[mid] < num:
            low = mid + 1
        else:
            low = high
    return mid


if __name__ == '__main__':
    # r = Solution()
    # print(r.minArray([3, 4,4, 5, 5, 0,1, 2, 3]))
    print(er([1, 2, 3, 4, 5, 6, 7], 1))
