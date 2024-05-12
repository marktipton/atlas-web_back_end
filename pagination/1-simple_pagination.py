import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
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
        """return page of dataset corresponding to page count and size"""
        assert page > 0 and isinstance (page, int), "page is positive int"
        assert page_size > 0 and isinstance (page_size, int), "is pos int"



    def index_range(page, page_size):
        """return start index and end index for pagination"""
        start_index = (page - 1) * page_size
        end_index = page * page_size
        return (start_index, end_index)
