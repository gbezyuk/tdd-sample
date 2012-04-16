from django.db import models
from django.contrib.auth.models import User

class Currency(models.Model):
    name = models.CharField(max_length=10, unique=True)

class Account(models.Model):
    amount = models.IntegerField()
    user = models.ForeignKey(to=User)
    currency = models.ForeignKey(to=Currency)

    def withdraw(self, amount, target_account):
        assert self.amount >= amount
        assert self.currency.name == target_account.currency.name
        self.amount -= amount
        target_account.amount += amount
