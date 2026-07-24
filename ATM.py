# ========Group Members====================
# Rogielyn C. Amisola = 2411600094
# Ali Akbhar C. Jikiri = 2411600058
# Arjun B Lawag =
# ========Details=========================
# Programming Language: Python
# Description: This program simulates a basic
# ATM Withdrawal System. It initializes an
# account balance, asks the user for a
# withdrawal amount, validates the transaction,
# and displays the result.
# ==========================================


# Account balance account_balance = 500.00
account_balance = 500.00

# Welcome Message
print ("Welcome to AJL ATM")
# Withdrawal message withdrawal_amount equal to user input
withdrawal_amount = float(input("Enter withdrawal amount: "))


# Validation logic uses withdrawal_amount less than equal to account_balance
# account_balance is deducted from the withdrawal_amount
# else withdrawal amount is greater than account_balance
# code diri

if withdrawal_amount <= account_balance:
    account_balance -= withdrawal_amount
    print(f"Withdrawal successful. Remaining balance: ${account_balance:.2f}")
else:
    print("Insufficient funds.")
