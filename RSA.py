from random import randint
import math

def to_binary(number):
    return bin(number).replace("0b", "")

def square_and_multiply(number, e, n):
    result = number
    root = to_binary(e)
    for i in range(1, len(root)):
        if root[i] == "0":
            result = result*result % n
        else:
            result = (result*result * number) % n
    return result % n

def extended_euclidean_algorithm(m, b):
    (A1, A2, A3) = (1, 0, m)
    (B1, B2, B3) = (0, 1, b)
    while True:
        if B3 ==  0:
            if (B1 < 0):
                B1 = b + B1
            return B1
        elif B3 == 1:
            if (B1 < 0):
                B1 = b + B1
            return B1
        Q = int(A3 / B3)
        (T1, T2, T3) = (int(A1 - Q*B1), int(A2 - Q*B2), int(A3 - Q*B3))
        (A1, A2, A3) = (B1, B2, B3)
        (B1, B2, B3) = (T1, T2, T3)

n = 9943237852845877651
e = 13
C = 1220703125

#For checking
C1 = 528567365900595529
P1 = 8835383948117812667
C2 = 8792215503885098117
P2 = 852845877651
#First step is to find p and q.
#Both cannot be higher than square root on n and must me odd.
root = int(math.sqrt(n)) - 1
p = 0
q = 0
for i in range(root, 0, -2):
    if n % i == 0:
        p = i
        q = int(n / p)
        print("p = " + str(p) + "\nq = " + str(q))
        break

#Second step is to find Euler totient.
phi = (p-1) * (q-1)
print("Euler totient = " + str(phi) + "\n")

#Third step is to find the inverse of e modulo n, which is the private key.
d = extended_euclidean_algorithm(e, phi)
print("Private key = " + str(d) + "\n")

#Fourth step is to check if found private key is the correct one.
if P1 == square_and_multiply(C1, d, n):
    print("1st example answer is: " + str(square_and_multiply(C1, d, n)))
    print("1st example solved correctly.")
if P2 == square_and_multiply(C2, d, n):
    print("2nd example answer is: " + str(square_and_multiply(C2, d, n)))
    print("1st example solved correctly.")

#Last step is to find the plaintext, that we need.
P = square_and_multiply(C, d, n)
print("The answer is: " + str(P))
