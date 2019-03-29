# age = 20
# if age < 18 :
#     print("teen")
# print('baby')

# yob = input('mời bạn nhập số năm tuổi :')
# age = 2019 - int(yob)
# if age <= 10 :
#     print("baby")
# if 10 < age <= 18 :
#     print('teen ')
# if age > 18 :
#     print('adult')

# n = int (input('mời bạn nhập số': ))

# if n>=0:
#     print('gia tri tuyet doi la:',  n)
# elif n == 0:
#     print('n == 0')
# else:
#     print('gia tri tuyet doi la:',  -n)

# yob = input('mời bạn nhập số năm tuổi :')
# age = 2019 - int(yob)
# if age < 10 :
#     print("baby")
# elif  age < 18 :
#     print("teen")
# else: 
#     print("adult")

# range(3)
# for i in [1,2,3,'x']:
#     print('hi',i)
# print('end')

# for i in range(100):
#     if i % 2 == 1:

#         print(i)

# n = int(input("mời nhập số: "))
# s = 0
# for i in range(1,n+1):
#     #  s1=s+i
#     #  s=s1
#     s+=i
# print(s)

# n = int(input("mời nhập số: "))
# s = 1
# for i in range(1,n+1):
#     #  s1=s+i
#     #  s=s1
#     s*=i
# print(s)
# for x in [1, 3, 5, 9] :

    # y = 3*x*x - 2*x + 1
    # print(y)

# for x in range (1,101):
#     for y in range (1,101):
#         for z in range (1,101):
#             if x*y*z == x*x + y*y + z*z:
#                  print(x,'  ', y,'  ',z)

arr = []

def parens(left, right, string):
  
  # if no more brackets can be added then add the final balanced string
  if left == 0 and right == 0:
    arr.append(string)
  
  # if we have a left bracket left we add it
  if left > 0:
   parens(left-1, right+1, string+"(")
  
  # if we have a right bracket left we add it
  if right > 0: 
    parens(left, right-1, string+")")

# the parameters parens(x, y, z) specify:
# x: left brackets to start adding
# y: right brackets we can add only after adding a left bracket
# z: the string so far
parens(3, 0, "")
print arr 




    
    
    



