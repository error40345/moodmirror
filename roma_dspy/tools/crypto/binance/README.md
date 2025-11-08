# Binance Toolkit for ROMA-DSPy

Clean, production-ready Binance cryptocurrency toolkit with full type safety and DSPy integration.

## Features

✅ **Multi-Market Support**
- Spot trading (immediate settlement)
- USDT-margined futures (USDⓈ-M)
- Coin-margined futures (COIN-M)

✅ **Type-Safe Value Objects**
- All prices use `Decimal` for precision
- Timestamps as `datetime` objects
- Pydantic models throughout

✅ **Optional Statistical Analysis**
- Enable via `enable_analysis: true`
- Volatility classification
- Volume ratings
- Price momentum indicators

✅ **Symbol Validation**
- Automatic symbol caching
- Fuzzy matching support
- User-defined symbol filters

## Architecture

```
value_objects/crypto/          # Generic crypto value objects
├── chains.py                  # BlockchainNetwork enums
├── currencies.py              # Fiat/Crypto currencies
├── intervals.py               # Time intervals
├── common.py                  # Base responses
└── trading.py                 # OHLCV, orderbook, trades

crypto/binance/                # Binance implementation
├── types.py                   # Binance-specific types
├── client.py                  # Low-level API client
└── toolkit.py                 # DSPy-compatible toolkit
```

## Available Tools

### 1. `get_current_price`
Get real-time price for a symbol.

```python
price = await toolkit.get_current_price("BTCUSDT", market="spot")
# Returns: {"success": true, "symbol": "BTCUSDT", "price": "50000.00", ...}
```

### 2. `get_ticker_stats`
Get 24-hour statistics (price change, volume, high/low).

```python
stats = await toolkit.get_ticker_stats("BTCUSDT")
# Returns: {
#   "success": true,
#   "price_change_percent": "5.23",
#   "volume": "12345.67",
#   "trend": "bullish",
#   "analysis": {...}  # If enable_analysis=true
# }
```

### 3. `get_order_book`
Get market depth (bids/asks).

```python
book = await toolkit.get_order_book("BTCUSDT", limit=100)
# Returns: {
#   "success": true,
#   "best_bid": "49999.99",
#   "best_ask": "50000.01",
#   "spread": "0.02",
#   ...
# }
```

### 4. `get_recent_trades`
Get recent trade history.

```python
trades = await toolkit.get_recent_trades("BTCUSDT", limit=100)
# Returns: {
#   "success": true,
#   "trades_count": 100,
#   "latest_price": "50000.00",
#   ...
# }
```

### 5. `get_klines`
Get candlestick (OHLCV) data.

```python
candles = await toolkit.get_klines("BTCUSDT", interval="1h", limit=24)
# Returns: {
#   "success": true,
#   "count": 24,
#   "trend": "bullish",
#   "analysis": {...}  # If enable_analysis=true
# }
```

### 6. `get_book_ticker`
Get best bid/ask with spread.

```python
ticker = await toolkit.get_book_ticker("BTCUSDT")
# Returns: {
#   "success": true,
#   "bid_price": "49999.99",
#   "ask_price": "50000.01",
#   "spread": "0.02",
#   "spread_percent": "0.0004",
#   ...
# }
```

## Configuration

### Basic Configuration

```yaml
toolkits:
  - class_name: "BinanceToolkit"
    enabled: true
    toolkit_config:
      symbols: ["BTCUSDT", "ETHUSDT"]
      default_market: "spot"
```

### With Analysis Enabled

```yaml
toolkits:
  - class_name: "BinanceToolkit"
    enabled: true
    toolkit_config:
      symbols: ["BTCUSDT", "ETHUSDT"]
      default_market: "spot"
      enable_analysis: true  # Adds statistical analysis to responses
```

### Multi-Market Setup

```yaml
toolkits:
  # Spot market
  - class_name: "BinanceToolkit"
    enabled: true
    toolkit_config:
      default_market: "spot"

  # Futures market
  - class_name: "BinanceToolkit"
    enabled: true
    toolkit_config:
      default_market: "usdm"  # USDT-margined futures
```

### With Authentication (Private Endpoints)

```yaml
toolkits:
  - class_name: "BinanceToolkit"
    enabled: true
    toolkit_config:
      api_key: "${BINANCE_API_KEY}"
      api_secret: "${BINANCE_API_SECRET}"
      default_market: "spot"
```

## Value Objects

All responses use type-safe Pydantic models:

### OrderBookSnapshot
```python
from src.roma_dspy.tools.value_objects.crypto import OrderBookSnapshot

book: OrderBookSnapshot
book.best_bid  # OrderBookLevel with price/quantity
book.best_ask  # OrderBookLevel with price/quantity
book.spread    # Decimal (ask - bid)
book.mid_price # Decimal ((bid + ask) / 2)
```

### Kline (Candlestick)
```python
from src.roma_dspy.tools.value_objects.crypto import Kline

kline: Kline
kline.open      # Decimal
kline.high      # Decimal
kline.low       # Decimal
kline.close     # Decimal
kline.volume    # Decimal
kline.is_bullish      # bool (close > open)
kline.body_size       # Decimal
kline.wick_high       # Decimal
```

### TickerStats
```python
from src.roma_dspy.tools.value_objects.crypto import TickerStats

ticker: TickerStats
ticker.price_change_percent  # Decimal
ticker.volume                # Decimal
ticker.high_price            # Decimal
ticker.low_price             # Decimal
ticker.trend                 # TrendDirection enum
```

## Analysis Features

When `enable_analysis: true`:

### Volatility Classification
- **low**: < 2% change
- **moderate**: 2-5% change
- **high**: 5-10% change
- **extreme**: > 10% change

### Volume Rating
- **low**: < 100
- **moderate**: 100-1,000
- **high**: 1,000-10,000
- **very_high**: > 10,000

### Price Momentum
- **positive**: Price increasing
- **negative**: Price decreasing
- **neutral**: Price stable

## Error Handling

All tools return consistent error format:

```python
{
    "success": false,
    "error": "Error message",
    "symbol": "BTCUSDT"
}
```

## Type Safety

✅ All numeric values → `Decimal` (no float precision issues)
✅ All timestamps → `datetime` objects
✅ All enums → strongly typed
✅ Full Pydantic validation

## Testing

```python
# Test imports
from src.roma_dspy.tools import BinanceToolkit
from src.roma_dspy.tools.value_objects.crypto import OrderBookSnapshot

# Initialize toolkit
toolkit = BinanceToolkit(
    symbols=["BTCUSDT"],
    default_market="spot",
    enable_analysis=True
)

# Use async context manager
async with toolkit:
    price = await toolkit.get_current_price("BTCUSDT")
    print(price)
```

## Extensibility

The generic `value_objects/crypto/` are reusable for:
- CoinGecko toolkit
- DefiLlama toolkit
- Arkham toolkit
- Any crypto data source

Same patterns, same types, consistent behavior across all crypto toolkits.