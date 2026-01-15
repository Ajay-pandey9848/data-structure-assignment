# Read input string
s=input("enter the strings:")

s.strip()

# Sort characters by Unicode value
sorted_string = ''.join(sorted(s))

# Print result
print(sorted_string)



