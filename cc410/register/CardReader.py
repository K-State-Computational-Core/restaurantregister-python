"""Class to represent a credit card reader.

Call the `run_card()` method to simulate using a credit card.

Once of the `CardTransactionResult` values will be returned.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

import random
from cc410.register.CardTransactionResult import CardTransactionResult


class CardReader:
    """Class to represent a credit card reader."""

    def run_card(self) -> CardTransactionResult:
        """Method to run a credit card.

        Returns:
            a `CardTransactionResult` giving the outcome
        """
        rand: int = random.randint(0, 9)
        if rand == 0:
            return CardTransactionResult.DECLINED
        elif rand == 1:
            return CardTransactionResult.READ_ERROR
        elif rand == 2:
            return CardTransactionResult.INSUFFICIENT_FUNDS
        elif rand == 3:
            return CardTransactionResult.INCORRECT_PIN
        else:
            return CardTransactionResult.APPROVED
