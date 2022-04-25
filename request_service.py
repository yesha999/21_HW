class Request:
    def __init__(self, product_name, product_amount, from_, to):
        self.product_name = product_name
        self.product_amount = product_amount
        self.from_ = from_
        self.to = to

    def __repr__(self):
        return f'Доставить {self.product_amount} {self.product_name} из {self.from_} в {self.to}'
