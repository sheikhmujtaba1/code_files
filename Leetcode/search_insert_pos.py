def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l= m+1
            else:
                r = m-1
        return l

def main():
    nums = [1,3,5,6]
    target= 5
    print(searchInsert(nums, target))


if __name__ == "__main__":
    main()
