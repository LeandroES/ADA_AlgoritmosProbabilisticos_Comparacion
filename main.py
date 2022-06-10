# Python3 code to implement Freivald’s Algorithm
import random

N = 2


# Function to check if ABx = Cx
def freivald(a, b, c):
    # Generate a random vector
    r = [0] * N

    for i in range(0, N):
        r[i] = (int)(random.randrange(509090009) % 2)

    # Now compute B*r for evaluating
    # expression A * (B*r) - (C*r)
    br = [0] * N

    for i in range(0, N):
        for j in range(0, N):
            br[i] = br[i] + b[i][j] * r[j]

    # Now compute C*r for evaluating
    # expression A * (B*r) - (C*r)
    cr = [0] * N
    for i in range(0, N):
        for j in range(0, N):
            cr[i] = cr[i] + c[i][j] * r[j]

    # Now compute A* (B*r) for evaluating
    # expression A * (B*r) - (C*r)
    axbr = [0] * N
    for i in range(0, N):
        for j in range(0, N):
            axbr[i] = axbr[i] + a[i][j] * br[j]

    # Finally check if value of expression
    # A * (B*r) - (C*r) is 0 or not
    for i in range(0, N):
        if (axbr[i] - cr[i] != 0):
            return False

    return True


# Runs k iterations Freivald. The value
# of k determines accuracy. Higher value
# means higher accuracy.
def isProduct(a, b, c, k):
    for i in range(0, k):
        if (freivald(a, b, c) == False):
            return False
    return True


# Driver code
a = [[1, 1], [1, 1]]
b = [[1, 1], [1, 1]]
c = [[2, 2], [2, 2]]
k = 2

if (isProduct(a, b, c, k)):
    print("Yes")
else:
    print("No")