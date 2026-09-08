
# 1. grade calculator

# scores = [56, 82, 78, 92, 78, 92, 78, 92, 78, 92, 78, 92, 78, 92, 78, 92, 78, 92, 78, 92, 78, 92]

# def gradeCalculator(grade):
#     if grade < 80:
#         print('C')

#     elif 80 <= grade <= 90:
#         print('B')

#     else:
#         print('A')
# 22
# for i in range(len(scores), -1 , -1):
#     grade = scores[i]
    
#     gradeCalculator(grade)

#     print(i)

# # for(let i = scores.length; i >= 0; i--){

# # }
    


# scores = [56, 82, 78, 92, 78, 92, 78, 92, 78, 92, 78, 92, 78, 92, 78, 92, 78, 92, 78]

# def gradeCalculator(gade):
#     if grade > 90:
#         print("a")
#     elif grade > 80:
#         print("b")
#     else:
#         print("c")

# for i in range(len(scores)):
#     grade = scores[i]   
#     gradeCalculator(grade)
#     print(grade)

# Tasteresalt = [90,42,53,50,10,40,50]

# def drivingAllowance(drivingLicenseresalt):
#     if drivingLicenseresalt > 50:
#         print("you can drive")
#     else:
#         print("you can not drive")
# for i in range(len(Tasteresalt)):

#     drivingLicenseresalt = Tasteresalt[i]

#     drivingAllowance(drivingLicenseresalt)


# nums = [1,12,35,3,23,2,13,55,6,4]
# print(nums[0:4])

# thisdict = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964 }
# thisdict.update({"year":"2000"})
# print(thisdict)

# myfamily = {
#     "child1" : { 
#         "age" : "10",
#         "name" : "matt"
#         },
#     "child2" : {
#         "age" : "12",
#         "name" : "nati"
#     }
# }
# print(myfamily["child1"]["age"])



# personalInfo = {
#     "name":"miki",
#     "age" : "15",
#     "school" : "pharo"
# }
# personalInfo.pop("age")
# personalInfo["name"] = "abel"
# print(personalInfo)


# new leetcode problem solution
# class Solution:
#  def leftRightDifference(self, nums: List[int]) -> List[int]:
#     n = len(nums)
#     ans = [0] * n

#     left_sum = 0
#     for i in range(n):
#         ans[i] = left_sum
#         left_sum += nums[i]

#         right_sum = 0
#         for i in range(n - 1, -1, -1):
#             ans[i] = abs(ans[i] - right_sum)
#             right_sum += nums[i]

#         return ans

# Implementing a stack is trivial using a dynamic array

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, n):
#         self.stack.append(n)

#     def pop(self):
#         return self.stack.pop()
# class Car:
#     def __init__(self,model,year,price):
#         self.model = model
#         self.year = year
#         self.price = price
#         car1 = Car("v8","2018","1.9m")
#         print(car1.model)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict1:
                return(dict1[diff], i)
            dict1[nums[i]] = i