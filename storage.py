from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    @abstractmethod
    def add(self, title, qnt):
        pass

    @abstractmethod
    def remove(self, title, qnt):
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
