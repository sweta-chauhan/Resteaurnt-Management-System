def single(food):
    return {
        "id": str(food["id"]),
        "name": food["name"],
        "slot": food["slot"],
        "price": food["price"],
        "inStock": food["inStock"],
        "category": food["category"]
    }


def multiple(foods):
    return [single(food) for food in foods]