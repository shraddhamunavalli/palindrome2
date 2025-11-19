import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    s = sys.argv[1]
    print("User provided string:")
else:
    script_name = sys.argv[0]
    s = "madam"
    print("No input given - using default string:")

original = s.lower()

reverse = ""
for ch in original:
    reverse = ch + reverse

if original == reverse:
    result = "Palindrome"
else:
    result = "Not a Palindrome"

print("Script Name:", script_name)
print("String:", s)
print("Reversed String:", reverse)
print("Result:", result)
