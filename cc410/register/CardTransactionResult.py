"""Enumeration of card transaction results.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from enum import Enum


class CardTransactionResult(str, Enum):
    """Enumeration of card transaction results."""
    APPROVED = "Approved"
    DECLINED = "Declined"
    READ_ERROR = "Card Read Error"
    INSUFFICIENT_FUNDS = "Insufficient Funds"
    INCORRECT_PIN = "Incorrect PIN"

    def __str__(self) -> str:
        """String description of the result.

        Returns:
            string description
        """
        return str(self.value)
