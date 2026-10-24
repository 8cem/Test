first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

if first_num > second_num:
    print(f"{first_num} is greater than {second_num}")
elif second_num < first_num:
    print(f"{second_num} is less than {first_num}")
elif first_num == second_num:
    print(f"{first_num} is equal to {second_num}")
