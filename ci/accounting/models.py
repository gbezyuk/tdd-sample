from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    amount = models.IntegerField()
    user = models.ForeignKey(to=User)

    def withdraw(self, amount, account):
        assert self.amount >= amount
        self.amount -= amount
        account.amount += amount
