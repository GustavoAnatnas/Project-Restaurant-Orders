class TrackOrders:
    def __init__(self):
        self.orders = []
        self.customers = {}
        self.days = {}

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))
        if customer not in self.customers:
            self.customers[customer] = set()
        self.customers[customer].add(order)
        if customer not in self.days:
            self.days[customer] = set()
        self.days[customer].add(day)

    def get_most_ordered_dish_per_customer(self, customer):
        if customer in self.customers:
            order_count = {}
            for order in self.customers[customer]:
                order_count[order] = sum([1 for c, o, d in self.orders 
                                          if c == customer and o == order])
            if order_count:
                return max(order_count, key=order_count.get)

    def get_never_ordered_per_customer(self, customer):
        if customer in self.customers:
            all_orders = set([o for c, o, d in self.orders])
            return all_orders - self.customers[customer]

    def get_days_never_visited_per_customer(self, customer):
        if customer in self.days:
            all_days = set([d for c, o, d in self.orders])
            return all_days - self.days[customer]

    def get_busiest_day(self):
        day_count = {}
        for day in set([d for c, o, d in self.orders]):
            day_count[day] = sum([1 for c, o, d in self.orders if d == day])
        if day_count:
            return max(day_count, key=day_count.get)

    def get_least_busy_day(self):
        day_count = {}
        for day in set([d for c, o, d in self.orders]):
            day_count[day] = sum([1 for c, o, d in self.orders if d == day])
        if day_count:
            return min(day_count, key=day_count.get)
