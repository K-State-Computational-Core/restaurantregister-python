"""Fake date class for testing.

See https://williambert.online/2011/07/
how-to-unit-testing-in-django-with-mocking-and-patching/
"""
from datetime import datetime


class FakeDate(datetime):
    """Fake date class for testing."""

    def __new__(cls, *args, **kwargs):
        """Return parent type."""
        return datetime.__new__(datetime, *args, **kwargs)
