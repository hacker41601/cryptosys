#Author: Nich Kiem
#Purpose: RSA Cryptosystem
import math
import random

def miller_rabin(n, k): #most of my variable names are straightforward, I will be putting notes onto the ones that may not be so obvious to both the grader and myself
    numIter = 0
    evenNum = n - 1 #since miller-rabin only uses odd integers n>=3
    while evenNum % 2 == 0:
        evenNum //= 2
        numIter += 1
    #assert(2**numIter * evenNum == n-1) #assert means 2^numIter * evenNum MUST equal n-1

    #this is where we check run the numbers through and check
    #pow(x, to the power of y, mod z)
    #if x = 1 or x = n - 1 then keep looping
    #maybe use another while loop for coherence
    #def millerWitness(tester) #tester is just the name of the random number being generated to be tested against the miller witness to determine if it is composite or prime
    for i in range(k):
        #pick random test^ ((2^i)*evenNum) mod n
        tester = random.randrange(2, n-1)
        res = mod_exp(tester, evenNum, n) 
        if res == 1 or res == n-1:
            continue

        for i in range(numIter - 1): #in range of the max number of iterations
            res = mod_exp(tester, 2, n)
            if res == n-1:
                break
        else:
            return False #composite
    return True


#This is a list of primes from range 0-420(lol) instead of writing code to produce the sieve of erasthothense like in cs315
#This is pulled from an online generator of primes
prime_divisors = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419]

def primeCheck(n):
    while True:
        #This is a random numbers in the range 2^(n-1)+1 to 2^n -1
        primeNum = random.randrange(n, 10**n-1)
        for div in prime_divisors:
            if primeNum % div == 0 and div**2 <= primeNum:
                break
        else:
            return primeNum

def rsaMod(p, q):
    n = p*q
    return n

def totient(p, q):
    r = (p-1)*(q-1)
    return r

def gcd_e(e,r):
    while (r != 0):
        e,r = r,e%r
    return e

def eea(e, r):
    x = 1
    y = 0
    z = r

    if (r == 1):
        return 0
    while (e > 1):
        div = e//r
        rem = r #rem is the remainder
        #keep going like regular euclid
        r = e%r
        e = rem
        rem = y
        #continuously update x and y
        y = x-div*y
        x = rem
    if (x < 0):
        x = x+z
    return x

def mod_exp(x,y,z):
    ans = 1
    x = x%z
    while (y > 0):
        if (y&1): #if y is odd
            ans = (ans*x)%z
        y = y >> 1
        x = (x*x)%z
    return ans

def encrypt(m, e, n): #An attempt was made to read the file line by line and convert to integer but they were lists and I could not figure out how to convert the list into an integer for both encrypt and decrypt
    #with open("cipherText.txt", "r") as f:
    #n = f.readline(1)
    #e = f.readline(2)
    #f.close()
    #n = int(e)
    #e = int(e)
    cipherText = mod_exp(m,e, n)
    return cipherText

#Decrypt
#The message needs to be output to a file named decrypt_message.txt
def decrypt(cipherText, d, n):
    #with open("decrypted_message.txt", "r") as f:
    #d =  f.readline(1)
    #f.close()
    #d = int(d)
    plainText = mod_exp(cipherText, d, n)
    return plainText

def p_and_q(size):

    prime_cand = random.randrange(size, 10**size-1)
    while not miller_rabin(prime_cand, 100):
        prime_cand = random.randrange(size, 10**size-1)
    return prime_cand

def main():
    print("!!!Welcome to Nich's RSA Encryptor/Decryptor!!!\n")

    p = 0
    q = 0

    while (p-q) < (10^95):
        bits = 10^99
        p = p_and_q(10^99)
        q = p_and_q(10^99)
            #This is where p and q are referenced so be sure to do all the encrypting and decrypting under this comment
    print(p, "is p\n and \n", q, "is q\n")
    print("The totient is: ")
    r = totient(p,q)
    print(r)
    print("\n")
    #SINCE WE HAVE r WE CAN CALCULATE e to find something coprime to r
    for i in range(1, 420):
        if (math.gcd(i,r)) == 1:
            e = i
    print("e is",e)
    print("\n")
    d = eea(e,r)
    outPriv = open("private_key.txt", "w")
    outPriv.write(str(d))
    outPriv.write("\n")
    outPriv.close()
    n  = rsaMod(p,q)
    print("\n")
    print("The RSA Mod is: ")
    print(n)
    outPub = open("public_key.txt", "w")
    outPub.write(str(n))
    outPub.write("\n")
    outPub.write(str(e))
    outPub.close()
    print("\n")
    print("What is the message you want to encrypt?\n")   
    m = 777777777777777000000000000000222222222222222333333333333333444444444444444222222222222222555555555555555666666666666666777777777777777888888888888888999999999999999000000000000
    cipherText = encrypt(m, e, n)
    pubKey = (n,e)
    print("This is the encrypted message:", cipherText, "\n")
    print("The public key is:", pubKey, "\n") 
    plainText = decrypt(cipherText, d, n)
    privKey = d 
    print("This is the decrypted message:", plainText, "\n")
    print("The private key is:", d, "\n")
                
            #OUTPUTTING TO A FILE
    outC = open("cipherText.txt", "w")
    outC.write(str(cipherText))
    outC.close()
    outP = open("decrypted_message.txt", "w")
    outP.write(str(plainText))
    outP.close()

    print(mod_exp(2,5,13)) #should equal 6 just testin
    print(eea(3,11)) #should be equal to 4 just testing

if __name__== '__main__':
    main()


