theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

new_list = list(map(lambda x: "woko" if x==0 else "wiki", theBools))

print(new_list)
