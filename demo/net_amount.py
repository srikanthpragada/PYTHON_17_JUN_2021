# Calculate net amount based on price and qty

price = int(input("Enter price :"))
qty = int(input("Enter quantity :"))

amount = price * qty
tax = amount * 12 // 100
net_amount = amount + tax

print(f"Amount            {amount:8}")
print(f"+ Tax             {tax:8}")
print(f"                  {'-' * 8}")
print(f"Net Amount        {net_amount:8}")

