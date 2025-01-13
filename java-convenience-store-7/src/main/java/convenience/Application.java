package convenience;

public class Application {
    public static void main(String[] args) {
        System.out.println("W 편의점 결제 시스템에 오신 것을 환영합니다.");
        
        PaymentService paymentService = new PaymentService();
        paymentService.start();  // 결제 로직 시작
    }
}
