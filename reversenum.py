n = int(input("Enter the Number: "))
rev_num = 0
while (n > 0):
    rev_num = (rev_num * 10) + n % 10
    n //= 10
print(rev_num)
