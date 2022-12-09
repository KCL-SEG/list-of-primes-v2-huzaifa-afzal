"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2] #2 always first prime
    if number_of_primes <= 0:
        raise ValueError
    j = 3
    while len(list) < number_of_primes:
        prime = True
        for i in range (2, j):
            if j % i == 0:
                prime = False
                break
        if(prime==True):
            list.append(j)
        j +=1
    return list
