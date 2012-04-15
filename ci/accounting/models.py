from django.db import models

class Account(models.Model):
    amount = models.IntegerField()

    def withdraw(self, amount, account):
        self.amount -= amount
        account.amount += amount
