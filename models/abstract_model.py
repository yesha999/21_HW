from abc import ABC, abstractmethod
from collections import defaultdict


class Storage(ABC):
    def __init__(self):
        self.items = defaultdict(int)
        self.capacity = 0

    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
