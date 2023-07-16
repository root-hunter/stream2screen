#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
from core.cli import get_args
from core.download import start

if __name__ == "__main__":
    args = get_args()

    asyncio.run(
        start(args=args, m3u8_url=args.input, output_folder=args.output_dir, key_url=args.key)
    )