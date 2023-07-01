def f(n):
    if n == 0 or n == 1:
        a = n + 1 
        return a 
    if n > 1:
        return f(n-1)+f(n//2)
def main():
    print(f(int(input())))
main()