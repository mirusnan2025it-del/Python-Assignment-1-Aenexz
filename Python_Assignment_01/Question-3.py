
# Accept order amount and membership status
amount = float(input("Enter order amount: "))
membership = input("Are you a member? (yes/no): ").strip().lower()

# Validate order amount
if amount < 0 or amount > 100000:
    print("Invalid order amount.")
elif membership != "yes" and membership != "no":
    print("Invalid membership status. Enter yes or no.")
else:
    # Determine discount percentage
    if amount >= 5000:
        discount_percent = 15
    elif amount >= 2000 and amount < 5000 and membership == "yes":
        discount_percent = 10
    else:
        discount_percent = 0

    # Calculate discount and final amount
    discount = amount * discount_percent / 100
    final_amount = amount - discount

    # Display results
    print("Original amount: ₹", amount)
    print("Discount percentage:", discount_percent, "%")
    print("Discount amount: ₹", discount)
    print("Final payable amount: ₹", final_amount)

    if discount_percent > 0:
        print("Eligibility status: Eligible for discount")
    else:
        print("Eligibility status: Not eligible for discount")
