a =5
b = 4.75
c= "Python"
d=False
f =None
print(type(a),type(b),type(c),type(d),type(f))#printed the data types of the variables and in a row

age=int(input("Enter your age: "))
print(age +10)
print(float(age))
print(int(7.9))# 
print(20// 6, 20 % 6, 3 ** 4)
print(8>5,8 ==5)
print(True and False, True or False, not False)
print(4 in[1, 2, 3, 4])
x=[5, 6]
y=x
print(x is y, x==[5, 6])
marks = int(input("Enter marks: "))
if marks>=85:
    print("Grade A")
elif marks>= 5:
    print("Pass")
else:
    print("Fail")
for i in range(1, 8, 2):
    if i==5:
        continue
    print(i)
