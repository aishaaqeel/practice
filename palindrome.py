a = input("Enter a string: ")
b = ""
for i in range(len(a)-1, -1, -1):
    b += a[i]
[print("String is palindrome") if a ==
 b else print("String is not palindrome")]
