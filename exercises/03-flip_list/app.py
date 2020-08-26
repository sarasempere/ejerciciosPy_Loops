arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:

new_list = []

for i in arr:
    element = len(arr)-(arr.index(i)+1)
    new_list.append(arr[element])

print(new_list)