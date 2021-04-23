import requests


# making request to form an dict with exchange rates

def request():
    currency = input().lower()

    r = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
    reading = r.json()

    # creating a cache using dict
    if currency == "usd":
        cache = {"eur": reading["eur"]["rate"]}

    elif currency == "eur":
        cache = {"usd": reading["usd"]["rate"]}
    else:
        cache = {"usd": reading["usd"]["rate"], "eur": reading["eur"]["rate"]}

    while True:
        exchange_currency = input().lower()
        if exchange_currency == "":
            break
        value = float(input())
        print("Checking the cache...")
        if f"{exchange_currency}" in cache:
            print("Oh! It is in the cache!")

            balance = float(reading[f"{exchange_currency}"]["rate"]) * value

            print("You received", balance, f"{exchange_currency}".upper())
        else:
            print("Sorry, but it is not in the cache!")
            add_value = float(reading[f"{exchange_currency}"]["rate"])
            cache[f"{exchange_currency}"] = add_value
            balance = float(reading[f"{exchange_currency}"]["rate"]) * value

            print("You received", balance, f"{exchange_currency}".upper())


if __name__ == '__main__':
    request()
