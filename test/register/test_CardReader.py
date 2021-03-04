"""Test Card Reader.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from unittest import mock
from cc410.register.CardReader import CardReader
from cc410.register.CardTransactionResult import CardTransactionResult


class TestCardReader():
    """Test Card Reader."""

    def test_run_card_declined(self) -> None:
        """Test declined result."""
        with mock.patch('random.randint', lambda x, y: 0):
            reader: CardReader = CardReader()
            assert_that(reader.run_card(), is_(CardTransactionResult.DECLINED))

    def test_run_card_read_error(self) -> None:
        """Test read_error result."""
        with mock.patch('random.randint', lambda x, y: 1):
            reader: CardReader = CardReader()
            assert_that(reader.run_card(),
                        is_(CardTransactionResult.READ_ERROR))

    def test_run_card_insufficient_funds(self) -> None:
        """Test insufficient funds result."""
        with mock.patch('random.randint', lambda x, y: 2):
            reader: CardReader = CardReader()
            assert_that(reader.run_card(),
                        is_(CardTransactionResult.INSUFFICIENT_FUNDS))

    def test_run_card_incorrect_pin(self) -> None:
        """Test incorrect pin result."""
        with mock.patch('random.randint', lambda x, y: 3):
            reader: CardReader = CardReader()
            assert_that(reader.run_card(),
                        is_(CardTransactionResult.INCORRECT_PIN))

    def test_run_card_approved(self) -> None:
        """Test approved result."""
        reader: CardReader = CardReader()
        with mock.patch('random.randint', lambda x, y: 4):
            assert_that(reader.run_card(), is_(CardTransactionResult.APPROVED))
        with mock.patch('random.randint', lambda x, y: 5):
            assert_that(reader.run_card(), is_(CardTransactionResult.APPROVED))
        with mock.patch('random.randint', lambda x, y: 6):
            assert_that(reader.run_card(), is_(CardTransactionResult.APPROVED))
        with mock.patch('random.randint', lambda x, y: 7):
            assert_that(reader.run_card(), is_(CardTransactionResult.APPROVED))
        with mock.patch('random.randint', lambda x, y: 8):
            assert_that(reader.run_card(), is_(CardTransactionResult.APPROVED))
        with mock.patch('random.randint', lambda x, y: 9):
            assert_that(reader.run_card(), is_(CardTransactionResult.APPROVED))
