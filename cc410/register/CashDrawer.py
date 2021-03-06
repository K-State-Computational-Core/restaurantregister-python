"""Class to represent a cash drawer.

Typical use is to instantiate a drawer and call `getCount()` and
`getTotal()` methods to get the state of the drawer while closed.

To perform a transaction, call `open()` to open the drawer, providing
the amount to be deposited. Then, use `addCount()` and `removeCount()`
to update the amounts of each denomination in the drawer as the customer
provides cash and change is made and given back to the customer. Finally,
call `close()` to close the drawer. The class will verify that the amount in
the drawer reflects the original amount plus the transaction amount

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from typing import Dict
from cc410.register.CashDenomination import CashDenomination


class CashDrawer:
    """Class to represent a cash drawer."""

    def __init__(self) -> None:
        """Constructor to initialize the cash drawer."""
        self.__contents: Dict[CashDenomination, int] = dict()
        for denom in CashDenomination:
            self.__contents[denom] = 10
        self.__open: bool = False
        self.__updated_total: int = 0

    def get_count(self, denom: CashDenomination) -> int:
        """Get the count of the denomination in the drawer.

        Args:
            denom: the denomination to check

        Returns:
            the count of that denomination in the drawer

        Raises:
            RuntimeError: if the drawer is not closed
        """
        if self.__open:
            raise RuntimeError("Cash drawer must be closed to count.")
        return self.__contents[denom]

    def get_total(self) -> float:
        """Get the total value of cash in the drawer.

        Returns:
            the total value of the cash

        Raises:
            RuntimeError: if the drawer is not closed
        """
        if self.__open:
            raise RuntimeError("Cash drawer must be closed to count.")
        total: float = 0.0
        for denom in CashDenomination:
            total += self.__contents[denom] * denom.amount
        return total

    def add_count(self, denom: CashDenomination, count: int) -> None:
        """Add to the count of the denomination in the drawer.

        Args:
            denom: the denomination to add to
            count: the count to add

        Raises:
            RuntimeError: if the drawer is not open
            ValueError: if the count is negative
        """
        if not self.__open:
            raise RuntimeError("Cash drawer must be open to modify.")
        if count < 0:
            raise ValueError("Count must not be negative.")
        self.__contents[denom] += count

    def remove_count(self, denom: CashDenomination, count: int) -> None:
        """Remove from the count of the denomination in the drawer.

        Args:
            denom: the denomination to remove from
            count: the count to remove

        Raises:
            RuntimeError: if the drawer is not open
            ValueError: if the count is negative
            ValueError: if the count is greater than the number present
        """
        if not self.__open:
            raise RuntimeError("Cash drawer must be open to modify.")
        if count < 0:
            raise ValueError("Count must not be negative.")
        if count > self.__contents[denom]:
            raise ValueError("Cannot remove more than are present.")
        self.__contents[denom] -= count

    def open(self, amount: float) -> None:
        """Open the cash drawer.

        Args:
            amount: The amount to be deposited

        Raises:
            ValueError: if the amount is negative
        """
        if amount < 0:
            raise ValueError("Amount must not be negative.")
        self.__updated_total = round((self.get_total() + amount) * 100.0)
        self.__open = True

    def close(self) -> None:
        """Close the cash drawer.

        If the contents are incorrect, the drawer is not closed.

        Raises:
            RuntimeError: if the cash drawer contents are incorrect.
        """
        self.__open = False
        total: float = self.get_total()
        if not self.__updated_total == round(total * 100.0):
            self.__open = True
            raise RuntimeError("Cash drawer contents incorrect.")
        self.__updated_total = 0
