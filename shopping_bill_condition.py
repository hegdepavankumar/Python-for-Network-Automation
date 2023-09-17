
# Calculate the shipping charges for shopping


print("\n")
total_amount = float(input("Enter the total amount of your purchase: $"))
fixed_amount = 50.0

if total_amount < fixed_amount:
    print(f"Your Total Shopping amount is : ${total_amount}")
    shipping_charge = 10.0
    print(f"Shipping charge: ${shipping_charge}")
    total_cost = total_amount + shipping_charge
else:
    shipping_charge = 0.0
    print(f"Your Total Shopping amount is : ${total_amount}")
    print("Congratulations Your Shipping is free!!")
    total_cost = total_amount

print(f"Total Amount Need to Pay : ${total_cost}")
print("Thanks For Shopping!!")