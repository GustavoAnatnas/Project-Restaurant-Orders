import csv
import collections


def read_orders_log(path_to_file):
    with open(path_to_file, newline='') as file:
        reader = csv.reader(file)
        orders = [(row[0], row[1], row[2]) for row in reader]
    return orders


def most_ordered_dish_by_client(orders, client):
    client_orders = [order[1] for order in orders if order[0] == client]
    dish_count = collections.Counter(client_orders)
    most_ordered_dish = max(dish_count, key=dish_count.get)
    return most_ordered_dish


def times_ordered_dish_by_client(orders, client, dish):
    client_orders = [(order[0], order[1]) for order in orders if
                     order[0] == client and order[1] == dish]
    times_ordered = len(client_orders)
    return times_ordered


def dishes_never_ordered_by_client(orders, client):
    client_orders = [order[1] for order in orders if order[0] == client]
    all_dishes = set([order[1] for order in orders])
    never_ordered_dishes = all_dishes - set(client_orders)
    return sorted(never_ordered_dishes)


def days_never_visited_by_client(orders, client):
    client_days_visited = {order[2].lower() for order in
                           orders if order[0] == client}
    all_days = {'segunda-feira', 'terça-feira', 'quarta-feira',
                'quinta-feira', 'sexta-feira', 'sábado', 'domingo'}
    never_visited_days = all_days - client_days_visited
    return never_visited_days


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        orders = read_orders_log(path_to_file)
        with open('output.txt', 'w') as f:
            f.write(str(most_ordered_dish_by_client(orders, 'maria')) + '\n')
            f.write(str(times_ordered_dish_by_client(orders, 'arnaldo',
                                                     'hamburguer')) + '\n')
            f.write(str(dishes_never_ordered_by_client(orders, 'joao')) + '\n')
            f.write(str(days_never_visited_by_client(orders, 'jose')) + '\n')
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
