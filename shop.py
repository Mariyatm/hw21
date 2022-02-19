from store import Store


class Shop(Store):
    def __init__(self, items, capacity=20, name="магазин"):
        super().__init__(items, capacity, name)

    def can_add(self, title, qnt):
        if qnt <= self.get_free_space() and self.get_unique_items_count() < 5:
            return True
        return False
