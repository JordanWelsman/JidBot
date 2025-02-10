# Economy Management

# Module Imports
import json
import os

# import discord

# Load Bot Variables
BALANCE_FILE = "balances.json"

# Expose Functions & Constants
__all__ = ["BALANCE_FILE",
           "load_balances",
           "save_balances",
           "generate_balance",
           "get_balance",
           "update_balance",
           "reset_balance",
           "withdraw_funds",
           "deposit_funds",
           "add_funds",
           "subtract_funds"]

# Load Balances from JSON
def load_balances():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            return json.load(f)
    return {}

# Save Balances to JSON
def save_balances(balances:dict):
    with open(BALANCE_FILE, "w") as f:
        json.dump(balances, f, indent=4)

# Generate New Player Balance
def generate_balance():
    return {"bank": 0, "wallet": 0}

# Get a User's Balance
def get_balance(user_id:str):
    balances = load_balances()
    if str(user_id) not in balances:
        balances[str(user_id)] = generate_balance()
        save_balances(balances)
    return balances[str(user_id)]

# Update a User's Balance
def update_balance(user_id:str, wallet_change:int=0, bank_change:int=0):
    balances = load_balances()
    user_id = str(user_id)
    if user_id not in balances:
        balances[user_id] = generate_balance()
    balances[user_id]["wallet"] += wallet_change
    balances[user_id]["bank"] += bank_change
    save_balances(balances)

# Reset a User's Balance
def reset_balance(user_id: str):
    balances = load_balances()
    user_id = str(user_id)
    balances[user_id] = generate_balance()
    save_balances(balances)

# Withdraw Funds
def withdraw_funds(user_id:str, amount:int):
    balances = load_balances()
    user_id = str(user_id)
    if user_id not in balances:
        balances[user_id] = generate_balance()
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if amount > balances[user_id]["bank"]:
        raise ValueError("Insufficient bank balance.")
    update_balance(user_id, amount, -amount)

# Deposit Funds
def deposit_funds(user_id:str, amount:int):
    balances = load_balances()
    user_id = str(user_id)
    if user_id not in balances:
        balances[user_id] = generate_balance()
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if amount > balances[user_id]["wallet"]:
        raise ValueError("Insufficient wallet balance.")
    update_balance(user_id, -amount, amount)

# Add Funds to User
def add_funds(user_id:str, amount:int, storage:str="bank"):
    balances = load_balances()
    user_id = str(user_id)
    if user_id not in balances:
        balances[user_id] = generate_balance()
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if storage.lower() == "bank":
        update_balance(user_id, 0, amount)
    elif storage.lower() == "wallet":
        update_balance(user_id, amount, 0)
    else:
        raise ValueError(f"Invalid storage type: {storage}. Expected 'bank' or 'wallet'.")
    
# Subtract Funds from User
def subtract_funds(user_id:str, amount:int, storage:str="bank"):
    balances = load_balances()
    user_id = str(user_id)
    if user_id not in balances:
        balances[user_id] = generate_balance()
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if storage.lower() == "bank":
        update_balance(user_id, 0, -amount)
    elif storage.lower() == "wallet":
        update_balance(user_id, -amount, 0)
    else:
        raise ValueError(f"Invalid storage type: {storage}. Expected 'bank' or 'wallet'.")