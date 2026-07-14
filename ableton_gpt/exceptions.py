"""Exception types for AbletonGPT."""

from __future__ import annotations


class AbletonGPTError(Exception):
    """Base exception for AbletonGPT."""


class ConfigurationError(AbletonGPTError):
    """Raised for invalid configuration."""
