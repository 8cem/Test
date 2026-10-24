first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
third_num = int(input("Enter third number: "))

# count up the numbers of evenr or odd
even_count = 0
odd_count = 0

if first_num % 2 == 0:
    even_count += even_count
else :
    odd_count += odd_count
if second_num % 2 == 0:
    even_count += even_count
elif second_num % 2 == 0:
   odd_count += odd_count
if third_num % 2 == 0:
   even_count += even_count
elif third_num % 2 == 0:
    odd_count += odd_count

print(f"Even number: {even_count}")
print(f"Odd number: {odd_count}")