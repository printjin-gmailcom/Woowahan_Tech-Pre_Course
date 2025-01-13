package convenience;

import convenience.utils.ConsoleUtils;
import java.util.Scanner;

public class PaymentService {
    private Inventory inventory;
    private MembershipDiscount membershipDiscount;

    public PaymentService() {
        this.inventory = new Inventory();
        this.membershipDiscount = new MembershipDiscount();
        Promotion.loadPromotions("src/main/resources/promotions.md");
    }

    public void start() {
        Scanner scanner = new Scanner(System.in);
        Receipt receipt = new Receipt();
        int promotionDiscount = 0;

        ConsoleUtils.printMessage("구매하실 상품명과 수량을 입력해 주세요. (예: [사이다-2],[감자칩-1])");
        String input = ConsoleUtils.readInput();

        String[] items = input.split(",");
        for (String item : items) {
            String[] details = item.replace("[", "").replace("]", "").split("-");
            String productName = details[0];
            int quantity = Integer.parseInt(details[1]);

            try {
                Product product = inventory.getProduct(productName);
                int totalPrice = product.getPrice() * quantity;

                int discountForProduct = 0;
                if (product.getPromotion() != null) {
                    Promotion promotion = Promotion.getPromotion(product.getPromotion());
                    if (promotion != null && promotion.isValid()) {
                        int bonus = promotion.getGet() * (quantity / promotion.getBuy());
                        discountForProduct = bonus * product.getPrice();
                        promotionDiscount += discountForProduct;
                        ConsoleUtils.printMessage(String.format("%s %d개 총액: %d원 (증정: %d개)", productName, quantity, totalPrice, bonus));
                    } else {
                        ConsoleUtils.printMessage(String.format("%s %d개 총액: %d원 (프로모션 없음)", productName, quantity, totalPrice));
                    }
                } else {
                    ConsoleUtils.printMessage(String.format("%s %d개 총액: %d원", productName, quantity, totalPrice));
                }

                receipt.addItem(productName, quantity, totalPrice);
                receipt.setTotalAmount(receipt.getFinalAmount() + totalPrice - discountForProduct);
                inventory.updateStock(productName, quantity);

            } catch (IllegalArgumentException e) {
                ConsoleUtils.printError(e.getMessage());
            }
        }

        receipt.applyPromotionDiscount(promotionDiscount);

        ConsoleUtils.printMessage("멤버십 할인을 적용하시겠습니까? (Y/N): ");
        String applyDiscount = ConsoleUtils.readInput();

        if ("Y".equalsIgnoreCase(applyDiscount)) {
            int membershipDiscountAmount = membershipDiscount.applyDiscount(receipt.getFinalAmount() - promotionDiscount);
            receipt.applyMembershipDiscount(membershipDiscountAmount);
        }

        receipt.calculateFinalAmount();
        receipt.printReceipt();

        scanner.close();
    }
}
