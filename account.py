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
        :return: Returns a boolean value
        """
        if amount <= 0:  # If amount is less than 0 then it cannot be deposited
            return False
        else:
            self.__account_balance += amount  # Readjusts the value of account_balance if function is valid
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method used to withdraw cash from the account
        :param amount: The amount to be withdrawn
        :return: Returns a boolean value
        """
        if 0 <= amount and amount < self.__account_balance:
            self.__account_balance -= amount  # Readjusts the value of account_balance if function is valid
            return True
        elif amount < 0 or self.__account_balance < amount:
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