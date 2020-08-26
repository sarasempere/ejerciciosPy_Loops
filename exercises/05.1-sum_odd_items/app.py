arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumOdds(arr):
    arr_odds=0
    for i in arr:
        if i%2!=0:
            arr_odds= arr_odds + i
    return arr_odds
            
print(sumOdds(arr))