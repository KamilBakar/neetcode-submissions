class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set() # creates an empty set


        for num in nums:            # iterates through the array nums
            if num in my_set:       # conditional statement checking for duplicates in the set
                return True         # if duplicate is found terminates the function

            my_set.add(num)         # if no duplicate is found adds to the set

        return False                # completes the loop
                
                

        
