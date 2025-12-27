"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Given an interger array, find all unique triplets that sum up to zero = a+b+c=0.
"""

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res: List[List[int]] = []
    n = len(nums)
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left -1]:
                    left +=1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                left += 1
                right -= 1
    return res

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
    nums1 = [-4, -1, -1, 0, 1, 2]
    print(threeSum(nums1))
    nums2 = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums2))