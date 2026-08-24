
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

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964 }
thisdict.update({"year":"2000"})
print(thisdict)