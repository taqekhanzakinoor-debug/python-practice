fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(fruits[-1])
print(fruits[0:2])
print(len(fruits))
fruits.append("orange")
fruits.insert(1,"grapes")
fruits.extend(["kiwi","peach"])
print(fruits)
fruits[0]="pear"
fruits.remove("banana")
last= fruits.pop()
print(last)
print(fruits)
print("mango" in fruits)
print(fruits.index("mango"))
nums = [30, 10, 20, 10]
print(sorted(nums))
nums.sort(reverse=True)
print(nums)
print(nums.count(10))
print(max(nums), min(nums), sum(nums))
squares = [n * n for n in range(1, 6)]
print(squares)
for fruit in fruits:
    print(fruit)