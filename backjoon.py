# #1330
# a, b = map(int, input().split())
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')
    
# #9498
# score = int(input())
# if  90 <= score <= 100:
#     print('A')
# elif 80 <= score <= 89:
#     print('B')
# elif 70 <= score <= 79:
#     print('C')
# elif 60 <= score <= 69:
#     print('D')
# else:
#     print('F')

# #2753
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(1)
# else:
#     print(0)
    
# #14681
# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# elif x > 0 and y < 0:
#     print(4)
    
# #2884
# h,m = map(int, input().split())
# if m > 44:
#     print(h, m - 45)
# elif m < 45 and h > 0:
#     print(h - 1, m + 15)
# else:
#     print(23, m + 15)
    
# #2739
# n = int(input())
# for i in range(1, 10):
#     print(n, "*", i, "=", n * i)
    
# #10950
# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#     print(a + b)
    
# #8393
# n = int(input())
# cnt = 0
# for i in range(1, n + 1):
#     cnt += i
# print(cnt)

# #15552
# import sys
# n = int(sys.stdin.readline())
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a + b)

# #2741
# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# #11021
# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#     print("Case #%s: %s"%(i + 1, a +b))

# #11022
# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#     print("Case #%s: %s + %s = %s"%(i + 1, a, b, a + b))

#10818
# num = int(input())
# number = list(map(int, input().split()))
# print(min(number), max(number))

#2562
# number = []
# for i in range(0, 9):
#     number.append(int(input()))
# max = max(number)
# print(max)
# print(number.index(max) + 1)

#2577
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# result = list(str(n1 * n2 * n3))
# for i in range(10):
#     print(result.count(str(i)))

#3052
# number = []
# result = []
# for i in range(10):
#     number.append(int(input()))
#     result.append(number[i] % 42)
# result = set(result)
# print(len(result))

#1546
# num = int(input())
# number = list(map(int, input().split()))
# max = max(number)
# list = []
# for s in number:
#     list.append(s / max * 100)
# avg = sum(list) / num
# print(avg)

#오류 그만 떠라