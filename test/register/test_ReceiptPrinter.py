"""Test Receipt Printer.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from hamcrest.library.collection.issequence_containinginorder import (
    contains_exactly)
import pytest
from datetime import datetime
from unittest import mock
from cc410.register.ReceiptPrinter import ReceiptPrinter
from test.register.FakeDate import FakeDate


class TestReceiptPrinter():
    """Test Receipt Printer."""

    def test_start_receipt_throws_if_started(self) -> None:
        """Start receipt throws if already started."""
        with mock.patch('builtins.open', mock.mock_open()):
            printer: ReceiptPrinter = ReceiptPrinter()
            printer.start_receipt()
            with pytest.raises(RuntimeError) as e:
                printer.start_receipt()
            assert_that(str(e.value), "Receipt already started.")

    def test_print_line_throws_if_not_started(self) -> None:
        """Print line throws if not started."""
        with mock.patch('builtins.open', mock.mock_open()):
            printer: ReceiptPrinter = ReceiptPrinter()
            with pytest.raises(RuntimeError) as e:
                printer.print_line("")
            assert_that(str(e.value), "Receipt not started.")

    def test_print_line_throws_if_too_long(self) -> None:
        """Print line throws if line too long."""
        with mock.patch('builtins.open', mock.mock_open()):
            printer: ReceiptPrinter = ReceiptPrinter()
            printer.start_receipt()
            with pytest.raises(ValueError) as e:
                printer.print_line("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            assert_that(str(e.value), "Text longer than 40 characters.")

    def test_end_receipt_throws_if_not_started(self) -> None:
        """End receipt throws if not started."""
        with mock.patch('builtins.open', mock.mock_open()):
            printer: ReceiptPrinter = ReceiptPrinter()
            with pytest.raises(RuntimeError) as e:
                printer.end_receipt()
            assert_that(str(e.value), "Receipt not started.")

    def test_close_calls_close(self) -> None:
        """Test close method closes file."""
        with mock.patch('builtins.open', mock.mock_open()) as m:
            printer: ReceiptPrinter = ReceiptPrinter()
            printer.close()
            handle = m()
            assert_that(handle.close.called, is_(True))

    @mock.patch('cc410.register.ReceiptPrinter.datetime', FakeDate)
    def test_start_receipt_prints_correctly(self) -> None:
        """Start receipt prints correctly."""
        date = datetime(2001, 1, 1, 1, 1, 1)
        with mock.patch('builtins.open', mock.mock_open()) as m:
            FakeDate.now = classmethod(lambda cls: date)
            printer: ReceiptPrinter = ReceiptPrinter()
            printer.start_receipt()
        handle = m()
        call1 = mock.call("========================================\n")
        call2 = mock.call("*** RECEIPT START: 20010101-01:01:01 ***\n")
        assert_that(handle.write.mock_calls,
                    contains_exactly(call1, call2, call1))

    @mock.patch('cc410.register.ReceiptPrinter.datetime', FakeDate)
    def test_end_receipt_prints_correctly(self) -> None:
        """End receipt prints correctly."""
        date = datetime(2001, 1, 1, 1, 1, 1)
        with mock.patch('builtins.open', mock.mock_open()) as m:
            FakeDate.now = classmethod(lambda cls: date)
            printer: ReceiptPrinter = ReceiptPrinter()
            printer.start_receipt()
            printer.end_receipt()
        handle = m()
        call1 = mock.call("========================================\n")
        call3 = mock.call("**** RECEIPT END: 20010101-01:01:01 ****\n")
        assert_that(handle.write.mock_calls[3:],
                    contains_exactly(call1, call3, call1))

    def test_print_line_prints_correctly(self) -> None:
        """Print line prints correctly."""
        with mock.patch('builtins.open', mock.mock_open()) as m:
            printer: ReceiptPrinter = ReceiptPrinter()
            printer.start_receipt()
            printer.print_line("This is a test line.")
        handle = m()
        call1 = mock.call("This is a test line.\n")
        assert_that(handle.write.mock_calls[3:],
                    contains_exactly(call1))
