package convenience;

import java.util.ArrayList;
import java.util.List;

public class Receipt {
    private List<String> purchasedItems;
    private int totalAmount;
    private int promotionDiscount;
    private int membershipDiscount;
    private int finalAmount;

    public Receipt() {
        purchasedItems = new ArrayList<>();
    }

    public void addItem(String name, int quantity, int price) {
        purchasedItems.add(String.format("%s\t%d\t%d원", name, quantity, price));
    }

    public void applyPromotionDiscount(int discount) {
        promotionDiscount = discount;
    }

    public void applyMembershipDiscount(int discount) {
        membershipDiscount = discount;
    }

    public void calculateFinalAmount() {
        finalAmount = totalAmount - promotionDiscount - membershipDiscount;
    }

    public void printReceipt() {
        System.out.println("===========W 편의점=============");
        System.out.println("상품명\t수량\t금액");
        for (String item : purchasedItems) {
            System.out.println(item);
        }
        System.out.println("===========증\t정=============");
        System.out.printf("총구매액\t\t%d원\n", totalAmount);
        System.out.printf("행사할인\t\t-%d원\n", promotionDiscount);
        System.out.printf("멤버십할인\t\t-%d원\n", membershipDiscount);
        System.out.printf("내실돈\t\t%d원\n", finalAmount);
        System.out.println("================================");
    }

    public void setTotalAmount(int amount) {
        totalAmount = amount;
    }

    public int getFinalAmount() {
        return finalAmount;
    }
}
