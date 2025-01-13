package convenience;

public class MembershipDiscount {
    private static final double DISCOUNT_RATE = 0.3;
    private static final int MAX_DISCOUNT = 8000;

    public int applyDiscount(int totalAmount) {
        int discount = (int) (totalAmount * DISCOUNT_RATE);
        return Math.min(discount, MAX_DISCOUNT);
    }
}
