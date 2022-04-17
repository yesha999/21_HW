from abstract_class import Storage


class Store(Storage):
    def __init__(self):
        super().__init__()
        self.capacity = 100

    def add(self, name: str, count: int):
        """Пояснение к некоторой логике функции: если товар уже есть на складе, мы запоминаем
         сколько было, добавляем нужное количество, если оно превышает лимит, возвращаем сколько было"""
        if name in self.items:
            old_count = self.items[name]
            self.items[name] += count
            total_count = self.total_count()
            if total_count <= self.capacity:
                return True, f'Товар {name} в количестве {count} успешно добавлен на склад'
            else:
                self.items[name] = old_count
                return False, f'Товар {name} в количестве {count} не может быть добавлен,' \
                              f' осталось места: {self.get_free_space()}.'
        else:
            self.items[name] = count
            total_count = self.total_count()
            if total_count <= self.capacity:
                return True, f'Товар {name} в количестве {count} успешно добавлен на склад'
            else:
                del self.items[name]
                return False, f'Товар {name} в количестве {count} не может быть добавлен,' \
                              f' осталось места: {self.get_free_space()}.'

    def remove(self, name: str, count: int):
        if name not in self.items:
            return False, f'Товар {name} не найден на складе'

        if self.items[name] >= count:
            self.items[name] -= count
            return True, f'Товар {name} в количестве {count} успешно отгружен со склада.'
        else:
            return False, f'На складе нет товара {name} в количестве {count}, {name} на складе: {self.items[name]}.'

    def get_free_space(self):
        return self.capacity - self.total_count()

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())

    def total_count(self):
        total_count = 0
        for name, count in self.items.items():
            total_count += count
        return total_count
