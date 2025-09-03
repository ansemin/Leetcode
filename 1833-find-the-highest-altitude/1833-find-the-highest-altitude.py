class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain=[0]+gain
        max_value=0
        for index in range(len(gain)-1):
            gain[index+1]+=gain[index]
            current_value=gain[index+1]
            # print('current_value {} max value {}'.format(current_value,max_value))
            max_value=max(max_value,current_value)
            # print(max_value)
        return max_value