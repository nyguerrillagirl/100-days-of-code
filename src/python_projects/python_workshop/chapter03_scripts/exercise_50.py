def countdown(n):
    if n == 0:
        print("liftoff!!")
    else:
        print(n)
        return countdown(n-1)


countdown(3)