class Account:
    def __init__(self, name: str) -> None:
        """
        Method used to set the name of an account and make a balance that's set to 0
        :param name: Account holder's first name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method used to increase the account balance by a specified amount.
        :param amount: The amount to be deposited
        :return: Returns True if amount is greater than 0, otherwise returns False
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method used to withdraw cash from the account
        :param amount: The amount to be withdrawn
        :return: Returns True if amount is greater than 0 and also less than the account balance,
        otherwise it will return False
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        elif amount <= 0 or self.__account_balance < amount:
            return False

    def get_balance(self) -> float:
        """
        Method to get the account balance
        :return: Returns the account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to get the name of the account
        :return: Returns the name of the account
        """
        return self.__account_name