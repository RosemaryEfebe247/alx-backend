#!/usr/bin/env python3
"""a function named index_range that takes two integer
Arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns
    tuple of size two containing a start index and an end index
    """
    if page < 1 or page_size < 1:
        return None  # Invalid input
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
