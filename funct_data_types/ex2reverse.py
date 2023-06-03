#ex2 reverse_string

def reverse_string():
    string = str(input("Give me a string to reverse>"))
    reversed_str = ''
    #return string[::-1] #everything, with step reversed
    for i in range(len(string)-1,-1,-1):
        reversed_str += string[i]
    return reversed_str

print(reverse_string())

def reverse_string2():
    string = str(input("Give me a string to reverse>"))
    return string[::-1] #everything, with step reversed
    
    
print(reverse_string2())