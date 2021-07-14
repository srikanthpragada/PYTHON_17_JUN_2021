# Accept 5 numbers and display total
# Make sure invalid numbers are ignored

total = 0
count = 1
while count <= 5:
    try:
        num = int(input(f"Enter Number {count} :"))
        total += num
        count += 1
    except ValueError:
        print("Invalid Number!")


print("Total :", total)
