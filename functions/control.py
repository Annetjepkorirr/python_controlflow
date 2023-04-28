# Write a function that uses while, if and continue statements to 
# print all the even numbers between 0 and 50. 
def find_even_numbers():
    y=0
    while y<50:
        y+=1
        if y%2!=0:
            continue
        print(y)     

# Write a function that takes an integer argument and prints "Prime" if the number is prime,
#  and "Not prime" 
# if the number is not prime.
def prime_numbers(num):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                print("Not prime")
                break
            else:
                print("Is prime")    
    
# Write a function that takes a list of integers as input and prints the sum
#  of all the even numbers in the list.
def addition_even(list_interger):
    summation=0
    for l in list_interger:
        if l%2==0:
            summation+=l
        print(summation)

# Write a function that takes any two integers as input, and prints the sum of all the 
# numbers between the two integers (inclusive) 
# that are divisible by 3.
def add_int(a,b):
    c=0
    for i in range(a,b):
        if i%2!=0:
            c+=i
    print(c)  