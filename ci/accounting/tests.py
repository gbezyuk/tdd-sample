from django.test import TestCase
from ci.accounting.models import Account

class TestAccountTransaction(TestCase):
    def test_transaction_succed(self):
        """
        Tests valid transaction succed
        """
        account1 = Account.objects.create(amount=25)
        account2 = Account.objects.create(amount=0)
        account1.withdraw(10, account2)
        self.assertEquals(account1.amount, 15)
        self.assertEquals(account2.amount, 10)
