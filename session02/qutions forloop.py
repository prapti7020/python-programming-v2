# (1)
# for i in range(1,100):
#     print(i)


# (2)
# for i in range(100,0,-1):
#     print(i)

# (3)
# for i in range(1,100):
#     if i % 2 == 0:
#         print(i)


# (4)
# for i in range(1,100):
#     if i % 2 != 0:
#         print(i)

# (5)
# n = 5
# total = 0
# for i in range(1,n+1):
#     total = total + 1
#     print(total)


# # (6)
# n = 5
# for i in range(1,11):
#     print(n, "X",i ,"=",n*i)
    

# (7)
# n = 4
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
#     print(fact)


# (8)
# a = 0
# b = 1
# for i in range(7):
#     print(a)
#     c = a + b
#     a = b
#     b = c



# (9)
# n = 1234
# rev = 0
# for i in range(4):
#     digit = n % 10
#     rev = rev * 10 +  digit
#     n = n // 10
#     print(rev)


# (10)
# n = 12345
# count = 0
# for i in str(n):
#     count = count +1

# print(count)


# (11)
# n = 1234
# total = 0
# for i in str(n):
#     digit = n % 10
#     total = total + digit
#     n = n // 10

# print(total)


# (12)
# n = 234
# product = 1
# for i in str(n):
#     digit = n % 10
#     product = product * digit
#     n = n // 10

# print(product)


# (13)
# n = 121
# original = n
# rev = 0
# for i in str(n):
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# if original == rev:
#     print("palindrome")
# else:
#     print("not palindrome")



# # (14)
# n = 153
# original = n
# total = 0
# for i in str(n):
#     digit = n % 10
#     total = total + digit ** 3
#     n = n // 10

# if total == original:
#     print("armstrong number")
# else:
#     print("not amstrong number")


(15)
n = 7 
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("prime")
else:
    print("not prime")


# (16)
# n = 10
# for num in range(2,n+1):
#     count = 0

# for i in range(1,num +1):
#     if num % i == 0:
#         count = count + 1

# if count == 2:
#     print(num)

# (17)
# a = 12
# b = 18
# gcd = 1
# for i in range(1, min(a,b) + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i
# print(gcd)


# (18)
# a = 4
# b = 6
# for i in range(max(a,b),a * b + 1):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break


