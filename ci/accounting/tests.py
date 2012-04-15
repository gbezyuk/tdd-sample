from django.test import TestCase
from ci.accounting.models import Account
from django_any import any_model

class TestAccountTransaction(TestCase):
    def test_transaction_succed(self):
        """
        Tests valid transaction succed
        """
        account1 = any_model(Account, amount=25)
        account2 = any_model(Account, amount=0)
        account1.withdraw(10, account2)
        self.assertEquals(account1.amount, 15)
        self.assertEquals(account2.amount, 10)
    def test_transaction_fails(self):
        """
        Tests invalid transaction fail (insufficient money amount)
        """
        account1 = any_model(Account, amount=10)
        account2 = any_model(Account)
        self.assertRaises(AssertionError, account1.withdraw, 100, account2)
