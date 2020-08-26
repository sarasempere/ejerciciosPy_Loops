
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello =[]

for i in my_list:
    data_type = type(i)
    if data_type is dict or data_type is list:
        hello.append(my_list[my_list.index(i)])

print(hello)

