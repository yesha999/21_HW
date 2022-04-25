from models.abstract_model import Storage


class Store(Storage):
    def __init__(self):
        super().__init__()
        self.capacity = 100

    def add(self, name: str, count: int):
        """Пояснение к некоторой логике функции: если товар уже есть на складе, мы запоминаем
         сколько было, добавляем нужное количество, если оно превышает лимит, возвращаем сколько было"""
        if name in self.items:
            old_count = self.items[name] # запоминаем сколько было товара до добавления
            self.items[name] += count
            total_count = self.total_count()
            if total_count <= self.capacity: # сравниваем допустимое количество после добавления товара
                return True
            else:
                self.items[name] = old_count # в случае ошибки возвращаем как было
                return False
        else:
            self.items[name] = count
            total_count = self.total_count()
            if total_count <= self.capacity:
                return True
            else:
                del self.items[name]
                return False


    def remove(self, name: str, count: int):
        if name not in self.items:
            return False

        if self.items[name] >= count:
            self.items[name] -= count
            return True
        else:
            return False



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
