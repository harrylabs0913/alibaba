#!/usr/bin/env python3
"""淘宝/阿里巴巴CLI入口"""
import sys
from alibaba import main
import asyncio

if __name__ == "__main__":
    asyncio.run(main())
