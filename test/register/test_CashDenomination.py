"""Test Cash Denomination.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from hamcrest.library.number.iscloseto import close_to
from cc410.register.CashDenomination import CashDenomination


class TestCashDenomination():
    """Test Cash Denomination."""

    def test_penny(self) -> None:
        """Test Penny."""
        assert_that(str(CashDenomination.PENNY), is_("Penny"))
        assert_that(CashDenomination.PENNY.amount,
                    close_to(0.01, 0.00001))

    def test_nickel(self) -> None:
        """Test Nickel."""
        assert_that(str(CashDenomination.NICKEL), is_("Nickel"))
        assert_that(CashDenomination.NICKEL.amount,
                    close_to(0.05, 0.00001))

    def test_dime(self) -> None:
        """Test Dime."""
        assert_that(str(CashDenomination.DIME), is_("Dime"))
        assert_that(CashDenomination.DIME.amount,
                    close_to(0.10, 0.00001))

    def test_quarter(self) -> None:
        """Test Quarter."""
        assert_that(str(CashDenomination.QUARTER), is_("Quarter"))
        assert_that(CashDenomination.QUARTER.amount,
                    close_to(0.25, 0.00001))

    def test_half_dollar(self) -> None:
        """Test Half Dollar."""
        assert_that(str(CashDenomination.HALF_DOLLAR), is_("Half Dollar"))
        assert_that(CashDenomination.HALF_DOLLAR.amount,
                    close_to(0.50, 0.00001))

    def test_dollar_coin(self) -> None:
        """Test Dollar Coin."""
        assert_that(str(CashDenomination.DOLLAR_COIN), is_("Dollar Coin"))
        assert_that(CashDenomination.DOLLAR_COIN.amount,
                    close_to(1.0, 0.00001))

    def test_one_dollar_bill(self) -> None:
        """Test One Dollar Bill."""
        assert_that(str(CashDenomination.ONE_DOLLAR_BILL), is_("$1 Bill"))
        assert_that(CashDenomination.ONE_DOLLAR_BILL.amount,
                    close_to(1.0, 0.00001))

    def test_five_dollar_bill(self) -> None:
        """Test Five Dollar Bill."""
        assert_that(str(CashDenomination.FIVE_DOLLAR_BILL), is_("$5 Bill"))
        assert_that(CashDenomination.FIVE_DOLLAR_BILL.amount,
                    close_to(5.0, 0.00001))

    def test_ten_dollar_bill(self) -> None:
        """Test Ten Dollar Bill."""
        assert_that(str(CashDenomination.TEN_DOLLAR_BILL), is_("$10 Bill"))
        assert_that(CashDenomination.TEN_DOLLAR_BILL.amount,
                    close_to(10.0, 0.00001))

    def test_twenty_dollar_bill(self) -> None:
        """Test Twenty Dollar Bill."""
        assert_that(str(CashDenomination.TWENTY_DOLLAR_BILL), is_("$20 Bill"))
        assert_that(CashDenomination.TWENTY_DOLLAR_BILL.amount,
                    close_to(20.0, 0.00001))

    def test_fifty_dollar_bill(self) -> None:
        """Test Fifty Dollar Bill."""
        assert_that(str(CashDenomination.FIFTY_DOLLAR_BILL), is_("$50 Bill"))
        assert_that(CashDenomination.FIFTY_DOLLAR_BILL.amount,
                    close_to(50.0, 0.00001))

    def test_hundred_dollar_bill(self) -> None:
        """Test Hundred Dollar Bill."""
        assert_that(str(CashDenomination.HUNDRED_DOLLAR_BILL),
                    is_("$100 Bill"))
        assert_that(CashDenomination.HUNDRED_DOLLAR_BILL.amount,
                    close_to(100.0, 0.00001))

    def test_enum_size(self) -> None:
        """Test size of enum."""
        assert_that(len(CashDenomination), is_(12))
