"""Type definitions for DefiLlama API."""

from __future__ import annotations

from decimal import Decimal
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class DataType(str, Enum):
    """Data types for fee/revenue endpoints."""

    DAILY_FEES = "dailyFees"
    DAILY_REVENUE = "dailyRevenue"
    DAILY_HOLDERS_REVENUE = "dailyHoldersRevenue"


class ProtocolInfo(BaseModel):
    """Protocol information model."""

    id: str
    name: str
    symbol: Optional[str] = None
    category: Optional[str] = None
    chains: List[str] = Field(default_factory=list)
    tvl: Decimal
    chain_tvls: dict = Field(default_factory=dict, alias="chainTvls")
    change_1d: Optional[Decimal] = None
    change_7d: Optional[Decimal] = None
    mcap: Optional[Decimal] = None

    class Config:
        populate_by_name = True


class ProtocolFees(BaseModel):
    """Protocol fees data model."""

    id: str
    name: str
    total24h: Optional[Decimal] = None
    total7d: Optional[Decimal] = None
    total_all_time: Optional[Decimal] = Field(None, alias="totalAllTime")
    change_1d: Optional[Decimal] = None
    chains: List[str] = Field(default_factory=list)
    total_data_chart: List[List] = Field(default_factory=list, alias="totalDataChart")

    class Config:
        populate_by_name = True


class YieldPool(BaseModel):
    """Yield pool data model."""

    pool_id: str = Field(alias="pool")
    chain: str
    project: str
    symbol: str
    apy: Optional[Decimal] = None
    apy_base: Optional[Decimal] = Field(None, alias="apyBase")
    apy_reward: Optional[Decimal] = Field(None, alias="apyReward")
    tvl_usd: Optional[Decimal] = Field(None, alias="tvlUsd")
    underlying_tokens: List[str] = Field(default_factory=list, alias="underlyingTokens")

    class Config:
        populate_by_name = True


class TVLDataPoint(BaseModel):
    """Single TVL data point."""

    date: int = Field(description="Unix timestamp")
    total_liquidity_usd: Decimal = Field(alias="totalLiquidityUSD")

    class Config:
        populate_by_name = True
