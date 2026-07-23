# Account balance account_balance = 500.00
account_balance = 500.00

# Welcome Message
print ("Welcome to JAL ATM")
# Withdrawal message withdrawal_amount equal to user input
withdrawal_amount = float(input("Enter the amount of your withdrawal:"))

# Validation logic uses withdrawal_amount less than equal to account_balance
# account_balance is deducted from the withdrawal_amount
# else withdrawal amount is greater than account_balance
if withdrawal_amount <= account_balance:
    account_balance -= withdrawal_amount
    print("Withdrawal successful!")
    print(f"Remaining Balance: ₱{account_balance:.2f}")
else:
    print("Insufficient funds!")