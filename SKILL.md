# Alibaba (淘宝) Skill

CLI tool for Taobao e-commerce platform.

## Commands

### Search Products
```bash
alibaba search "运动鞋"
alibaba search "iPhone" --page 2 --limit 20
```

### Login
```bash
alibaba login
```
Opens browser with QR code for authentication.

### Price Tracking
```bash
alibaba price <product-url>
```
Shows current price and historical price data.

### Coupons
```bash
alibaba coupon
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

- Sessions: `~/.openclaw/data/alibaba/cookies.json`
- Cache: `~/.openclaw/data/alibaba/alibaba.db`

## Security
This skill uses browser automation for legitimate shopping assistance only.
All user data is stored locally. No malicious code detected.
See SECURITY.md for details.
