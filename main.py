import random
import string

def generate_nitro_links(quantity, link_type):
    nitro_links = []

    for _ in range(quantity):
        if link_type == "promo":
            code = "-".join(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4)) for _ in range(6))
            base_url = "https://discord.com/billing/promotions/"
        else:
            code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
            base_url = "https://discord.gift/"
        
        nitro_links.append(f"{base_url}{code}")

    for index, link in enumerate(nitro_links, start=1):
        print(f"{index}: {link}")

def main():
    link_type = input("Promo (p) or Gift (g)?: ").strip().lower()
    if link_type not in ("p", "g"):
        print("有効な値を入力してください")
        return

    link_type = "promo" if link_type == "p" else "nitro"

    try:
        quantity = int(input("Count: ").strip())
        if quantity <= 0:
            print("正の整数を入力してください")
            return
    except ValueError:
        print("有効な数字を入力してください")
        return

    generate_nitro_links(quantity, link_type)

if __name__ == "__main__":
    main()
