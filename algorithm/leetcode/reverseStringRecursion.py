def reverse(str):
    if len(str) == 0:
        return str    
    return reverse(str[1:]) + str[0]


print(reverse("myjobaaaaaaaaaaaffffffffffffffffddddddddd"))