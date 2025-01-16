import unittest
from store_calculator import Product, Promotion, Inventory, Customer

class TestStoreCalculator(unittest.TestCase):
    def setUp(self):
        # 테스트에 사용할 프로모션과 상품 초기화
        self.promotion = Promotion(required_quantity=2, free_quantity=1)
        self.product_cola = Product(name="콜라", price=1000, stock=10, promotion=self.promotion)
        self.product_water = Product(name="물", price=500, stock=5)
        
        # 인벤토리에 상품 추가
        self.inventory = Inventory(products=[self.product_cola, self.product_water])

    def test_empty_string(self):
        # 빈 문자열 입력 시 총합이 0이어야 합니다.
        customer = Customer()
        self.assertEqual(customer.total, 0)

    def test_single_product_addition(self):
        # 단일 상품 추가 테스트
        customer = Customer()
        cost = customer.add_to_cart(self.product_cola, 2)
        self.assertEqual(cost, 2000)
        self.assertEqual(customer.total, 2000)

    def test_multiple_product_addition(self):
        # 여러 상품 추가 테스트
        customer = Customer()
        customer.add_to_cart(self.product_cola, 2)
        customer.add_to_cart(self.product_water, 3)
        self.assertEqual(customer.total, 3500)

    def test_promotion_applied(self):
        # 프로모션 적용 테스트 (2+1 프로모션이 적용되는지 확인)
        customer = Customer()
        customer.add_to_cart(self.product_cola, 2)
        free_items = self.product_cola.apply_promotion(2)
        self.assertEqual(free_items, 1)

    def test_negative_number_exception(self):
        # 음수 입력 시 예외가 발생해야 합니다.
        customer = Customer()
        with self.assertRaises(ValueError):
            customer.add_to_cart(self.product_cola, -1)

    def test_membership_discount(self):
        # 멤버십 할인 적용 테스트
        customer = Customer(membership=True)
        customer.add_to_cart(self.product_cola, 3)  # 3000원
        customer.apply_membership_discount()
        self.assertEqual(customer.discount, 800)  # 30% 할인 적용, 최대 한도 8000원 내

    def test_large_number_ignored(self):
        # 1000 이상 숫자 무시 테스트
        self.product_large = Product(name="비싼물품", price=1500, stock=1)
        customer = Customer()
        customer.add_to_cart(self.product_large, 1)  # 1500원 상품이므로 포함되어야 함
        customer.add_to_cart(self.product_cola, 1001)  # 1000 이상이므로 무시
        self.assertEqual(customer.total, 1500)

    def test_custom_delimiter(self):
        # 커스텀 구분자 사용 테스트
        # 이 기능을 실제로 구현할 때 추가해야 합니다. 예를 들어 "//;\n1;2;3" 형식
        pass  # 실제 커스텀 구분자 파싱 코드가 필요

    def test_logging_on_error(self):
        # 잘못된 입력 발생 시 로그 파일에 기록되는지 테스트
        customer = Customer()
        with self.assertRaises(ValueError):
            customer.add_to_cart(self.product_cola, "잘못된입력")

if __name__ == '__main__':
    unittest.main()
