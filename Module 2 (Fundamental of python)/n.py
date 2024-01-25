n = int(input("Enter a positive integer (n): "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print(f"The sum of the first {n} positive integers is: {n * (n + 1) // 2}")
