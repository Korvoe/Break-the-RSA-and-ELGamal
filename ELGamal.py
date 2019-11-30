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

q  = 2934201397
a  = 37
YA = 2174919958
c1 = 2909170161
c2 = 2565161545

#For checking
P1  = 189465461
c11 = 2909170161
c12 = 1004005362
P2  = 848963461
c21 = 2909170161
c22 = 2081016632

#One way to find K.
#Find k.
print("First way:")
for i in range(1, q-1):
    if c1 == square_and_multiply(a, i, q):
        k = i
        print("k is: " + str(k))
        break

#Calculate K.
K = square_and_multiply(YA, k, q)
print("K is: " + str(K))

#Another way to find K.
#Find private key of A.
print("Second way:")
for i in range(1, q-1):
    if YA == square_and_multiply(a, i, q):
        Xa = i
        print("Private key is: " + str(Xa))
        break

#Recover K.
K = square_and_multiply(c1, Xa, q)
print("K is: " + str(K) + "\n")

#Find inverse of K modulo q.
K_inverse = extended_euclidean_algorithm(K, q)
print("Modular inverse of K is: " + str(K_inverse) + "\n")

#Check if correct, finding plaintexts of first and second examples.
M1 = (square_and_multiply(c12, 1, q) * square_and_multiply(K_inverse, 1, q)) % q
if M1 == P1:
    print("1st example answer is: " + str(M1))
    print("1st example solved correctly.")
M2 = (square_and_multiply(c22, 1, q) * square_and_multiply(K_inverse, 1, q)) % q
if M2 == P2:
    print("2nd example answer is: " + str(M2))
    print("2nd example solved correctly.")

#Recover M.
M = (square_and_multiply(c2, 1, q) * square_and_multiply(K_inverse, 1, q)) % q
print("The answer is: " + str(M))
