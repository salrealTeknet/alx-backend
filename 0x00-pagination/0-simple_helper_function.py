#!/usr/bin/env python3
"""
function to calculate start and end indexes
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    range of pages required
    """
    return ((page_size * page) - page_size, (page_size * page))
