def get_top_users(orders, top_n=3):
    user_spend = {}
    for order in orders:
        user_spend[order.user.name] = user_spend.get(order.user.name, 0) + order.total()

    sorted_users = sorted(user_spend.items(), key=lambda x: x[1], reverse=True)
    return sorted_users[:top_n]