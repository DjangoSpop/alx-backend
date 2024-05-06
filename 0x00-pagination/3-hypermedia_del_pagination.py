import csv
import math
from typing import Dict, List
import os
cwd = os.getcwd
file_path = os.path.join(cwd,'C:\Users\ahmed el bahi\alx-backend\0x00-pagination\Popular_Baby_Names.csv', 'Popular_Baby_Names.csv' )

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing hypermedia pagination information based on an index.
        
        Args:
            index (int, optional): The starting index of the page. Defaults to None.
            page_size (int, optional): The number of items per page. Defaults to 10.
            
        Returns:
            Dict: A dictionary containing hypermedia pagination information.
        """
        data = []
        indexed_dataset = self.indexed_dataset()
        next_index = index + page_size if index + page_size < len(indexed_dataset) else None

        if index is None:
            index = 0

        assert 0 <= index < len(indexed_dataset), "Index out of range"

        for i in range(index, index + page_size):
            if i in indexed_dataset:
                data.append(indexed_dataset[i])

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }