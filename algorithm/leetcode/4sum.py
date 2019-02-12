 
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        start = 0
        end = len(nums) - 1
        result = set()
        cache = {}
        finalResult = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if cache.get(nums[i]+nums[j]) == None :
                    cache[nums[i]+nums[j]] = [(i, j)]
                else:
                    (cache.get(nums[i]+nums[j])).append((i, j))
        
        while start < len(nums) - 2:
            for second in range(start+1, len(nums)):
                target1 = target - nums[start] - nums[second]
                if cache.get(target1) == None:
                    continue
                else:
                    for tuple in cache.get(target1):
                        temparr = sorted([start, second, tuple[0], tuple[1]])
                        if len(set(temparr)) == 4:
                            temparr = sorted([nums[temparr[0]],nums[temparr[1]],nums[temparr[2]],nums[temparr[3]]])
                            result.add((temparr[0],temparr[1],temparr[2],temparr[3]))
            start+=1
            
        for item in result:
            finalResult.append([item[0],item[1],item[2],item[3]])
             
        return finalResult 
             
         
 
 
 
 
 
print(Solution().fourSum([1,0,-1,0,-2,2], 0))



# arr = [0,1,3,4,5,7,9,10,11]
# start = 0
# end = len(arr) - 1
# target = 12
# result = []
# index = 0
# while start < end:
#     index+=1
#     if (arr[start] + arr[end] > target) :
#         end -= 1
#     elif arr[start] + arr[end] < target :
#         start += 1
#     else:
#         result.append([arr[start],arr[end]])
#         if start+1 < len(arr) and arr[start] == arr[start+1]:
#             start +=1
#         elif end-1 >=0 and arr[end] == arr[end-1]:
#             end-=1
#         else:
#             start +=1
#  
# print(result, index)