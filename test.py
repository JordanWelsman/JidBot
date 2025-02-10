import economy

# Reset Balance
economy.reset_balance("jordan")

# Get Balance
print(economy.get_balance("jordan"))

# Add Money
economy.add_funds("jordan", 30, "bank")
print(economy.get_balance("jordan"))

# Remove Money
economy.subtract_funds("jordan", 10, "bank")
print(economy.get_balance("jordan"))

# Move money to wallet
economy.withdraw_funds("jordan", 10)
print(economy.get_balance("jordan"))

# Move half back to bank
economy.deposit_funds("jordan", 5)
print(economy.get_balance("jordan"))