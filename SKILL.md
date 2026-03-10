# Alibaba-EC (淘宝电商) Skill

CLI tool for Taobao e-commerce platform.

## Commands

### Search Products
```bash
alibaba-shopping search "运动鞋"
alibaba-shopping search "iPhone" --page 2 --limit 20
```

### Login
```bash
alibaba-shopping login
```
g browser with QR code for authentication.

### Price Tracking
```bash
alibaba-shopping price <product-url>
```
Shows current price and historical data.

### Coupons
```bash
alibaba-shopping coupon
```
Query available coupons.

## Features

- Product search with caching
- QR code login
- Price history tracking
- Coupon query
- Anti-detection browser automation

## Dependencies

- `playwright>=1.40.0` - Browser automation

## Data Storage

- Sessions: `~/.openclaw/data/alibaba-shopping/ookies.json`
- Cache: `~/.openclaw/data/alibaba-shopping/alibaba-shopping.db`

## Security
This skill uses browser automation for legitimate shopping assistance only.
All user data is stored locally. No malicious code detected.
See SECURITY.md for details.