"""Enumeration of cash denomination values.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from enum import Enum


class CashDenomination(Enum):
    """Enumeration of cash denomination values."""
    PENNY = ("Penny", 0.01)
    NICKEL = ("Nickel", 0.05)
    DIME = ("Dime", 0.10)
    QUARTER = ("Quarter", 0.25)
    HALF_DOLLAR = ("Half Dollar", 0.50)
    DOLLAR_COIN = ("Dollar Coin", 1.0)
    ONE_DOLLAR_BILL = ("$1 Bill", 1.0)
    FIVE_DOLLAR_BILL = ("$5 Bill", 5.0)
    TEN_DOLLAR_BILL = ("$10 Bill", 10.0)
    TWENTY_DOLLAR_BILL = ("$20 Bill", 20.0)
    FIFTY_DOLLAR_BILL = ("$50 Bill", 50.0)
    HUNDRED_DOLLAR_BILL = ("$100 Bill", 100.0)

    def __init__(self, description: str, amount: float) -> None:
        """Constructor.

        Args:
            description: the description of the denomination
            amount: the amount it represents
        """
        self.description: str = description
        self.amount: float = amount

    def __str__(self) -> str:
        """String description of the denomination.

        Returns:
            string description
        """
        return str(self.description)
