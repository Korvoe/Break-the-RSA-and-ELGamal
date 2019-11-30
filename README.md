# Break-the-RSA-and-ELGamal
Textbook RSA.
1. Find p and q, two prime factors of n by brute-force, knowing that both are less that square root of n. [+]
2. Calculate Euler totient, which is (p-1) * (q-1) [+]
3. Through extended Euclidean algorithm calculate the inverse of public key e modulo n, which is a private key, d. [+]
4. Find plaintext P = C^d mod n. [+]

ELGamal.
1. Find K. Two approaches:
    Find k, so that c1 = a^k mod q and calculate K = YA^k mod q. [+]
            or
    Find private key Xa so that YA = a^Xa mod q and recover K = c1^Xa mod q. [+]
2. Find inverse of K modulo q, K_inverse. [+]
3. Recover plaintext M = (c2*K_inverse) mod q. [+]
