class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output=[]
        for i in range(len(candies)):
          max_value=candies[i]+extraCandies
          candy_max=max(candies)
          if max_value>=candy_max:
            output.append(True)
          else:
            output.append(False)
        return output 