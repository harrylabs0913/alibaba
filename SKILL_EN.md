---
name: alibaba-ec
description: "CLI tool for Taobao/Alibaba e-commerce platform - search products, track prices, and manage authentication"
---

# Alibaba (Taobao) Skill

A command-line interface for Taobao (淘宝/阿里巴巴), China's largest C2C e-commerce platform. This skill provides comprehensive access to product search, price history tracking, and authentication management.

## Description

Alibaba is a powerful CLI tool designed for interacting with the Taobao e-commerce ecosystem. It enables automated product searches with intelligent caching, detailed price history analysis, and secure QR code-based authentication. The platform offers an enormous selection of products from millions of merchants, making it ideal for price research, product discovery, and competitive analysis.

### Use Cases

- **Product Discovery**: Find products across Taobao's vast marketplace
- **Price Analysis**: Track historical pricing to identify buying opportunities
- **Coupon Management**: Query and manage available coupons
- **Market Intelligence**: Gather competitive pricing information

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install browser
playwright install chromium
```

## Usage

### Commands

#### Search Products
```bash
alibaba search "运动鞋"
alibaba search "iPhone" --page 2 --limit 20
```

Search for products by keyword with pagination support.

- **Arguments:**
  - `query` - Search keyword (required)
  - `--page` - Page number (default: 1)
  - `--limit` - Number of results per page (default: 20)

**Example:**
```bash
# Basic search
alibaba search "wireless earbuds"

# Paginated search
alibaba search "coffee maker" --page 5 --limit 30
```

#### Login
```bash
alibaba login
```

Authenticate with Taobao using QR code. Opens a browser window with a QR code that can be scanned with the Taobao/Alipay mobile app. Session tokens are securely stored for future use.

#### Price Tracking
```bash
alibaba price <product-url>
```

Display current price and historical price data for a specific product.

- **Arguments:**
  - `product-url` - Full Taobao product URL (required)

**Example:**
```bash
alibaba price "https://item.taobao.com/item.htm?id=123456789"
```

#### Coupons
```bash
alibaba coupon
```

Query available coupons from the platform.

## Features

- **Product Search with Caching**: Intelligent caching system for fast repeated searches and reduced API load
- **QR Code Login**: Secure and convenient authentication via mobile app QR code scanning
- **Price History Tracking**: Comprehensive historical price data to identify trends and optimal purchase timing
- **Coupon Query**: Access available coupons and promotions
- **Anti-Detection Browser Automation**: Stealth automation that mimics human interaction patterns
- **Session Persistence**: Long-lived authentication tokens for uninterrupted access

## Examples

### Product Search
```bash
# Search for electronics
alibaba search "iPhone 15 Pro"

# Search with custom results
alibaba search "running shoes" --page 2 --limit 50
```

### Price Analysis
```bash
# Get price history
alibaba price "https://item.taobao.com/item.htm?id=687543210"

# Check historical low price
alibaba price "https://item.taobao.com/item.htm?id=123456" | grep -i "lowest"
```

### Coupon Query
```bash
# List available coupons
alibaba coupon
```

### Authentication Setup
```bash
# First-time login
alibaba login
# Scan QR code with Taobao app
```

## Technical Details

### Data Storage

| Data Type | Location |
|-----------|----------|
| Session Tokens | `~/.openclaw/data/alibaba/cookies.json` |
| Search Cache | `~/.openclaw/data/alibaba/alibaba.db` |

### Dependencies

- `playwright>=1.40.0` - Browser automation
- SQLite for data persistence

### Platform Notes

Taobao operates as a C2C (Consumer-to-Consumer) platform with:
- Millions of individual sellers
- Diverse product categories
- Competitive pricing through negotiation
- Integrated with Alipay for payments

### Anti-Detection Implementation

All browser automation includes:
- Randomized timing between actions
- Human-like mouse movements and clicks
- Realistic navigation patterns
- Session fingerprint management
