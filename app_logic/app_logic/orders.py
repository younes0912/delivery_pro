class OrderManager:
    def __init__(self):
        self.current_order = []

    def add_to_order(self, item, price):
        self.current_order.append({"item": item, "price": price})
        return f"تم إضافة {item} بنجاح ✅"

    def get_total(self):
        return sum(item['price'] for item in self.current_order)
