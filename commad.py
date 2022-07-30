"""
Command Coding Exercise
Implement the Account.process()  method to process different account commands.

The rules are obvious:
success indicates whether the operation was successful
You can only withdraw money if you have enough in your account
"""
from enum import Enum

class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False
        
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        if command.action == command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == command.Action.WITHDRAW:
            command.success = True
            if self.balance - command.amount >= 0:
                self.balance -= command.amount
            else:
                command.success = False
