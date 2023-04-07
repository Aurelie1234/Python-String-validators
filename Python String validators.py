if __name__ == '__main__':
    s = input()
    if any(ele.isalnum() for ele in s):
     print(True)
    else:
     print(False)
    
    if any(ele.isalpha() for ele in s):
     print(True)
    else:
     print(False)
     
    if any(ele.isdigit() for ele in s):
     print(True)
    else:
     print(False)
    
    if any(ele.islower() for ele in s):
     print(True)
    else:
     print(False)
     
    if any(ele.isupper() for ele in s):
     print(True)
    else:
     print(False)
