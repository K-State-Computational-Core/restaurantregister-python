"""Class to print a receipt.

Typical usage is to instantiate a receipt printer along with the application.

To print a receipt, call the `startReceipt()` method first, then print each
line using the `printLine()` method. Each line on the receipt must be no longer
than 40 characters. Newlines will be inserted by the class. Finally, call
`endReceipt()` to finalize the receipt before starting a new one.

The `close()` method should be called when the application is closed.

Any Exception thrown by the underlying file object will be thrown.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from typing import TextIO
from datetime import datetime


class ReceiptPrinter:
    """Class to print a receipt."""

    def __init__(self) -> None:
        """Constructor."""
        self.__writer: TextIO = open("receipt.txt", "a")
        self.__started: bool = False

    def start_receipt(self) -> None:
        """Start printing a receipt.

        Raises:
            RuntimeError: if the receipt is already started
        """
        if self.__started:
            raise RuntimeError("Receipt already started.")
        self.__started = True
        self.__writer.write("========================================\n")
        self.__writer.write("*** RECEIPT START: {} ***\n".
                            format(datetime.now().strftime("%Y%m%d-%H:%M:%S")))
        self.__writer.write("========================================\n")

    def print_line(self, text: str) -> None:
        """Add a line to the receipt.

        Args:
            text: the line to print

        Raises:
            ValueError: if the text is longer than 40 characters
            RuntimeError: if the receipt is not started
        """
        if not self.__started:
            raise RuntimeError("Receipt not started.")
        if len(text) > 40:
            raise ValueError("Test longer than 40 characters.")
        self.__writer.write("{}\n".format(text))

    def end_receipt(self) -> None:
        """Ends a receipt.

        Raises:
            RuntimeError: if the receipt is not started
        """
        if not self.__started:
            raise RuntimeError("Receipt not started.")
        self.__started = False
        self.__writer.write("========================================\n")
        self.__writer.write("**** RECEIPT END: {} ****\n".
                            format(datetime.now().strftime("%Y%m%d-%H:%M:%S")))
        self.__writer.write("========================================\n")
        self.__writer.flush()

    def close(self) -> None:
        """Closes the file."""
        self.__writer.close()
