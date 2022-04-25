from request_service import Request
from models.shop_model import Shop
from models.store_model import Store


def add_func(place_where_receipt):
    is_success = place_where_receipt.add(request.product_name, request.product_amount)
    if is_success:
        print(f'Товар {product_name} в количестве {product_amount} успешно добавлен в {to_} ')
    if not is_success:
        print(f'Товар {product_name} в количестве {product_amount} не может быть добавлен,'
              f' осталось места: {place_where_receipt.get_free_space()}.')
    return is_success


def remove_func(place_where_shipment):
    is_success = place_where_shipment.remove(request.product_name, request.product_amount)
    if is_success:
        print(f'Товар {product_name} в количестве {product_amount} успешно отгружен с {from_}.')
    if not is_success:
        print(f'На складе нет товара {product_name} в количестве {product_amount},'
              f' {product_name} на складе: {place_where_shipment.items[product_name]}.')
    return is_success


if __name__ == "__main__":

    store = Store()
    shop = Shop()
    while True:
        product_name = input('Введите наименование товара, который необходимо доставить: ').lower()
        if product_name == 'stop':
            break

        while True:
            product_amount = None
            try:
                product_amount = int(input('Введите количество доставляемого товара: '))
            except:
                'Введите число'
            if product_amount:
                break

        from_ = input('Откуда? (в именительном падеже): ')
        to_ = input('Куда? (в именительном падеже): ')

        request = Request(product_name, product_amount, from_, to_)
        print(request)

        if from_ == 'склад':
            from_place = store
            is_success = add_func(from_place)
            if not is_success:
                continue

        if from_ == 'магазин':
            from_place = shop
            is_success = add_func(from_place)
            if not is_success:
                continue

        if to_ == 'склад':
            to_place = store
            is_success = add_func(to_place)
            if not is_success:
                continue

        elif to_ == 'магазин':
            to_place = shop
            is_success = add_func(to_place)
            if not is_success:
                continue
