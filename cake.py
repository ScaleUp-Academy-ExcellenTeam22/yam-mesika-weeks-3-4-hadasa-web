"#hadasa-web"


def get_recipe_price(price, *ingredients, optionals=[]):
    pricee = 0
    val = list(price.keys())

    try:
        if isinstance(ingredients[-1], list):
            optionals = ingredients[-1]
            ingredients = ingredients[:-1]
        for i in range(len(ingredients)):
            if not i in optionals:
                pricee += price[val[i]] * (ingredients[i] / 100)
    except:
        pricee = 0
    return int(pricee)


print(get_recipe_price({'chocolate': 18, 'milk': 8}, 200, 100))

print(get_recipe_price({'chocolate': 18, 'milk': 8}, 300, ['milk']))

print(get_recipe_price({}))