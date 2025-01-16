import json
from datetime import datetime

class Product:
    def __init__(self, name, price, stock, promotion=None):
        self.name = name
        self.price = price
        self.stock = stock
        self.promotion = promotion

    def apply_promotion(self, quantity, promo_date=None):
        # Check if the current date is within promotion period if specified
        if promo_date and promo_date != datetime.now().date():
            return 0  # No promotion applied if date doesn't match

        # Apply promotion if eligible
        if self.promotion and quantity >= self.promotion.required_quantity:
            free_items = (quantity // self.promotion.required_quantity) * self.promotion.free_quantity
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
    def __init__(self, required_quantity, free_quantity, promo_start_date=None, promo_end_date=None):
        self.required_quantity = required_quantity
        self.free_quantity = free_quantity
        self.promo_start_date = promo_start_date
        self.promo_end_date = promo_end_date

    def is_promo_valid(self):
        today = datetime.now().date()
        return (self.promo_start_date <= today <= self.promo_end_date) if self.promo_start_date and self.promo_end_date else True

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

    def save_inventory(self, filename="products.json"):
        # Save updated stock levels back to file
        data = {"products": [{"name": product.name, "price": product.price, "stock": product.stock} for product in self.products.values()]}
        with open(filename, 'w') as file:
            json.dump(data, file)

class Customer:
    def __init__(self, membership=False):
        self.cart = {}
        self.membership = membership
        self.total = 0
        self.discount = 0
        self.promotion_discount = 0

    def add_to_cart(self, product, quantity, promo_date=None):
        if product.update_stock(quantity):
            free_items = product.apply_promotion(quantity, promo_date)
            self.cart[product.name] = {"quantity": quantity, "free_items": free_items, "unit_price": product.price}
            cost = product.price * quantity
            promo_discount = free_items * product.price
            self.total += cost
            self.promotion_discount += promo_discount
            print(f"{product.name} {quantity}개 추가됨: {cost}원 (프로모션 할인: -{promo_discount}원)")
            return cost
        return 0

    def apply_membership_discount(self):
        if self.membership:
            self.discount = min((self.total - self.promotion_discount) * 0.3, 8000)
            self.total -= self.discount

    def generate_receipt(self):
        print("\n=========== W 편의점 =============")
        print("상품명\t\t수량\t금액")
        for item, details in self.cart.items():
            print(f"{item}\t\t{details['quantity']}\t{details['quantity'] * details['unit_price']}")
        print("=========== 증정 상품 =============")
        for item, details in self.cart.items():
            if details["free_items"] > 0:
                print(f"{item}\t\t{details['free_items']}개 무료")
        print("===================================")
        print(f"총구매액:\t\t{self.total + self.discount + self.promotion_discount}원")
        print(f"행사할인:\t\t-{self.promotion_discount}원")
        print(f"멤버십할인:\t\t-{self.discount}원")
        print(f"내실돈:\t\t{self.total}원")
        print("===================================\n")

    def cancel_purchase(self):
        # Clear the cart and reset totals
        self.cart.clear()
        self.total = 0
        self.discount = 0
        self.promotion_discount = 0
        print("구매가 취소되었습니다.")

def load_inventory_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        products = []
        for item in data["products"]:
            promotion = Promotion(item["promotion"][0], item["promotion"][1], item.get("promo_start_date"), item.get("promo_end_date")) if "promotion" in item else None
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
                    promo_date = datetime.now().date()
                    cost = customer.add_to_cart(product, qty, promo_date)
                    if product.promotion and qty < product.promotion.required_quantity:
                        print(f"{product.name} {product.promotion.required_quantity}개 이상 구매 시 {product.promotion.free_quantity}개 무료 증정. 추가 구매하시겠습니까? (Y/N)")
                else:
                    print(f"[ERROR] 존재하지 않는 상품입니다: {name}")
        except ValueError:
            print("[ERROR] 올바르지 않은 형식입니다. 다시 입력해 주세요.")
            continue

        action = input("추가 구매 또는 결제 취소하시겠습니까? (Y/N/C): ").strip().upper()
        if action == 'C':
            customer.cancel_purchase()
            continue  # Start over after canceling

        if action == 'N':
            break

    customer.apply_membership_discount()
    customer.generate_receipt()
    inventory.save_inventory()  # Save updated stock to file

if __name__ == "__main__":
    main()
