##Create a program that takes in a list of integers as an input, and returns the number of unique elements in the list.
##The program should not use any built-in functions or libraries.

list = [1,1,1,2,2,5,5,5,3,4,9,5,3,6,6,7,3,1,3,8]
f = {"key" : 1}
f["key"] += 1
unique_list = []

for x in list:
    if x not in unique_list:
        unique_list.append(x)

print(f"amount of elements that are unique: {len(unique_list)}")


print(list[3:])

for i in range(len(list)):
    if frequency_of(list[i:]) == 1:
        unique_cnt += 1