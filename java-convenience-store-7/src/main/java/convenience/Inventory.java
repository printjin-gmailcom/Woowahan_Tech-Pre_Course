package convenience;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Inventory {
    private Map<String, Product> products;

    public Inventory() {
        products = new HashMap<>();
        loadProducts("src/main/resources/products.md");
    }

    // products.md 파일에서 상품 정보를 읽어들여 products에 추가
    private void loadProducts(String filePath) {
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            reader.readLine(); // 첫 줄은 헤더이므로 건너뜁니다.
            while ((line = reader.readLine()) != null) {
                String[] details = line.split(",");
                String name = details[0];
                int price = Integer.parseInt(details[1]);
                int quantity = Integer.parseInt(details[2]);
                String promotion = details[3].equals("null") ? null : details[3];

                Product product = new Product(name, price, quantity, promotion);
                products.put(name, product);
            }
        } catch (IOException e) {
            System.out.println("[ERROR] products.md 파일을 읽는 도중 오류가 발생했습니다.");
        }
    }

    public Product getProduct(String name) {
        if (!products.containsKey(name)) {
            throw new IllegalArgumentException("[ERROR] 존재하지 않는 상품입니다.");
        }
        return products.get(name);
    }

    public void updateStock(String name, int amount) {
        Product product = getProduct(name);
        if (amount > product.getStock()) {
            throw new IllegalArgumentException("[ERROR] 재고 수량을 초과하여 구매할 수 없습니다.");
        }
        product.decreaseStock(amount);
    }
}
