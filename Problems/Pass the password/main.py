# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()

# your code below
sorted_passwords = sorted(passwords, key=len)
for password in sorted_passwords:
    print(f"{password} {len(password)}")
