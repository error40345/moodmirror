"""Arkham Intelligence blockchain analytics toolkit.

Provides access to Arkham Intelligence APIs for on-chain intelligence,
token analysis, wallet tracking, and entity attribution.
"""

from .client import ArkhamAPIClient, ArkhamAPIError
from .toolkit import ArkhamToolkit
from .types import TokenBalance, TokenFlow, TokenHolder, Transfer

# Import shared value objects for convenience
from roma_dspy.tools.value_objects.crypto import (
    AssetIdentifier,
    BlockchainNetwork,
)

__all__ = [
    # Main toolkit
    "ArkhamToolkit",
    # Client and errors
    "ArkhamAPIClient",
    "ArkhamAPIError",
    # Arkham-specific types
    "TokenHolder",
    "TokenFlow",
    "Transfer",
    "TokenBalance",
    # Shared value objects (for convenience)
    "BlockchainNetwork",
    "AssetIdentifier",
]
