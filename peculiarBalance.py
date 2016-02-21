# Peculiar balance
# ================
# Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure – but there’s an obstacle. The door will only open if a challenge is solved correctly. The future of the zombified rabbit population is at stake, so Beta reads the challenge: There is a scale with an object on the left-hand side, whose mass is given in some number of units. Predictably, the task is to balance the two sides. But there is a catch: You only have this peculiar weight set, having masses 1, 3, 9, 27, … units. That is, one for each power of 3. Being a brilliant mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced exactly using this set.
# To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where the weights should be placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.
# The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight, and so on. Each string is one of:

# “L” : put weight on left-hand side
# “R” : put weight on right-hand side
# “-” : do not use weight

# To ensure that the output is the smallest possible, the last element of the list must not be “-“.
# x will always be a positive integer, no larger than 1000000000.

# Test cases
# ==========
# Inputs:
# (int) x = 2
# Output:
# (string list) [“L”, “R”]
# Inputs:
# (int) x = 8
# Output:
# (string list) [“L”, “-“, “R”]

def answer(x):
    return to_balanced(to_ternary(x))

def to_ternary(x):

    res = ""
    while x > 0:
        res = str(x % 3) + res
        x /= 3
    return int(res) 

def to_balanced(t):
   
    res = map(int, str(t))[::-1] 
    for i in range(0, len(res)):
        if res[i] == 2:
            res[i] = -1
            res = increment(res, i + 1)

    return ['-' if x == 0 else ('R' if x == 1 else 'L') for x in res]


def increment(arr, ind):
    """
    calculate the carryover
    """
    if len(arr) == ind:
        arr += [1] 
    elif arr[ind] == -1:
        arr[ind] = 0
    elif arr[ind] == 0:   
        arr[ind] = 1
    elif arr[ind] == 1: 
        arr[ind] = -1
        arr = increment(arr, ind + 1)
    else: # arr[ind] == 2
        arr[ind] = 0
        arr = increment(arr, ind + 1)
    return arr
