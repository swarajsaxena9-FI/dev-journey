def two_sum(nums:list[int], target:int)->list[int] | None :
    for i in range(len(nums)):
        for k in range(i+1,len(nums)) :
            if (nums[i]+nums[k])==target:
               return [i,k]
    return None

def test_two_sum():
   assert two_sum([2, 7, 11, 15], 9)==[0, 1]
   assert two_sum([3, 2, 4], 6)==[1, 2]
   assert two_sum([3,3], 6)==[0, 1]
   assert two_sum([0, 4, 3, 0],0)==[0,3]
   assert two_sum([1, 2],10)is None

def two_sum_dict(nums:list[int],target:int)->list[int]|None:
    seen ={}

    for index ,num in enumerate(nums,start=0):
        required =target - num
        if required in seen:
            return [seen[required],index]
        seen[num] =index
    return None

def test_two_sum_dict():
   assert two_sum_dict([2, 7, 11, 15], 9)==[0, 1]
   assert two_sum_dict([3, 2, 4], 6)==[1, 2]
   assert two_sum_dict([3,3], 6)==[0, 1]
   assert two_sum_dict([0, 4, 3, 0],0)==[0,3]
   assert two_sum_dict([1, 2],10)==None

# [1, 2], target 10, expected None
# Zero wala: [0, 4, 3, 0], target 0, expected [0, 3]

