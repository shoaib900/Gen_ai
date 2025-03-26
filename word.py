# 01 - display the result to output
# print("hello world")
# print(34)
# print(True)
# print(type("hello world 56"))

# 02 - legal name of variables

# name = "Khurram"
# firstName = "ali" # camel case;
# FirstName = "aslam" # pascal case;
# first_name = "ali" # snake case;
# name1st = "alia" # number case; case sensitive;


# 03 - type of variables;

# print(type(23))
# print(type(True))
# print(type("34"))

# 04 data types in python

# a = "string"
# b = True
# c = 34
# d = 34.5
# e = 1j
# f = ["aslam","amna","mehmona"] 
# g = ("hello","world","!")
# h = {"name":"umar","age":23}
# i = b"hello world"
# j = {"hi","many","fight"}

# 05 math operation

# a = 4
# b = 2
# sum =  a + b 
# print(sum , type(sum))
# print(a ** b)

# 06 input type 

# a = input("Enter you name : ")
# print(a,type(a))

# 07 if conditions 

# num = 101
# if (num >= 45 and num <= 50 ) :
#     print("you are passed")
# elif (num >= 90 and num > 101) :
#     print("you are passed Grad A")
# else :
#     print("you are not passsed")

# num = 20
# num2 = 60
# if num == 20:

#     if num2 == 40:
#         print("you got both right")
#     elif num2 == 60:
#         print("hurrey you got it")
#     else :
#         print("you have wrong")
# else:
#    print( "you got both wrong")

# marks = 90
# if marks > 80:
#     print("passed")
# elif marks > 85:
#     print("passed Grade a")

# 08 typ casting

# num = "45"
# num = int(num)
# print(type(num))

# num2 = 45
# num2 = str(num2)
# print(type(num2))

# num3 = "43.0"
# num3 = float(num3)
# print(type(num3))

# val = input("Enter your age in number : ")
# val1 = int(val)
# print(type(val1) , type(val))


# 01 Assignment solution

# edu = int(input("Enter you education : "))
# age = int(input("Enter you age : "))
# height = float(input("Enter you height : "))

# if( edu >= 12 and (age <= 32 and age >= 18)):
#     print("Passed")
# elif( (age <= 32 and age >= 18) and height >= 5.6 ) :
#     print("Passed")
# elif(  height >= 5.6 and edu >= 12 ) :
#     print("Passed")
# else:
#     print("Failed")

# 09  multiline string

# b = """hello world how are
#  you;"""
# print(b)

# c = """hello world"""
# print(type(c), len(c))

# 10 concatenation 

# a = "hello"
# b = "World"
# print(a + " " + b)

# a = 42
# b = 43
# c = "hello world!"
# print( str(a) + b + " " + c)


# 11  format in string and integers / float
# marks = 45
# total = " your total marks is 100 and you got {}"
# obt = total.format(marks)
# print(obt)

# age = 24
# total = 100
# obt = 90
# res = " your age is {0} and your total marks {2} and obtain marks {1}"
# tot = res.format(age,obt,total)
# print(tot)


# 12 string slicing

# a = "hello world!"
# print(a[-3:-1])
# print(a[0:])
# print(a[:5])

# 13  split in string

# a = "hello AI class"
# b = a.split(" ")
# print(a, b)

# 14  uppar case lower case in string

# st = "Hello World!"
# up = st.upper()
# lo = st.lower()
# print(up, lo) 
# print( st.upper(), st.lower())
# st = "hello world"
# print(st.capitalize(),st.title())

# a = "hello"
# b = "world"
# print( a.capitalize() + " " + b.capitalize())

# 02 assignment solution 

# a = "jaranwala faisalabad lahore"
# print( a[0:1].upper() + a[1:9] , a[10:11].upper() + a[11:20] , a[21:22].upper() + a[22:]   )


# 15 replace methods 
# a = "hello"
# b = a.replace("h","H")
# print(b)

# 03 assignment home 

st = "Jaranwala Faisalabad Lahore Karachi Multan" # don't use the slice method and replace first letters in small;


# 15 lists  

 # ls = list(("Lahore","Faisalabad","Jaranwala")) # constructor method

# ls= []
# ls = [ "Lahore","Faisalabad","Jaranwala"]
# print(type(ls), ls)
# print(type(ls), ls)

# ls = ["Lahore","Faisalabad","Jaranwala"]

# print(ls[2:])

# ls[1] = "Multan"
# ls[0:1] = [ "Karachi"]
# ls[2:] = ["Multan"]
# ls[1:2] = ["Peshawar"]
# ls[0:] = ["Lahore","Faislabad","Jaranwala","Peshawar"]
# print(ls)

# ls = ["Lahore","Faisalabad","Jaranwala"]
# ls.append("Peshawar")
# ls.insert(2,"Peshawar")
# ls.pop(0)
# ls.remove("Faisalabad")
# del ls

# ls.clear()
# print(ls)

# 16 for loops 

# ls = ["apple","banana","mango", "orange"]

# print(ls)
# for item in ls:
#     print(item)

# Assignments class 19/ 03/ 2025:______________________

# ls = ["lahore","faisalabad","jaranwala"]
# lp=[]
# for x in ls:
#     p = x[0:1].upper() + x[1:-1].lower() + x[-1:].upper()
#     lp.append(p)
#     print(p)
# print(lp)

# ls = [ "lahore","Faisalabad","jaranwala"]
# lp = []
# for x in ls:
#     lp.insert(0,x)
# print(lp)



# ls1 = ["Faisalabad","jaranwala"]
# ls2 = ["Lahore"]
# ls1.extend(ls2)
# print(ls1)

# for i in range(1,10):
#     print("Pakistan Zindabad: " + str(i))

# ls = [1,2,3,4,5,6,7,8,9,10]
# ls2 = []
# for i in ls:
#     if i % 2 == 0:
#         ls2.append(i)
#         print(i)
# print(ls2)

# i = 0
# while i < len(ls):
#       print(ls[i])
#       i= i + 1

# ls = ["Lahore","Jaranwala"]
# n = input("Enter your city : ")
# city_found = False
# for x in ls:
#     if n == x:
#         city_found = True

# if city_found:
#     print("your city is neat and clean now.")
# else:
#     print("your city is not neat and clean now")

# ls = ["Lahore","Jaranwala"]
# [print(x) for x in ls]

# ls = ["Lahore","Jaranwala"]
# ip = input("Enter your city :")
# ls2 = [x for x in ls if ip==x]
# print(ls2)

# ls1 = [1,2,3,4,5,6,7,8,9,10]
# ls2 = [x for x in ls1 if x %2 == 0]
# print(ls2)

# ls1 = ["Lahore","Jaranwala","Faisalabad","Jaranwala"]
# ls2 = [x if x!= "Jaranwala" else "144GB" for x in ls1 ]
# print(ls2)


# 17  for loop while loop

# ls = [ "Karachi", "Jaranwala", "Faisalabad"]

# for x in range(len(ls)):
#     print(ls[x], x +1)

# i = 0
# while i < len(ls):
#     print(ls[i])
#     i= i + 1

# 18 range 

# for x in range(2,21,2):
#     print(x)

# 19 list comprensions 

# ls = [x for x in range(2,10,2)]
# print(ls)

# ls = ["Karachi","Jaranwala","Faisalabad","kivi","test"]
# [print(x) for x in ls if "i" in x ]

# for x in ls:
#     if "a" in x:
#         ls2.append(x)

# ls = ["karachi","jaranwala","faisalabad","kivi","test"]

# ls2 = [x for x in ls if x != "Karachi"]
# ls2 = [x.capitalize() for x in ls ]
# ls2 = [x[0].upper()+x[1:-1].lower()+x[-1:].upper() for x in ls]
# ls2 = [x[0].upper() for x in ls if "F" in x]
# print(ls2)

# inp = int(input("Enter the number: "))
# val = 1

# for i in range(2,inp + 1):
#     val *= i
#     print(val)


# count = 0
# for i in range(1,101):
#     if ("3" or "33") in str(i):
#             count += 1
# print(count)


# 20 tuples 

# tup = ("hello",)

# tp = tuple(("hello",))

# ls = list((tp))

# ls.append("guru99")
# print(ls)
# tup = tuple((ls))
# print(tup)




# print(type(tp))

# del tup

# print(tup)

# print(type(tup))
# print(type(tup))
# print(tup[1])
# print(tup[0:-1])

# tup1 = ("tup 1",)
# tup2 = ("tup 2",)

# tup3 = tup1 + tup2
# print(tup3)

# tup1 = ("faisalabad","Jaranwala","Lahore")
# tup2 = (1,2,3,4,5,6,7)
# tup3 = tup2 + tup1

# print(tup3[7:] + tup3[:7])
# ls = list(tup3)
# ls2 =[]
# for i in  ls:
#     ls2.insert(0, i)
# tup4 = tuple(ls2)
# print(tup4)
# print(ls)

# tup = ("semester","annual","master","M phil","P hd")
# (tup1,tup2,*tup3) = tup
# print(tup2)

# 21 sets   ---------------------------------------

# st = {"hello","world","!"}
# st = set((False,True,"hello","world","!",0,1,"yes","no"))
# st2 = set(("philospher","hell menu"))

# st.add("philospher")
# st.update(st2)
# st.pop()

# print(type(st))

# st = {"hello","world","!",'hello world'}
# st.discard("hello")
# st.discard("hello")
# st.clear()
# del st[0]



# st1 = {"hello","world","!"}
# st2 = {"menu","food","world"}

# st3 = st1 | st2
# st3 = st1.union(st2)

# st3 = st1.intersection(st2)
# st3 = st1 & st2

# st3 = st1.difference(st2)
# st3 = st1 - st2
# print(st3)


# 22 dictionaries --------------------------------

# dic = {"name":"amna"}  
# dic = dict({"name":"amna","age": 20})


# print(type(dic),dic, len(dic))
# print(dic["name"])
# print(dic.get("name"))
# dic["color"] = "fade"
# dic.update({"color":"white","alpha":"1.09"})
# dic.pop("color")
# dic.popitem()
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# del dic["name"]
# dic.clear()
# del dic 
# print(dic) 

# 23 pass by reference / pass by value ----------------------

# a = 10
# b = a
# a = 20
# print(a,b)

# dic1 = {"name":"amna","age":20}
# dic2 = dic1

# dic1["name"] = "adil"

# print(dic1,dic2) 

# 24 copy dictionary --------------------------------

# dic1 = {"name":"adil","age":24}

# dic2 = dic1.copy()
# dic2 = {"name":"adil","age":24}
# dic2 = dict(dic1)
# dic1["name"] = "amna"
# print(dic1,dic2)






















