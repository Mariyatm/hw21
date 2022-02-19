from store import Store
from shop import Shop
from request import Request


store = Store({"конфета":20, "маска": 10, "молоко":7, "мандарин":20})
shop =  Shop({"конфета": 5, "маска": 5})

requests = ["Доставить 8 конфета из склад в магазин",
            "Доставить 2 маска из магазин в склад",
            "Доставить 3 мандарин из склад в магазин"]

for str_request in requests:
    request = Request(str_request)
    if request.from_ == "магазин" and request.to == "склад":
        storage_from = shop
        storage_to = store
    else:
        storage_from = store
        storage_to = shop
    if storage_from.get_item(request.product) >= request.amount:
        print(f"Нужное количество есть в {request.from_}е")
    else:
        print(f"Не хватает в {request.from_}е, попробуйте заказать меньше")
        continue
    if not storage_to.can_add(request.product, request.amount):
        print(f"В {request.to}е  недостаточно места, попобуйте что-то другое")
        continue
    storage_from.remove(request.product, request.amount)
    print(f"Курьер забрал {request.amount} {request.product} со {request.from_}а")
    storage_to.add(request.product, request.amount)
    print(f"Курьер доставил {request.amount} {request.product} в {request.to}\n")
    print(storage_from)
    print(storage_to)