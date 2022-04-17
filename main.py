from request_service import Request
from shop_class import Shop
from store_class import Store

if __name__ == "__main__":

    store = Store()
    shop = Shop()
    while True:
        product = input('Введите наименование товара, который необходимо доставить: ')
        if product == 'STOP':
            break

        while True:
            amount = None
            try:
                amount = int(input('Введите количество доставляемого товара: '))
            except:
                'Введите число'
            if amount:
                break

        from_ = input('Откуда? (в именительном падеже): ')
        to = input('Куда? (в именительном падеже): ')

        request = Request(product, amount, from_, to)
        print(request)

        if from_ == 'склад':
            success, answer = store.remove(request.product, request.amount)
            print(answer)
            if success is False:
                continue

        if from_ == 'магазин':
            success, answer = shop.remove(request.product, request.amount)
            print(answer)
            if success is False:
                continue

        if to == 'склад':
            success, answer = store.add(request.product, request.amount)
            print(answer)
            if success is False:
                if from_ == 'склад':
                    success, answer = store.add(request.product, request.amount)

                if from_ == 'магазин':
                    success, answer = shop.add(request.product, request.amount)
                continue

        if to == 'магазин':
            success, answer = shop.add(request.product, request.amount)
            print(answer)
            if success is False:
                if from_ == 'склад':
                    success, answer = store.add(request.product, request.amount)

                if from_ == 'магазин':
                    success, answer = shop.add(request.product, request.amount)
                continue
