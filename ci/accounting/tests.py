from django.test import TestCase
from ci.accounting.models import Account, Currency
from django_any import any_model
from django.core.exceptions import ValidationError

class TestAccountTransaction(TestCase):
    def setUp(self):
        """
        Setting up model instances. Using factory (django_any) instead of fixtures (couse fixtures are evil)
        """
        self.currency1 = any_model(Currency)    
        self.currency2 = any_model(Currency)
        self.account1 = any_model(Account, amount=25, currency=self.currency1)
        self.account2 = any_model(Account, amount=0, currency=self.currency1)
        self.account3 = any_model(Account, amount=1000)

    def test_currency_create_same_name_fails(self):
        """
        Tests that creation of two currencies with same names will fail
        """
        c1 = any_model(Currency)
        self.assertRaises(ValidationError, any_model, Currency, **{'name': c1.name})

    def test_transaction_succed(self):
        """
        Tests valid transaction succed
        """
        self.account1.withdraw(10, self.account2)
        self.assertEquals(self.account1.amount, 15)
        self.assertEquals(self.account2.amount, 10)

    def test_transaction_fails(self):
        """
        Tests invalid transaction fail (insufficient money amount)
        """
        self.assertRaises(AssertionError, self.account1.withdraw, 100, self.account2)

    def test_different_currencies_transaction_fails(self):
        """
        Tests that transaction with accounts having different currencies fails
        """
        self.assertRaises(AssertionError, self.account3.withdraw, 100, self.account2)
