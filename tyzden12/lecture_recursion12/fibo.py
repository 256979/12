
def main():
    pass
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)


print(fibonacci(0))
for n in range(10):
    print(fibonacci(n))


if __name__ == "__main__":
    main()


