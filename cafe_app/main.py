from models.item import Item
from models.order import Order
from models.user import User

from database.db_init import init_db
from database.db_actions import insert_user, insert_order
from utils.analytics import get_top_users

def main():
    init_db()

    user1 = User("Bob")
    user2 = User("Alice")

    pizza = Item("Пицца", 50)
    tea = Item("Tea", 5)
    salad = Item("salad", 25)

    order1 = Order(user1)
    order1.add_item(pizza)
    order1.add_item(tea)


    order2 = Order(user2)
    order2.add_item(tea)
    order2.add_item(pizza)
    order2.add_item(salad)

    order3 = Order(user1)
    order3.add_item(salad)
    order3.add_item(tea)

    insert_user(user1)
    insert_user(user2)

    insert_order(order1)
    insert_order(order2)
    insert_order(order3)

    orders = [order1, order2, order3]

    print("----Orders----")
    for o in orders:
        print(o)

    print("----Top Users----")
    for user, total in get_top_users(orders):
        print(f"{user} : {total} $")

if __name__ == "__main__":
    main()