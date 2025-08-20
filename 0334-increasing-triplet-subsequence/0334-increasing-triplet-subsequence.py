class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # [1,0,3,0,5]
        first_num,second_num, third_num=max(nums),0,0
        i=0
        while i <len(nums)-2: # 0 1 2  
            if first_num>nums[i]: 
                first_num=nums[i]
                """ 
                i=0, 1>1, F
                i=1, 1>0, T, fn=0
                i=2, 0>3, F, fn=0
                    
                """
            if first_num<nums[i+1]: 
                second_num=nums[i+1]
            """
            i=0, 1<0, F
            i=1, 0<3, fn=0, sn=3
            i=2, 0<0, fn=0, sn=3
                 
            """
            if second_num<nums[i+2]:
                third_num=nums[i+2]
            """
            i=0, 1<0, F
            i=1, 3<0, F
            i=2, 3<5, T, fn=0, sn=3, tn=5

            """
            if first_num<second_num<third_num:
                print(f'{first_num}-{second_num}-{third_num}')
                return True 
            i+=1
        return False




                    
