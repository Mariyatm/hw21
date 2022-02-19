from storage import Storage


class Store(Storage):
    def __init__(self, items, capacity=100, name="склад"):
        self.name = name
        super().__init__(items, capacity)

    def add(self, title, qnt):
        if self.can_add(title, qnt):
            if title in self.items:
                self.items[title] += qnt
            else:
                self.items[title] = qnt

    def can_add(self, title, qnt):
        if qnt <= self.get_free_space():
            return True
        return False

    def remove(self, title, qnt):
        qnt_fact = min(qnt, self.items[title])
        self.items[title] -= qnt_fact

    def get_free_space(self):
        return self.capacity - sum(qnt for qnt in self.items.values())

    def get_items(self):
        return self.items

    def get_item(self, title):
        return self.items.get(title, 0)

    def get_unique_items_count(self):
        return len(self.items)

    def __repr__(self):
        res = f"В {self.name}е хранится:\n"
        for item in self.items:
            res += f"{self.items[item]} {item} \n"
        res += "\n"
        return res
