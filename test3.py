num=int(input("Enter a number : "))
def fact(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)
ans=factorial(num)
print("Factorial of",num,"is",ans)
