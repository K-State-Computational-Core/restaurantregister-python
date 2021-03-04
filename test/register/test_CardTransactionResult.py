"""Test Card Transaction Result.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from cc410.register.CardTransactionResult import CardTransactionResult


class TestCardTransactionResult():
    """Test Card Transaction Result."""

    def test_approved(self) -> None:
        """Test Approved."""
        assert_that(str(CardTransactionResult.APPROVED), is_("Approved"))

    def test_declined(self) -> None:
        """Test Declined."""
        assert_that(str(CardTransactionResult.DECLINED), is_("Declined"))

    def test_read_error(self) -> None:
        """Test Card Read Error."""
        assert_that(str(CardTransactionResult.READ_ERROR),
                    is_("Card Read Error"))

    def test_insufficient_funds(self) -> None:
        """Test Approved."""
        assert_that(str(CardTransactionResult.INSUFFICIENT_FUNDS),
                    is_("Insufficient Funds"))

    def test_incorrect_pin(self) -> None:
        """Test Approved."""
        assert_that(str(CardTransactionResult.INCORRECT_PIN),
                    is_("Incorrect PIN"))

    def test_enum_size(self) -> None:
        """Test size of enum."""
        assert_that(len(CardTransactionResult), is_(5))
