import numpy as np
import matplotlib.pyplot as plt

# Singleton class which represents the bank for a game.
class Bank:
    # Shared across instances.
    the_bank = {}

    def reset(self):
        Bank.the_bank = {}
    
    # Adds a player to the bank. Their default balance is zero.
    def create_account(self, name):
        if name in Bank.the_bank:
            print("[error] an account with name {} already exists".format(name))
            return False
        Bank.the_bank[name] = 0
        return True

    # Querys the bank to see if a given user has an account.
    def has_account(self, name):
        return name in Bank.the_bank

    # Returns the balance of an account holder.
    def check_balance(self, who):
        if who not in Bank.the_bank:
            print("[error] failed to check balance: no account for {}".format(who))
            return 0
        return Bank.the_bank[who]

    # Deposits _amount_ in the bank account for _who_.
    def deposit(self, who, amount):
        if who not in Bank.the_bank:
            print("[error] failed to deposit: no account for {}".format(who))
            return False
        if amount < 0:
            print("[error] can't deposit a negative amount")
            return False
        Bank.the_bank[who] += amount
        return True

    # Withdraws _amount_ in the bank account for _who_.
    def withdraw(self, who, amount):
        if who not in Bank.the_bank:
            print("[error] failed to withdraw: no account for {}".format(who))
            return False
        if amount < 0:
            print("[error] can't withdraw a negative amount")
            return False
        # if Bank.the_bank[who] < amount:
        #     print("[error] withdrawal amount ${} is more than balance ${} for {}"
        #           .format(amount, Bank.the_bank[who], who))
        #     return False
        Bank.the_bank[who] -= amount
        return True
