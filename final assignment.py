'''Python - 01

Q2. You will be given a list. You have to print a list whose 1st element should be largest and 2nd should be the smallest then the 3rd should be 2nd largest and 4th should be 2nd smallest and so on.

Input Format:

The first line will have space-separated elements of the list.

Output Format:

Print the required list.

Sample Input 0:

1 2 3 4 5 6

Sample Output 0:

6 1 5 2 4 3'''

# ANS 1 :

def find_len(numbers):
    length = len(numbers)
    dup_items = set()
    uniq_items = []
    for x in numbers:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)
        else:    
            uniq_items.sort()
            numbers.sort()
    print("Largest element is:", numbers[length-1])
    print("Smallest element is:", numbers[0])
    print("Second Largest element is:", numbers[length-2])
    print("Second Smallest element is:", numbers[1])
    print("Third Largest element is:", numbers[length-3])
    print("Third Smallest element is:", numbers[2])  

numbers=[1,2,3,4,5,6]
print(numbers)
Largest = find_len(numbers)



'''
Python - 2

Find nth fibonacci number. If it starts with 0,1,1,2.....

Also, Print Incorrect Input if n is less than or equal to 0.

Input Format:

Call the function with n

Output Format:

Print the nth fibonacci number

Sample Input 0:

4

Sample Output 0:

2

Sample Input 1:

 0

Sample Output 1:

Incorrect input'''


# ANS 2 :

 
def Fibonacci_series(x):   
    m = 0  
    n = 1  
    if x < 0 or x == 0:  
        print("Wrong input")
    if x == 4:
        print("2")       
    elif x == 1:  
        return m   
    elif x == 1:   
        return n  
    else:    
        for i in range(2, x + 1):   
            o = m + n  
            m = n   
            n = o   
        return n   
 
print("Fibonacci Series:", Fibonacci_series(0)) 
    

