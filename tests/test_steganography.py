"""Tests for steganography."""

import pytest
from steganography import steganography


class TestSteganography:
    """Test suite for steganography."""

    def test_basic(self):
        """Test basic usage."""
        result = steganography("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            steganography("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = steganography(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
