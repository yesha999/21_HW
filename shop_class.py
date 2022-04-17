from abstract_class import Storage


class Shop(Storage):
    def __init__(self, unique_items_limit=5):
        super().__init__()
        self.capacity = 20
        self.unique_items_limit = unique_items_limit

    def add(self, name: str, count: int):
        if name in self.items:
            old_count = self.items[name]
            self.items[name] += count
            total_count = self.total_count()
            if total_count <= self.capacity:
                return True, f'Товар {name} в количестве {count} успешно добавлен в магазин'
            else:
                self.items[name] = old_count
                return False, f'Товар {name} в количестве {count} не может быть добавлен,' \
                              f' осталось места: {self.get_free_space()}.'
        else:
            unique_items_count = self.get_unique_items_count()
            if unique_items_count >= self.unique_items_limit:
                return False, f'Товар {name} в количестве {count} не может быть добавлен,' \
                              f' превышен лимит уникальных товаров ({self.unique_items_limit}).'
            self.items[name] = count
            total_count = self.total_count()
            if total_count <= self.capacity:
                return True, f'Товар {name} в количестве {count} успешно добавлен в магазин'
            else:
                del self.items[name]
                return False, f'Товар {name} в количестве {count} не может быть добавлен,' \
                              f' осталось места: {self.get_free_space()}.'

    def remove(self, name: str, count: int):
        if name not in self.items:
            return False, f'Товар {name} не найден в магазине'

        if self.items[name] >= count:
            self.items[name] -= count
            return True, f'Товар {name} в количестве {count} успешно отгружен из магазина.'
        else:
            return False, f'В магазине нет товара {name} в количестве {count}, {name} в магазине: {self.items[name]}.'

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
