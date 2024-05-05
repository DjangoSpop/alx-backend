import csv
from typing import List

index_range = __import__('0-simple_helper_function.py')

class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset.

        Returns:
            List[List]: The dataset containing popular baby names.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a specific page of the dataset.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of records per page. Defaults to 10.

        Returns:
            List[List]: The records in the specified page.
        """        
        assert page > 0 
        assert page_size > 0
        self.dataset()
        start, end = self.index_range(page, page_size)
        if start >= len(self.__dataset):
            return []
        return self.__dataset[start:end]
