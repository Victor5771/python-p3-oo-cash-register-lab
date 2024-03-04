#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total_price = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total_price += price * quantity
        self.items.append((title, price, quantity))

    def apply_discount(self):
        if self.discount > 0:
            self.total_price *= (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${self.total_price:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_title, last_item_price, last_item_quantity = self.items.pop()
            self.total_price -= last_item_price * last_item_quantity
            if not self.items:
                self.total_price = 0

    def total(self):
        return self.total_price
