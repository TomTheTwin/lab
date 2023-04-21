from account import *
from pytest import *


class Test:
    def setup(self):
        self.a1 = Account('John')
        self.a2 = Account('Jane')

    def teardown(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0
        assert self.a1.get_balance() != 50.00
        assert self.a1.get_balance() != -50.00
        assert self.a1.get_balance() != 'zero'
        assert self.a2.get_name() == 'Jane'
        assert self.a2.get_balance() == 0
        assert self.a2.get_balance() != 50.00
        assert self.a2.get_balance() != -50.00
        assert self.a2.get_balance() != 'zero'

    def test_deposit(self):
        assert self.a1.deposit(50.00) == True
        assert self.a1.get_balance() == 50.00
        assert self.a1.deposit(-50.00) == False
        assert self.a1.get_balance() == 50.00
        assert self.a1.deposit(0) == False
        assert self.a1.get_balance() == 50.00
        assert self.a2.deposit(50.00) == True
        assert self.a2.get_balance() == 50.00
        assert self.a2.deposit(-50.00) == False
        assert self.a2.get_balance() == 50.00
        assert self.a2.deposit(0) == False
        assert self.a2.get_balance() == 50.00

    def test_withdraw(self):
        self.a1.deposit(50.00)
        assert self.a1.withdraw(50.00) == True
        assert self.a1.get_balance() == 0.00
        assert self.a1.withdraw(-50.00) == False
        assert self.a1.get_balance() == 0.00
        assert self.a1.withdraw(0.00) is False
        assert self.a1.get_balance() == 0.00
        assert self.a1.withdraw(50.00) is False
        self.a2.deposit(50.00)
        assert self.a2.withdraw(50.00) == True
        assert self.a2.get_balance() == 0.00
        assert self.a2.withdraw(-50.00) == False
        assert self.a2.get_balance() == 0.00
        assert self.a2.withdraw(0.00) is False
        assert self.a2.get_balance() == 0.00
        assert self.a2.withdraw(50.00) is False
