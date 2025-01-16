import json
from datetime import datetime

class Product:
    def __init__(self, name, price, stock, promotion=None):
        self.name = name
        self.price = price
        self.stock = stock
        self.promotion = promotion

    def apply_promotion(self, quantity):
        # Apply promotion if eligible
        if self.promotion and quantity >= self.promotion.required_quantity:
            free_items = quantity // self.promotion.required_quantity
            return free_items
        return 0

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            print(f"[ERROR] 재고가 부족합니다. {self.name}의 현재 재고는 {self.stock}개입니다.")
            return False

class Promotion:
    def __init__(self, required_quantity, free_quantity):
        self.required_quantity = required_quantity
        self.free_quantity = free_quantity

class Inventory:
    def __init__(self, products):
        self.products = {product.name: product for product in products}

    def get_product(self, product_name):
        return self.products.get(product_name, None)

    def display_products(self):
        print("현재 보유하고 있는 상품입니다:")
        for product in self.products.values():
            promo_text = f" {product.promotion.required_quantity}+{product.promotion.free_quantity}" if product.promotion else ""
            stock_text = "재고 없음" if product.stock <= 0 else f"{product.stock}개"
            print(f"- {product.name} {product.price}원 {stock_text}{promo_text}")

class Customer:
    def __init__(self, membership=False):
        self.cart = {}
        self.membership = membership
        self.total = 0
        self.discount = 0

    def add_to_cart(self, product, quantity):
        if product.update_stock(quantity):
            self.cart[product.name] = self.cart.get(product.name, 0) + quantity
            cost = product.price * quantity
            self.total += cost
            return cost
        return 0

    def apply_membership_discount(self):
        if self.membership:
            self.discount = min(self.total * 0.3, 8000)
            self.total -= self.discount

    def generate_receipt(self):
        print("=========== W 편의점 =============")
        for item, quantity in self.cart.items():
            print(f"{item}\t{quantity}\t{self.cart[item] * quantity}")
        print(f"총구매액:\t{self.total + self.discount}")
        print(f"멤버십할인:\t-{self.discount}")
        print(f"내실돈:\t{self.total}")

def load_inventory_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        products = []
        for item in data["products"]:
            promotion = Promotion(item["promotion"][0], item["promotion"][1]) if "promotion" in item else None
            products.append(Product(item["name"], item["price"], item["stock"], promotion))
        return Inventory(products)

def main():
    inventory = load_inventory_from_file("products.json")
    customer = Customer(membership=True)  # 예시: 멤버십 회원으로 설정
    while True:
        inventory.display_products()
        selection = input("구매하실 상품명과 수량을 입력해 주세요. (예: [사이다-2],[감자칩-1]): ")
        try:
            items = selection.strip().split(",")
            for item in items:
                name, qty = item.strip("[]").split("-")
                product = inventory.get_product(name)
                if product:
                    qty = int(qty)
                    cost = customer.add_to_cart(product, qty)
                    print(f"{name} {qty}개 추가됨: {cost}원")
                else:
                    print(f"[ERROR] 존재하지 않는 상품입니다: {name}")
        except ValueError:
            print("[ERROR] 올바르지 않은 형식입니다. 다시 입력해 주세요.")
            continue

        more = input("추가 구매를 진행하시겠습니까? (Y/N): ").strip().upper()
        if more == 'N':
            break

    customer.apply_membership_discount()
    customer.generate_receipt()

if __name__ == "__main__":
    main()
