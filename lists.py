a = [10,20,30,40,50]

b = [item for item in a if item > 20]
print(b)

c = [10,20,30,56,78]
print(c[1:4])

c1 = [10,20,30,40,50]
for item in c1:
    print(item)

#Replacing Values in python

n = [10,20,30,40,50]
n[2] = 99
print(n)

#mapping method
r = [10,25,35,45,55]
r = list(map(lambda x : 99 if r == 35 else x,r))
print(r)



#inserting into lists

score = [43,57,78,90]
score.insert(0,23)
score.insert(2,67)
print(score)


#insertion in a list Before any Element

list1 = [1,2,4,5,7,8]
element = 13

beforeElement = 5
index =list1.index(beforeElement)

list1.insert(index,element)

#inserting a tuple into the list

list2 = [1,4,5,6,7,8]
num_tuple = (2,3,4,6)
list2.insert(4,num_tuple)
print(list2)

n = 42
res = f"The number is {n}"
print(res)

#s = "the number is %d"
#n =45

c = [1,2,3]
n = [4,5,6]

c.extend(n)
print(c)



d = [2,3,4,5]
e = [7,8,9]

list1[len(d):] = e
print(e)




