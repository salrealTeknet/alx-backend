#!/usr/bin/env python3
"""
Implementation of a server class to paginate a dataset
"""

from math import ceil
import csv
from typing import Dict, Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index range for list
    """
    return ((page_size * page) - page_size, (page_size * page))


class Server:
    """Server class for paginating database for popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        paginates dataset using index range and returns empty list if its 0
        """
        self.dataset()
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        startEnd = index_range(page, page_size)
        try:
            return self.__dataset[startEnd[0]: startEnd[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        this generates a dictionary with hypermedia information related
        pagination
        """
        hyper = {}
        try:
            curr_page = self.get_page(page, page_size)
        except AssertionError:
            curr_page = []

        if curr_page:
            hyper["page"] = page
            hyper["page_size"] = page_size
            hyper["data"] = curr_page
        else:
            hyper["page"] = page
            hyper["page_size"] = 0
            hyper["data"] = []

        try:
            next_page = self.get_page(page + 1, page_size)
        except AssertionError:
            next_page = []
        hyper["next_page"] = page + 1 if next_page else None

        try:
            prev_page = self.get_page(page - 1, page_size)
        except AssertionError:
            prev_page = []
        hyper["prev_page"] = page - 1 if (prev_page or page - 1 > 0) else None

        hyper["total_pages"] = ceil(len(self.__dataset) / page_size)
        return hyper
