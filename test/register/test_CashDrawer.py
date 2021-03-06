"""Test Cash Drawer.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from hamcrest.library.number.iscloseto import close_to
import pytest
from cc410.register.CashDrawer import CashDrawer
from cc410.register.CashDenomination import CashDenomination


class TestCashDrawer():
    """Test Cash Drawer."""

    def test_constructor_populates_drawer(self) -> None:
        """Test constructor."""
        drawer: CashDrawer = CashDrawer()
        for denom in CashDenomination:
            assert_that(drawer.get_count(denom), is_(10))

    def test_total_initially_correct(self) -> None:
        """Test total method."""
        drawer: CashDrawer = CashDrawer()
        total: float = 0.0
        for denom in CashDenomination:
            total += denom.amount
        assert_that(total, is_(187.91))
        assert_that(drawer.get_total(), is_(10 * total))

    def test_must_open_drawer_to_modify(self) -> None:
        """Test must open drawer to modify."""
        drawer: CashDrawer = CashDrawer()
        with pytest.raises(RuntimeError) as e:
            drawer.add_count(CashDenomination.PENNY, 1)
        assert_that(str(e.value), is_("Cash drawer must be open to modify."))
        with pytest.raises(RuntimeError) as e:
            drawer.remove_count(CashDenomination.PENNY, 1)
        assert_that(str(e.value), is_("Cash drawer must be open to modify."))

    def test_must_close_drawer_to_count(self) -> None:
        """Test must close drawer to count."""
        drawer: CashDrawer = CashDrawer()
        drawer.open(0.0)
        with pytest.raises(RuntimeError) as e:
            drawer.get_count(CashDenomination.PENNY)
        assert_that(str(e.value), is_("Cash drawer must be closed to count."))
        with pytest.raises(RuntimeError) as e:
            drawer.get_total()
        assert_that(str(e.value), is_("Cash drawer must be closed to count."))

    def test_open_drawer_amount_negative(self) -> None:
        """Open drawer amount must not be negative."""
        drawer: CashDrawer = CashDrawer()
        with pytest.raises(ValueError) as e:
            drawer.open(-0.01)
        assert_that(str(e.value), is_("Amount must not be negative."))

    def test_add_count_negative(self) -> None:
        """Add Count must not be negative."""
        drawer: CashDrawer = CashDrawer()
        drawer.open(0.0)
        with pytest.raises(ValueError) as e:
            drawer.add_count(CashDenomination.PENNY, -1)
        assert_that(str(e.value), is_("Count must not be negative."))

    def test_remove_count_negative(self) -> None:
        """Remove Count must not be negative."""
        drawer: CashDrawer = CashDrawer()
        drawer.open(0.0)
        with pytest.raises(ValueError) as e:
            drawer.remove_count(CashDenomination.PENNY, -1)
        assert_that(str(e.value), is_("Count must not be negative."))

    def test_cash_amount_changed_balance(self) -> None:
        """Cash amount changed must balance."""
        drawer: CashDrawer = CashDrawer()
        total: float = drawer.get_total()
        drawer.open(187.91)
        for denom in CashDenomination:
            drawer.add_count(denom, 1)
        try:
            drawer.close()
            assert_that(drawer.get_total(), close_to(total + 187.91, 0.001))
        except Exception:
            pytest.fail("Unexpected Exception when closing drawer")

    def test_cash_amount_changed_make_change(self) -> None:
        """Cash amount changed must balance with change given."""
        drawer: CashDrawer = CashDrawer()
        total: float = drawer.get_total()
        drawer.open(187.91)
        cash_in: float = 200.0
        drawer.add_count(CashDenomination.HUNDRED_DOLLAR_BILL, 2)
        cash_in -= 0.01 * 4
        drawer.remove_count(CashDenomination.PENNY, 4)
        cash_in -= 0.05 * 1
        drawer.remove_count(CashDenomination.NICKEL, 1)
        cash_in -= 1.0 * 1
        drawer.remove_count(CashDenomination.DOLLAR_COIN, 1)
        cash_in -= 1.0 * 1
        drawer.remove_count(CashDenomination.ONE_DOLLAR_BILL, 1)
        cash_in -= 10.0 * 1
        drawer.remove_count(CashDenomination.TEN_DOLLAR_BILL, 1)
        assert_that(cash_in, close_to(187.91, 0.001))
        try:
            drawer.close()
            assert_that(drawer.get_total(), close_to(total + 187.91, 0.001))
        except Exception:
            pytest.fail("Unexpected Exception when closing drawer")

    def test_cash_amount_changed_wrong_throws(self) -> None:
        """Cash amount changed will throw exception when incorrect."""
        drawer: CashDrawer = CashDrawer()
        drawer.open(187.91)
        for denom in CashDenomination:
            drawer.add_count(denom, 1)
        drawer.add_count(CashDenomination.PENNY, 1)
        with pytest.raises(RuntimeError) as e:
            drawer.close()
        assert_that(str(e.value), is_("Cash drawer contents incorrect."))

    def test_remove_too_many_throws_exception(self) -> None:
        """Removing too many should throw exception."""
        drawer: CashDrawer = CashDrawer()
        drawer.open(0.0)
        for denom in CashDenomination:
            with pytest.raises(ValueError) as e:
                drawer.remove_count(denom, 11)
            assert_that(str(e.value),
                        is_("Cannot remove more than are present."))
