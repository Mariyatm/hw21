class Request:
    def __init__(self, str_request):
        parse_request = Request.parse_requst(str_request)
        self._from = parse_request["from_"]
        self._to = parse_request["to"]
        self._amount = parse_request["amount"]
        self._product = parse_request["product"]

    @property
    def from_(self):
        return self._from

    @property
    def to(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product

    @staticmethod
    def parse_requst(str_reuest):
        split_request = str_reuest.split()
        amount = int(split_request[1])
        product = split_request[2]
        from_ = split_request[4]
        to = split_request[6]
        return {"from_": from_, "to": to, "amount": amount, "product": product}
