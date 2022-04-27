from models.abstract_model import Storage


class Shop(Storage):
    def __init__(self, unique_items_limit=5):
        super().__init__()
        self.capacity = 20
        self.unique_items_limit = unique_items_limit

    def add(self, name: str, count: int):
        """Пополняем помещение, если успех - возвращаем True"""
        if name in self.items:
            if self.total_count() + count <= self.capacity:  # сравниваем допустимое количество после добавления товара
                return True
            return False
        self.items[name] = count
        total_count = self.total_count()
        if total_count <= self.capacity:
            return True
        del self.items[name]
        return False

    def remove(self, name: str, count: int):
        if name not in self.items:
            return False
        if self.items[name] >= count:
            self.items[name] -= count
            return True
        return False

    def get_free_space(self):
        return self.capacity - self.total_count()

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        unique_items_count = 0
        for name in self.items:
            unique_items_count += 1
        return unique_items_count

    def total_count(self):
        total_count = 0
        for name, count in self.items.items():
            total_count += count
        return total_count
