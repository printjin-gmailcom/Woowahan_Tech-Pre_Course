package convenience;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;

public class Promotion {
    private String name;
    private int buy;
    private int get;
    private LocalDate startDate;
    private LocalDate endDate;

    private static Map<String, Promotion> promotions = new HashMap<>();

    public Promotion(String name, int buy, int get, LocalDate startDate, LocalDate endDate) {
        this.name = name;
        this.buy = buy;
        this.get = get;
        this.startDate = startDate;
        this.endDate = endDate;
    }

    public static void loadPromotions(String filePath) {
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            reader.readLine(); // 첫 줄은 헤더이므로 건너뜁니다.
            while ((line = reader.readLine()) != null) {
                String[] details = line.split(",");
                String name = details[0];
                int buy = Integer.parseInt(details[1]);
                int get = Integer.parseInt(details[2]);
                LocalDate startDate = LocalDate.parse(details[3]);
                LocalDate endDate = LocalDate.parse(details[4]);

                Promotion promotion = new Promotion(name, buy, get, startDate, endDate);
                promotions.put(name, promotion);
            }
        } catch (IOException e) {
            System.out.println("[ERROR] promotions.md 파일을 읽는 도중 오류가 발생했습니다.");
        }
    }

    public static Promotion getPromotion(String name) {
        return promotions.get(name);
    }

    public boolean isValid() {
        LocalDate today = LocalDate.now();
        return (today.isAfter(startDate) || today.isEqual(startDate)) &&
               (today.isBefore(endDate) || today.isEqual(endDate));
    }

    public int getBuy() {
        return buy;
    }

    public int getGet() {
        return get;
    }
}
