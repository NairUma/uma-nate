#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
    def __str__(self):
        return "label is %s and the balance is %s" % (self.label, self.balance)
    def withdraw(self, value):
        if self.balance - value < 0:
            print("Too large amount to be withdrawn. You currently have %s." % self.balance)
        elif value < 0:
            print("Invalid Input, must be a positive number.")
        else:
            self.balance = self.balance - value
    def deposit(self, value):
        if value < 0:
            print("Invalid Input, must be a positive number.")
        else:
            self.balance = self.balance + value
    def rename(self, labell):
        if labell == "":
            print("Can not be blank")
        else:
            self.label = labell
    def transfer(self, value, dest_account):
        if value > self.balance:
            print("Can not transfer more than is in account get nay'nay'd")
        elif amount < 0:
            print("Can not transfer negative values.")
        else:
            self.balance = self.balance - value
            dest_account.deposit(value)
#user_input = int(raw_input("Enter value of deposit/withdrawal: "))
