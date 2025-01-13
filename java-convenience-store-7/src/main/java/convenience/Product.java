package convenience;

public class Product {
    private String name;
    private int price;
    private int stock;
    private String promotion;

    public Product(String name, int price, int stock, String promotion) {
        this.name = name;
        this.price = price;
        this.stock = stock;
        this.promotion = promotion;
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }

    public int getStock() {
        return stock;
    }

    public String getPromotion() {
        return promotion;
    }

    public void decreaseStock(int amount) {
        if (amount <= stock) {
            stock -= amount;
        } else {
            throw new IllegalArgumentException("[ERROR] 재고 수량을 초과할 수 없습니다.");
        }
    }
}
