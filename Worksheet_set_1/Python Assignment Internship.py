#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Which of the following operators is used to calculate remainder in a division? Ans = C) %


# In[ ]:


#2. In python 2//3 is equal to? Ans = B) 0


# In[ ]:


#3. In python, 6<<2 is equal to? Ans = C) 24


# In[ ]:


#4. In python, 6&2 will give which of the following as output? Ans = A) 2


# In[ ]:


#5. In python, 6|2 will give which of the following as output? Ans = D) 6


# In[ ]:


#6. What does the finally keyword denotes in python? Ans = C) the finally block will be executed no matter if the try block raises an error or not.


# In[ ]:


#7. What does raise keyword is used for in python? Ans = A) It is used to raise an exception.


# In[ ]:


#8. Which of the following is a common use case of yield keyword in python? Ans = C) in defining a generator


# In[ ]:


#9. Which of the following are the valid variable names? Ans = D) None of the above


# In[ ]:


#10. Which of the following are the keywords in python? Ans = A)yeild B)raise


# In[9]:


#11. Write a python program to find the factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))

if num < 0:
    print("Factorial cannot be found for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")


# In[10]:


#12. Write a python program to find whether a number is prime or composite.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is a composite number.")

if __name__ == "__main__":
    main()


# In[11]:


#13. Write a python program to check whether a given string is palindrome or not.

def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    # Compare the string with its reverse
    return s == s[::-1]

def main():
    string = input("Enter a string: ")
    if is_palindrome(string):
        print(f"The string '{string}' is a palindrome.")
    else:
        print(f"The string '{string}' is not a palindrome.")

if __name__ == "__main__":
    main()


# In[ ]:


#14. Write a Python program to get the third side of right-angled triangle from two given sides.


# In[ ]:


#15. Write a python program to print the frequency of each of the characters present in a given string


# In[ ]:




