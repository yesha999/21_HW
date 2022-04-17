class Request:
    def __init__(self, product, amount, from_, to):
        self.product = product
        self.amount = amount
        self.from_ = from_
        self.to = to

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'
