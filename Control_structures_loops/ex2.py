num = int(input("give me a number please>"))

def check(a):
    if a > 0:
        for i in range(2,a):
            if (a%i) == 0:
                return False
        return True
    else:
        print("not whole number")
        return False
  

print(check(num))
