def isPalindrome(num):
    num = str(num)
    temp = ""
    for i in range(len(num)-1,-1,-1):
        temp += num[i]
    if(str(num) == temp):
        return True
    else:
        return False

num = 1221
print(num, "is a palindrome: " , isPalindrome(num))